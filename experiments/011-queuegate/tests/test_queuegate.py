import threading,time,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from queuegate import QueueGate

class Tests(unittest.TestCase):
    def test_one(self):
        out=[]; g=QueueGate(out.append,capacity=2); self.assertTrue(g.submit(1)); g.close(); self.assertEqual(out,[1])
    def test_reject_after_close(self):
        g=QueueGate(lambda x:None,capacity=1); g.close(); self.assertFalse(g.submit(1))
    def test_close_drains(self):
        out=[]; g=QueueGate(out.append,capacity=10)
        for x in range(10): self.assertTrue(g.submit(x))
        g.close(); self.assertEqual(sorted(out),list(range(10)))
    def test_full_is_explicit_rejection(self):
        started=threading.Event(); release=threading.Event(); out=[]
        def h(x): started.set(); release.wait(); out.append(x)
        g=QueueGate(h,capacity=2); self.assertTrue(g.submit(0)); started.wait()
        self.assertTrue(g.submit(1)); self.assertTrue(g.submit(2)); self.assertFalse(g.submit(3))
        release.set(); g.close(); self.assertEqual(sorted(out),[0,1,2])
    def test_repeated_close(self):
        g=QueueGate(lambda x:None,capacity=1); g.close(); g.close(); self.assertTrue(g.closed)
    def test_concurrent_close_idempotent(self):
        out=[]; g=QueueGate(out.append,capacity=10,workers=2)
        for i in range(5): g.submit(i)
        ts=[threading.Thread(target=g.close) for _ in range(4)]
        [t.start() for t in ts]; [t.join(2) for t in ts]
        self.assertTrue(all(not t.is_alive() for t in ts)); self.assertEqual(sorted(out),list(range(5)))
    def test_handler_exception_does_not_lose_later_work(self):
        out=[]
        def h(x):
            if x==2: raise ValueError("boom")
            out.append(x)
        g=QueueGate(h,capacity=10)
        for i in range(5): g.submit(i)
        g.close(); self.assertEqual(out,[0,1,3,4]); self.assertEqual(len(g.errors),1); self.assertEqual(g.errors[0][0],2)
    def test_concurrent_producers_accepted_equals_processed_once(self):
        processed=[]; plock=threading.Lock()
        def h(x):
            with plock: processed.append(x)
        g=QueueGate(h,capacity=64,workers=4)
        accepted=[]; alock=threading.Lock()
        def prod(base):
            for i in range(250):
                x=base+i
                if g.submit(x):
                    with alock: accepted.append(x)
                else:
                    time.sleep(0.0002)
                    if g.submit(x):
                        with alock: accepted.append(x)
        ts=[threading.Thread(target=prod,args=(k*1000,)) for k in range(6)]
        [t.start() for t in ts]; [t.join() for t in ts]; g.close()
        self.assertEqual(len(processed),len(set(processed))); self.assertEqual(set(processed),set(accepted))
    def test_multiple_workers_no_duplication(self):
        out=[]; lock=threading.Lock()
        def h(x):
            with lock: out.append(x)
        g=QueueGate(h,capacity=100,workers=5)
        for i in range(100): self.assertTrue(g.submit(i))
        g.close(); self.assertEqual(len(out),100); self.assertEqual(set(out),set(range(100)))
    def test_empty_close(self):
        g=QueueGate(lambda x:None,capacity=3,workers=3); g.close(); self.assertTrue(g.closed)
    def test_post_green_close_submit_race(self):
        for roundno in range(200):
            processed=[]; lock=threading.Lock()
            def h(x):
                with lock: processed.append(x)
            g=QueueGate(h,capacity=8,workers=2); accepted=[]; gate=threading.Barrier(5)
            def producer(k):
                gate.wait()
                for i in range(20):
                    x=k*100+i
                    if g.submit(x): accepted.append(x)
            ps=[threading.Thread(target=producer,args=(k,)) for k in range(4)]
            for p in ps:p.start()
            gate.wait(); c=threading.Thread(target=g.close); c.start()
            for p in ps:p.join()
            c.join(2); self.assertFalse(c.is_alive()); self.assertEqual(len(processed),len(set(processed))); self.assertEqual(set(processed),set(accepted)); self.assertFalse(g.submit(999999))

if __name__=="__main__": unittest.main(verbosity=2)
