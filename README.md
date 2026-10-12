# Artificial-Class-Lab

> Course repository — *Introduction to AI and Its Application Using Python*

Hands-on Python work from the course, organized as **one folder per lab**.
Each lab folder is self-contained: a `README.md` (explanation), the official
manual where available, and the runnable scripts for that lab.

---

## Repository Layout

```
Artificial-Class-Lab/
│
├── README.md                 ← You are here (navigation hub)
│
├── Lab1/                     ← Lab 1: Python Fundamentals
│   ├── README.md             ← Explanation → links to manual + all scripts
│   ├── manual.md             ← Lab 1 manual
│   └── 01_python_syntax.py … 11_common_in_two_arrays.py
│
├── Lab2/                     ← Lab 2: Loops, Functions & Classes
│   ├── README.md             ← Explanation → links to all scripts
│   └── 01_while_loop.py … 13_object_methods.py
│
├── Lab3/                     ← Lab 3: Problem-Solving with Python
│   ├── README.md             ← Explanation → links to manual + all scripts
│   ├── Lab 3.pdf             ← Lab 3 manual
│   └── q1.py … q14_2.py
│
├── Lab4/                     ← Lab 4: Data Structures & Algorithms
│   ├── README.md             ← Explanation → links to all scripts
│   └── task1.py … task3.py
│
└── Lab5/                     ← Lab 5: Graphs, Trees & BFS
    ├── README.md             ← Explanation → links to all scripts
    └── task1.py … task3.py
```

---

## Labs Index

| Lab | Topics | Explanation | Manual | Status |
|-----|--------|-------------|--------|--------|
| **Lab 1** | Python syntax, input/output, data types, strings, lists, conditionals | [Read](Lab1/README.md) | [View](Lab1/manual.md) | Complete |
| **Lab 2** | `while`/`for` loops, `break`/`continue`, functions, classes & objects | [Read](Lab2/README.md) | — | Complete |
| **Lab 3** | Nested loops, data structures, strings, `random`, regex, 2D arrays | [Read](Lab3/README.md) | [View](Lab3/Lab%203.pdf) | Complete |
| **Lab 4** | Stacks, queues, binary search — implemented with classes & objects | [Read](Lab4/README.md) | — | Complete |
| **Lab 5** | Graphs, trees, breadth-first search, priority queue (min-heap) | [Read](Lab5/README.md) | — | Complete |

> **Pattern:** Every lab folder follows the same structure — a `README.md`
> (explanation), the manual where available, and the lab's scripts.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Zaidx-me/Artificial-Class-Lab.git
cd Artificial-Class-Lab
```

### 2. Run any lab script

```bash
cd Lab1
python3 01_python_syntax.py
python3 07_lists.py
# ... etc
```

> **Note:** Many scripts (input/output and most Lab 3–5 tasks) require
> interactive input when run. See each lab's `README.md` for details.

### 3. Requirements

- **Python 3.6+** (scripts use f-strings)
- **No external packages** — Python standard library only

---

## Repository Conventions

- Each lab folder is self-contained: **explanation** + **manual** + **scripts**
- Scripts are numbered (`NN_topic.py`) to reflect the order topics are introduced
- Code follows the **PEP 8** conventions taught in Lab 1 (4-space indentation, 79-char lines)
- Python artifacts and agent metadata are excluded via `.gitignore`
