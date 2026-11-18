# Day 1 – Set 1: E-Commerce Catalogue and Traffic Analysis

## Overview

This project demonstrates core data structures and algorithm patterns for an e-commerce platform:

1. Binary Search Tree (BST) operations and traversals for product categories.
2. Hash table with chaining for SKU lookup, including a collision example, compared with Python's built-in dictionary over 100,000 SKUs.
3. Microservice dependency graph with BFS and DFS topological ordering and circular-dependency detection.
4. Sliding-window calculation of the busiest continuous 3-hour request period.
5. Two-pointer search for order-value pairs matching a gift-card amount.

## Files

| File | Description |
|---|---|
| `set1.py` | Complete Python source code |
| `output_and_complexity.md` | Execution output, decision table, complexity analysis, and assumptions |

## Requirements

- Python 3.8 or later
- No third-party packages required

## Run

Open a terminal in this folder and execute:

```bash
python set1.py
```

The program prints the output for all five tasks. SKU lookup timings are measured during execution and may vary between runs and machines.

## Complexity summary

- BST operations: average `O(log n)`, worst-case `O(n)`; traversals `O(n)`.
- Chained hash lookup and Python dictionary lookup: average `O(1)`, worst-case `O(n)` under heavy collisions.
- BFS/DFS graph processing: `O(V + E)`.
- Sliding window: `O(h)`.
- Two-pointer pair search: `O(p)` plus the space needed for returned pairs.

See [`output_and_complexity.md`](output_and_complexity.md) for the full decision table and analysis.
