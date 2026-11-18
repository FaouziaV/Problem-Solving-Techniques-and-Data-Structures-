# Day 1 – Set 2: Insurance Claims Processing

## Overview

A Python implementation of common data structures and algorithms for an insurance claims workflow. It covers claim indexing, duplicate submission detection, approval-stage routing, claim-volume monitoring, and merging regional claim lists.

## Files

| File | Description |
|---|---|
| `source_code.py` | Complete working Python source code, including test cases |
| `output_and_complexity.md` | Actual output, complexity table, design decisions, assumptions, and test coverage |

## Requirements

- Python 3.8 or later
- No third-party packages required

## Run

```bash
python source_code.py
```

The script runs all five demonstrations and then executes assertions covering empty inputs and duplicates.

## Tasks

1. **Claim ID BST:** Insert and search claim IDs; print inorder, preorder, and postorder traversals. Inorder gives sorted claim IDs.
2. **Duplicate detection:** Normalize policy numbers for case and whitespace, then hash the policy/date pair to group duplicate submissions.
3. **Approval graph:** Use BFS to find a shortest path between approval stages and DFS to detect directed cycles.
4. **Claim spike monitoring:** Scan daily claim counts to find the longest consecutive run above 100 claims.
5. **Regional merge:** Merge two already-sorted regional lists using two pointers, preserving duplicate values.

See [`output_and_complexity.md`](output_and_complexity.md) for the complexity table and detailed notes.
