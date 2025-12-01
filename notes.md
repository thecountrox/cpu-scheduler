What is a CPU Scheduler:
A CPU Scheduler is a program mostly driven by a distinct group of algorithms.

A CPU gets a lot of processes and limited processing time or processing power at any given point in time.

To balance this to our requirement we use a CPU scheduling algorithm tailored to our needs.

There are various metrics you can derive from just how the processes behave under different cpu scheduling algorithms.
Some of the metrics are:

- Arrival Time (AT)
- Completion Time (CT)
- Burst Time (BT)
- Turn around Time (TBT)
- Waiting Time (WT)

Depending on the nature of our workflow we may prefer to pay attention to one of these attributes over the other.

For example in a system that requires immediate processing (realtime systems) we prefer to have the least Waiting time.
In other Systems like Big Data Systems we prefer Throughput over Actual Completion times

This repo will contain my implementations of the most common CPU scheduling algorithms.

---

Okay so the following needs to be implemented before I can even think about the algorithms themselves:

- Input functions
- Standard notations for processes and process list
- Gnatt Chart Generator
