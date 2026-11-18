# Execution Output and Complexity Analysis

## Actual execution output

The following output was captured by running the included `set2.py` file.

```text
DAY 1 - SET 2: INSURANCE CLAIMS PROCESSING

TASK 1: CLAIM ID BINARY SEARCH TREE
Claim IDs inserted: 15
Inorder: [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]
Preorder: [105, 102, 101, 100, 104, 103, 108, 107, 106, 110, 109, 112, 111, 113, 114]
Postorder: [100, 101, 103, 104, 102, 106, 107, 109, 111, 114, 113, 112, 110, 108, 105]
Search claim 107: Found
Search claim 999: Not found
Sorted traversal: Inorder (left, root, right)

TASK 2: HASH-BASED DUPLICATE CLAIM DETECTION
Normalized key ('pol7788', '2026-03-12'): duplicate claim IDs ['CLM-201', 'CLM-202', 'CLM-204']
Collision handling: hash maps compare keys within collision buckets; unequal keys remain separate.

TASK 3: CLAIM APPROVAL GRAPH
Shortest path registration -> settlement: ['registration', 'assessment', 'settlement']
Cycle detected in approval graph: False
Cycle detected after adding settlement -> assessment: True

TASK 4: LONGEST RUN WITH MORE THAN 100 CLAIMS
Daily claim counts: [80, 120, 135, 110, 95, 140, 155, 160, 90, 105, 115, 125, 70, 130]
Longest qualifying run: day 2 to day 4 (3 consecutive days)

TASK 5: MERGE TWO REGIONAL CLAIM LISTS
North region: [101, 104, 108, 115, 120]
South region: [102, 104, 109, 112, 121]
Merged sorted claims: [101, 102, 104, 104, 108, 109, 112, 115, 120, 121]

TEST CASES
PASS: BST empty input, search, and duplicate insertion
PASS: Hashing empty input and case/space-normalized duplicate claims
PASS: Graph shortest path and DFS cycle detection
PASS: Sliding-window empty input and consecutive-day run
PASS: Two-pointer merge empty lists and duplicate values
```

## Complexity table

Let `n` be the number of claim IDs, `c` the number of claim records, `V` the number of approval stages, `E` the number of graph edges, `d` the number of days, and `a`, `b` the sizes of the two regional lists.

| Task / operation | Data structure or pattern | Time complexity | Space complexity |
|---|---|---:|---:|
| BST insertion | Binary Search Tree | Average `O(log n)` per insert; worst `O(n)` | `O(n)` |
| BST search | Binary Search Tree | Average `O(log n)`; worst `O(n)` | `O(1)` iterative |
| BST traversals | Inorder, preorder, postorder DFS | `O(n)` | `O(h)` recursion stack, where `h` is tree height |
| Duplicate claim detection | Hash map / dictionary with normalized composite key | Average `O(c)` total; worst `O(c²)` under severe collisions | `O(c)` |
| Shortest approval path | BFS on directed graph | `O(V + E)` | `O(V)` |
| Loop detection | DFS with three-state visitation | `O(V + E)` | `O(V)` |
| Longest run above threshold | One-pass moving window / streak scan | `O(d)` | `O(1)` |
| Merge regional sorted lists | Two pointers | `O(a + b)` | `O(a + b)` for the returned merged list |

## Decision notes

- **BST:** Inorder traversal (left, root, right) returns claim IDs in ascending order for this binary search tree. The tree is not self-balancing, so sorted or unfavourable insertion orders can produce linear-height trees.
- **Hashing:** Policy numbers are normalized by removing whitespace and applying `casefold()`. The incident date is trimmed and included in the key. Hash collisions are resolved by the dictionary's internal collision-handling mechanism: keys are compared for equality, so different keys that share a hash are not treated as duplicates.
- **Near-duplicate scope:** This implementation treats case and whitespace differences as equivalent. It does not remove punctuation (for example, `POL-123` remains different from `POL123`) and does not interpret different date formats as the same date.
- **Graph:** Directed edges represent allowed transitions. BFS returns a path with the fewest edges. DFS detects a back edge to a node currently being explored, which indicates a directed cycle.
- **Longest run:** The scan extends the current contiguous run while each day's claim count is greater than 100, and resets it when a day does not qualify. Day indices shown in the output are one-based for readability.
- **Merge:** The inputs must already be sorted in ascending order. The merge preserves duplicate claim IDs/values and does not perform another sorting pass.

## Test coverage

The program includes assertions for:
- Empty BST and missing-key search.
- Duplicate BST insertion (the duplicate ID is ignored).
- Empty claim list and duplicate policy/date keys with case and whitespace differences.
- Empty graph, shortest path, acyclic graph, and cyclic graph.
- Empty daily-count input, no qualifying days, and a qualifying consecutive run.
- Empty regional lists, one empty regional list, and duplicate values across lists.
