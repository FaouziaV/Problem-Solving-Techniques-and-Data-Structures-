# Day 1 – Data Structures and Algorithms Assignments

This repository contains three Python assignments based on practical business scenarios. Each set demonstrates data structures and algorithmic patterns, with a focus on implementation, complexity, and practical use.

## Set 1 – E-Commerce Catalogue and Traffic Analysis

### Overview

This project demonstrates core data structures and algorithm patterns for an e-commerce platform:

1. Binary Search Tree (BST) operations and traversals for product categories.
2. Hash table with chaining for SKU lookup, including a collision example, compared with Python's built-in dictionary over 100,000 SKUs.
3. Microservice dependency graph with BFS and DFS topological ordering and circular-dependency detection.
4. Sliding-window calculation of the busiest continuous 3-hour request period.
5. Two-pointer search for order-value pairs matching a gift-card amount.

### Files

| File | Description |
|---|---|
| `source_code.py` | Complete Python source code |
| `output_and_complexity.md` | Execution output, decision table, complexity analysis, and assumptions |

### Run

```bash
python source_code.py
```

The program prints the output for all five tasks. SKU lookup timings are measured during execution and may vary between runs and machines.

### Complexity summary

- BST operations: average `O(log n)`, worst-case `O(n)`; traversals `O(n)`.
- Chained hash lookup and Python dictionary lookup: average `O(1)`, worst-case `O(n)` under heavy collisions.
- BFS/DFS graph processing: `O(V + E)`.
- Sliding window: `O(h)`.
- Two-pointer pair search: `O(p)` plus the space needed for returned pairs.

---

## Set 2 – Insurance Claims Processing

### Overview

A Python implementation of common data structures and algorithms for an insurance claims workflow. It covers claim indexing, duplicate submission detection, approval-stage routing, claim-volume monitoring, and merging regional claim lists.

### Tasks

1. **Claim ID BST:** Insert and search claim IDs; print inorder, preorder, and postorder traversals. Inorder gives sorted claim IDs.
2. **Duplicate detection:** Normalize policy numbers for case and whitespace, then hash the policy/date pair to group duplicate submissions.
3. **Approval graph:** Use BFS to find a shortest path between approval stages and DFS to detect directed cycles.
4. **Claim spike monitoring:** Scan daily claim counts to find the longest consecutive run above 100 claims.
5. **Regional merge:** Merge two already-sorted regional lists using two pointers, preserving duplicate values.

### Files

| File | Description |
|---|---|
| `source_code.py` | Complete working Python source code, including test cases |
| `output_and_complexity.md` | Actual output, complexity table, design decisions, assumptions, and test coverage |

### Run

```bash
python source_code.py
```


The script runs all five demonstrations and then executes assertions covering empty inputs and duplicates.

---

## Set 3 – Logistics Network and Delivery Windows

### Overview

This Python assignment models a courier company's hub network and delivery planning using a Binary Search Tree, hash maps, graph traversal, sliding windows, and two pointers.

### Tasks covered

1. **Hub-code BST:** Insert and search hub codes, calculate tree height, and demonstrate how sorted insertion creates a skewed tree.
2. **Parcel tracking hash map:** Look up parcel tracking numbers and detect repeated scans of the same parcel at the same hub.
3. **Hub route graph:** Represent ten hubs with an adjacency list, use BFS for a fewest-hop route, and DFS to list hubs reachable from the central depot.
4. **Delivery-window analysis:** Use a sliding window to find the four consecutive hours with the highest average parcel count.
5. **Route palindrome:** Use two pointers to check a route description while ignoring case and separators.

### Files

| File | Description |
|---|---|
| `source_code.py` | Complete Python implementation with all five tasks and test cases |
| `output_and_complexity.md` | Execution output, graph adjacency list, complexity table, algorithm explanations, and test coverage |

### Graph model

The sample graph contains ten hubs. Direct routes are modelled as bidirectional. The complete adjacency list and route results are documented in the Set 3 `output_and_complexity.md` file.

### Tests

The script runs assertions for empty inputs, duplicate insertions/scans, reachable paths, and palindrome/non-palindrome cases.

### Run

```bash
python source_code.py
```

## Requirements and execution

- Python 3.8 or later
- No third-party packages are required for these assignments.
- Run each Python script from the folder containing that script and its required input files.
- For Set 1, keep `orders.csv` in the same folder as `source_code.py` if using the version that reads the CSV dataset.
- Refer to each set's `output_and_complexity.md` for its execution output and detailed complexity analysis.
- Runtime measurements may vary depending on the machine and system load.

## Suggested repository structure

```text
Day-3/
├── README.md
├── Set-1-E-Commerce/
│   ├── source_code.py
│   └── output_and_complexity.md
├── Set-2-Insurance-Claims/
│   ├── source_code.py
│   └── output_and_complexity.md
└── Set-3-Logistics-Network/
    ├── source_code.py
    └── output_and_complexity.md
```
