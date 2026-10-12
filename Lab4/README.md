# Lab 4 — Data Structures & Algorithms

> **Introduction to AI and Its Application Using Python**

| Navigation | |
|---|---|
| **Repository hub** | [← Back to main README](../README.md) |

---

## Overview

Lab 4 moves from Python syntax into classic computer-science building blocks.
Each task implements a data structure or algorithm **using a class and objects**,
putting the object-oriented material from Lab 2 to work:

- a **stack** (LIFO) built on a fixed-size array,
- a **queue** (FIFO) built on a fixed-size array,
- **binary search** over an array that is first sorted with bubble sort.

Each task is an independent runnable script — run it and follow the prompts.

## Files in This Lab

| # | File | Topic |
|---|------|-------|
| 01 | [`task1.py`](task1.py) | Stack — `push`, `pop`, `peek` |
| 02 | [`task2.py`](task2.py) | Queue — `enqueue`, `dequeue` |
| 03 | [`task3.py`](task3.py) | Binary search (after bubble sort) |

---

## Detailed File Guide

### task1.py — Stack (LIFO)

Implements a stack as a class backed by a fixed-size list, with a `top` index
that tracks the last element (`-1` means the stack is empty).

**Concepts demonstrated:**
- A class with an `__init__` that stores fixed-length state
  (`self.stack = [None] * size`, `self.top = -1`)
- `push(x)` — move the top pointer up and store the value
- `pop()` — return the top value, clear its slot, move the top pointer down
- `peek()` — read the top value without removing it
- Slicing the underlying array (`self.stack[:self.top + 1]`) to show the live stack

**Interactive flow:** asks for the stack size, pushes that many values, then
prints the stack, its top element, pops one value and prints the result.

---

### task2.py — Queue (FIFO)

Implements a queue as a class backed by a fixed-size list, with `front` and
`rear` indices tracking the two ends.

**Concepts demonstrated:**
- Two index pointers: `self.front = 0` and `self.rear = -1`
- `enqueue(y)` — move the rear pointer forward and store the value
- `dequeue()` — return the front value, clear its slot, move the front pointer
- Slicing the live queue (`self.queue[self.front:self.rear + 1]`)

**Interactive flow:** asks for the queue size, enqueues that many values,
prints the queue, then dequeues twice and prints the result after each removal.

**Key point:** a stack removes the **newest** element (LIFO); a queue removes
the **oldest** element (FIFO).

---

### task3.py — Binary Search

Implements binary search in a class, after sorting the array with bubble sort so
the search precondition (a sorted array) is guaranteed.

**Concepts demonstrated:**
- `bubble_sort()` — in-place comparison sort with nested loops and tuple-swap
- `search(target)` — iterative binary search with `low`, `high` and `mid`
- Returning the **index** when the target is found, or `-1` when it is not
- Sorting is required: binary search only works on ordered data

**Interactive flow:** works on a fixed sample array, prints the sorted array,
then prompts for the number to search and reports its index (or "not found").

---

## How to Run

Each script is independent — run any of them with:

```bash
cd Lab4
python3 task1.py
python3 task2.py
python3 task3.py
```

> **Note:** All three scripts require interactive input when run.

**Requirements:** Python 3.6+ · no external packages

---

| Navigation | |
|---|---|
| **Repository hub** | [← Back to main README](../README.md) |
