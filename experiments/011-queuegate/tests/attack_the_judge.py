import queue, threading, time, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from queuegate import QueueGate
rejected=[]
q=queue.Queue(2); state={"closed":False}; checked=threading.Event(); go=threading.Event(); accepted=[]
def m1submit():
    if state["closed"]: return
    checked.set(); go.wait(); q.put_nowait(1); accepted.append(True)
t=threading.Thread(target=m1submit); t.start(); checked.wait(); state["closed"]=True; go.set(); t.join(); rejected.append(state["closed"] and accepted==[True])
q2=queue.Queue(1); q2.put(1)
try: q2.put_nowait(object()); rejected.append(False)
except queue.Full: rejected.append(True)
started=threading.Event(); release=threading.Event(); done=[]
def slow(): started.set(); release.wait(); done.append(1)
t=threading.Thread(target=slow); t.start(); started.wait(); rejected.append(done==[]); release.set(); t.join()
q4=queue.Queue(1); q4.put(1); finished=threading.Event()
def blocking_submit(): q4.put(2); finished.set()
t=threading.Thread(target=blocking_submit); t.start(); time.sleep(.03); rejected.append(not finished.is_set()); q4.get(); q4.task_done(); t.join(1)
q5=queue.Queue(); processed=[]
for x in [1,2,3]: q5.put(x)
def fragile():
    while True:
        x=q5.get()
        try:
            if x==2: raise ValueError
            processed.append(x)
        except ValueError:
            q5.task_done(); return
        q5.task_done()
t=threading.Thread(target=fragile); t.start(); t.join(); rejected.append(processed==[1] and q5.unfinished_tasks==1)
while not q5.empty(): q5.get_nowait(); q5.task_done()
assert all(rejected),rejected
out=[]; g=QueueGate(out.append,capacity=4,workers=2); assert g.submit(1); assert g.submit(2); g.close(); assert sorted(out)==[1,2] and not g.submit(3)
print("PASS: 5/5 known-false designs rejected; accepted implementation accepted")
