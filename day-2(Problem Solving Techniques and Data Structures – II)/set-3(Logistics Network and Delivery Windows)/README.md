# Day 1 – Set 3: Logistics Network and Delivery Windows

## Overview

This Python assignment models a courier company's hub network and delivery planning using a Binary Search Tree, hash maps, graph traversal, sliding windows, and two pointers.

## Files

| File | Description |
|---|---|
| `source_code.py` | Complete Python implementation with all five tasks and test cases |
| `output_and_complexity.md` | Execution output, graph adjacency list, complexity table, algorithm explanations, and test coverage |

## Requirements

- Python 3.8 or later
- No third-party packages required

## Run

```bash
python source_code.py
```

## Tasks covered

1. **Hub-code BST:** Insert and search hub codes, calculate tree height, and demonstrate how sorted insertion creates a skewed tree.
2. **Parcel tracking hash map:** Look up parcel tracking numbers and detect repeated scans of the same parcel at the same hub.
3. **Hub route graph:** Represent ten hubs with an adjacency list, use BFS for a fewest-hop route, and DFS to list hubs reachable from the central depot.
4. **Delivery-window analysis:** Use a sliding window to find the four consecutive hours with the highest average parcel count.
5. **Route palindrome:** Use two pointers to check a route description while ignoring case and separators.

## Graph model

The sample graph contains ten hubs. Direct routes are modelled as bidirectional. The complete adjacency list and route results are documented in [`output_and_complexity.md`](output_and_complexity.md).

## Tests

The script runs assertions for empty inputs, duplicate insertions/scans, reachable paths, and palindrome/non-palindrome cases.

See [`output_and_complexity.md`](output_and_complexity.md) for detailed output and complexity analysis.
