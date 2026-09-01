# Decision Map — QueueGate

1. What operation is the authority for admission?
2. How is close ordered against concurrent submitters?
3. What does the capacity bound include?
4. How does shutdown wait for already accepted work without losing it?
5. Can worker termination be signaled safely when the queue is full?
6. What evidence establishes accepted-set = processed-set exactly once?
