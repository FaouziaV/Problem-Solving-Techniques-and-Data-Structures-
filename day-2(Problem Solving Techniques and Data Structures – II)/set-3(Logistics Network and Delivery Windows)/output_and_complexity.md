# Execution Output and Complexity Analysis

## Actual execution output

Captured by running the included `source_code.py` source code.

```text
DAY 1 - SET 3: LOGISTICS NETWORK AND DELIVERY WINDOWS

TASK 1: HUB CODE BINARY SEARCH TREE
Insertion order: ['HUB-M', 'HUB-F', 'HUB-T', 'HUB-B', 'HUB-J', 'HUB-P', 'HUB-W', 'HUB-A', 'HUB-D', 'HUB-H']
Inorder traversal: ['HUB-A', 'HUB-B', 'HUB-D', 'HUB-F', 'HUB-H', 'HUB-J', 'HUB-M', 'HUB-P', 'HUB-T', 'HUB-W']
Tree height (edges): 3
Search HUB-P: Found
Search HUB-Z: Not found
Height after sorted insertion: 9
Effect of sorted input: the BST becomes skewed like a linked list; height can reach n-1.

TASK 2: PARCEL TRACKING HASH MAP AND DUPLICATE SCANS
Tracking lookup TRK-1002: {'tracking_number': 'TRK-1002', 'destination': 'South'}
Duplicate scans (tracking number, hub): [('TRK-1001', 'HUB-M'), ('TRK-1002', 'HUB-F')]

TASK 3: HUB ROUTE GRAPH
Adjacency list:
  HUB-M: ['HUB-F', 'HUB-T']
  HUB-F: ['HUB-M', 'HUB-B', 'HUB-J']
  HUB-T: ['HUB-M', 'HUB-P', 'HUB-W']
  HUB-B: ['HUB-F', 'HUB-A']
  HUB-J: ['HUB-F', 'HUB-D']
  HUB-P: ['HUB-T', 'HUB-H']
  HUB-W: ['HUB-T', 'HUB-H']
  HUB-A: ['HUB-B']
  HUB-D: ['HUB-J']
  HUB-H: ['HUB-P', 'HUB-W']
Fewest-hop route HUB-M -> HUB-H: ['HUB-M', 'HUB-T', 'HUB-P', 'HUB-H']
Hubs reachable from central depot HUB-M (DFS): ['HUB-M', 'HUB-F', 'HUB-B', 'HUB-A', 'HUB-J', 'HUB-D', 'HUB-T', 'HUB-P', 'HUB-H', 'HUB-W']

TASK 4: HIGHEST-AVERAGE 4-HOUR WINDOW
Hourly parcel counts: [40, 55, 60, 70, 85, 100, 120, 150, 180, 160, 140, 130, 110, 95, 90, 80, 75, 70, 65, 60, 55, 50, 45, 40]
Best window: 07:00 to 11:00
Parcels in window: 630
Highest average per hour: 157.50

TASK 5: PALINDROME DELIVERY ROUTE
Route description: HUB-A / HUB-B / HUB-C / HUB-B / HUB-A
Normalized route: ['hub-a', 'hub-b', 'hub-c', 'hub-b', 'hub-a']
Is palindrome: True

TEST CASES
PASS: BST empty tree, search, and duplicate insertion
PASS: Hash lookup empty input and repeated same-hub scan
PASS: Graph empty input, BFS route, and DFS reachability
PASS: Sliding window empty/short input and exact-size window
PASS: Palindrome empty route, separators, and non-palindrome
```

## Hub network adjacency list / diagram

The ten hubs and direct, bidirectional routes used by the program are:

```text
HUB-M: HUB-F, HUB-T
HUB-F: HUB-M, HUB-B, HUB-J
HUB-T: HUB-M, HUB-P, HUB-W
HUB-B: HUB-F, HUB-A
HUB-J: HUB-F, HUB-D
HUB-P: HUB-T, HUB-H
HUB-W: HUB-T, HUB-H
HUB-A: HUB-B
HUB-D: HUB-J
HUB-H: HUB-P, HUB-W
```

The adjacency list is the exact graph representation used by BFS and DFS.

## Algorithm choice and complexity table

Let `n` be the number of hub codes, `p` the number of parcels, `s` the number of scan events, `V` the number of hubs, `E` the number of direct routes, `h` the number of hourly counts, and `r` the number of hub codes in a route description.

| Task | Algorithm / data structure | Time complexity | Space complexity |
|---|---|---:|---:|
| Hub insert and search | Binary Search Tree | Average `O(log n)`; worst `O(n)` | `O(n)` for tree; search `O(1)` auxiliary |
| BST height | Recursive tree traversal | `O(n)` | `O(h_tree)` recursion |
| Tracking-number lookup | Hash map / Python dictionary | Average `O(1)` lookup; worst `O(p)` | `O(p)` |
| Duplicate scans at same hub | Hash set of `(tracking_number, hub_code)` | Average `O(s)` total; worst `O(s²)` under pathological hashing | `O(s)` |
| Fewest-hop route | BFS on adjacency list | `O(V + E)` | `O(V)` |
| Reachable hubs | DFS on adjacency list | `O(V + E)` | `O(V)` |
| Highest-average 4-hour window | Sliding window | `O(h)` | `O(1)` |
| Route palindrome | Two pointers over hub-code tokens | `O(r)` | `O(r)` for normalized tokens |

## Short explanations

1. **BST:** The tree supports ordered hub-code insertion and search. Its height is the longest root-to-leaf path measured in edges. Inserting sorted codes makes each new node extend one side, producing a skewed tree with height `n - 1`; operations then degrade to `O(n)`. A balanced BST would avoid this worst-case shape.
2. **Hash map:** A dictionary maps each tracking number to parcel details. Duplicate scans are detected by storing the pair `(tracking_number, hub_code)` in a set. The same parcel scanned at a different hub is not counted as a duplicate at the same hub.
3. **Graph:** The adjacency list stores each hub's direct neighbours. The sample routes are treated as bidirectional. BFS explores by hop distance, so the first path found to a destination has the fewest edges. DFS visits every hub reachable from the central depot.
4. **Sliding window:** The algorithm maintains a rolling sum of four adjacent hourly counts. It adds the next hour and removes the hour leaving the window; since every window has four hours, the highest sum also has the highest average.
5. **Two pointers:** The route description is split into hub-code tokens, with case normalized and separators ignored. Pointers compare tokens from both ends and move inward. This checks whether the sequence of hub codes is a palindrome, rather than whether the individual characters happen to form one.

## Test coverage

The source includes assertions for:
- Empty BST, missing search result, and duplicate hub insertion.
- Empty tracking lookup and scan list, plus repeated scans at the same hub.
- Empty graph, BFS route, and DFS reachability.
- Empty/too-short hourly data and a window exactly equal to the requested size.
- Empty route, a palindrome with separators, and a non-palindrome.
