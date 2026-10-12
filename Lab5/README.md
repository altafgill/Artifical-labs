# Lab 5 — Graphs, Trees & BFS

> **Introduction to AI and Its Application Using Python**

| Navigation | |
|---|---|
| **Repository hub** | [← Back to main README](../README.md) |

---

## Overview

Lab 5 introduces the structures that underpin search and AI problem-solving:
**graphs**, **trees**, **breadth-first search (BFS)** and a **priority queue**.
Each task is implemented with classes and objects and is an independent runnable
script — run it and follow the prompts (or read the traversal output directly).

## Files in This Lab

| # | File | Topic |
|---|------|-------|
| 01 | [`task1.py`](task1.py) | Graph + Breadth-First Search (BFS) |
| 02 | [`task2.py`](task2.py) | Tree + BFS to a goal node (shortest path) |
| 03 | [`task3.py`](task3.py) | Priority queue as a min-heap |

---

## Detailed File Guide

### task1.py — Graph and Breadth-First Search

Implements an undirected graph as an **adjacency list** (a dictionary mapping
each node to its neighbours) and traverses it with BFS.

**Concepts demonstrated:**
- `add_node(node)` and `add_edge(u, v)` — an undirected edge is stored in
  **both** directions
- `bfs(start)` using `collections.deque` as the FIFO queue
- A `seen` set to avoid revisiting nodes and a `visited` list to record order

**Output:** prints the adjacency list of the sample graph, then asks for a
starting node and prints the BFS visit order.

---

### task2.py — Tree and BFS to a Goal (Shortest Path)

Implements a tree as a directed adjacency list (parent → children) and runs a
BFS that **stops as soon as the goal node is reached**, rebuilding the path from
the start node.

**Concepts demonstrated:**
- A hand-written `Queue` class (`enqueue`, `dequeue`, `is_empty`)
- A `Tree` class whose edges go one way (`add_edge(parent, child)`)
- `bfs_goal(start, goal)` — a `parent` dictionary remembers how each node was
  reached; the goal is detected on dequeue
- Rebuilding the route by walking `parent` links back from the goal and
  reversing it

**Output:** prints the tree's adjacency list, the BFS order (stopped at goal G)
and the path `A → … → G`.

---

### task3.py — Priority Queue (Min-Heap)

Implements a priority queue as a **min-heap**: the smallest value is always
removed first. Ordering is maintained with the classic sift operations.

**Concepts demonstrated:**
- Array-based binary heap with index arithmetic
  (`parent = (i-1)//2`, `left = 2*i+1`, `right = 2*i+2`)
- `_sift_up(index)` used by `insert(value)`
- `_sift_down(index)` used by `extract_min()`
- `peek()` reads the minimum without removing it; `is_empty()` guards the loop

**Interactive flow:** asks for the number of elements and their values, prints
the heap and its smallest element, then removes every element in priority order.

---

## How to Run

Each script is independent — run any of them with:

```bash
cd Lab5
python3 task1.py
python3 task2.py
python3 task3.py
```

> **Note:** `task1.py` and `task3.py` require interactive input when run;
> `task2.py` prints its results directly.

**Requirements:** Python 3.6+ · standard library only (`collections`, which
ships with Python)

---

| Navigation | |
|---|---|
| **Repository hub** | [← Back to main README](../README.md) |
