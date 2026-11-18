# Execution Output and Complexity Analysis

## Execution output

The following output was produced by running the included `set1.py` source code.

```text
DAY 1 - SET 1: E-COMMERCE CATALOGUE AND TRAFFIC ANALYSIS

TASK 1: BINARY SEARCH TREE
Categories inserted: 15
Inorder: ['Accessories', 'Beauty', 'Books', 'Electronics', 'Fashion', 'Footwear', 'Furniture', 'Grocery', 'Home', 'Kitchen', 'Laptops', 'Mobiles', 'Sports', 'Toys', 'Watches']
Preorder: ['Electronics', 'Books', 'Beauty', 'Accessories', 'Fashion', 'Home', 'Grocery', 'Furniture', 'Footwear', 'Sports', 'Mobiles', 'Laptops', 'Kitchen', 'Toys', 'Watches']
Postorder: ['Accessories', 'Beauty', 'Books', 'Footwear', 'Furniture', 'Grocery', 'Kitchen', 'Laptops', 'Mobiles', 'Watches', 'Toys', 'Sports', 'Home', 'Fashion', 'Electronics']
Search 'Mobiles': Found
Search 'Automotive': Not found

TASK 2: SKU HASH TABLE VS BUILT-IN DICTIONARY
Collision demonstration:
SKU-101 and SKU-110 bucket index: 4
Bucket contents: [('SKU-101', 'Wireless Mouse'), ('SKU-110', 'USB-C Cable')]
Chained lookup SKU-110: USB-C Cable
SKUs loaded for benchmark: 100000
Target SKU: SKU-099999
Chained hash table result: Product-99999
Chained hash table lookup time: 0.000004366 seconds
Built-in dictionary result: Product-99999
Built-in dictionary lookup time: 0.000002704 seconds

TASK 3: MICROSERVICE DEPENDENCY GRAPH
BFS topological deployment order: ['checkout', 'cart', 'payment', 'pricing', 'inventory', 'notification']
DFS topological deployment order: ['checkout', 'payment', 'cart', 'pricing', 'inventory', 'notification']
Circular dependency detected (BFS): True
Circular dependency detected (DFS): True

TASK 4: BUSIEST CONTINUOUS 3-HOUR WINDOW
Hourly requests: [120, 100, 90, 80, 110, 150, 220, 300, 450, 520, 610, 580, 490, 400, 350, 320, 280, 260, 240, 210, 190, 170, 150, 130]
Busiest window: 09:00 to 12:00
Requests in busiest 3-hour window: 1710

TASK 5: GIFT-CARD PAIRS (TWO POINTERS)
Sorted order values: [10, 20, 30, 40, 50, 60, 70, 80, 90]
Gift-card value: 100
Matching pairs: [(10, 90), (20, 80), (30, 70), (40, 60)]
```



## Decision table

| Problem | Data structure / pattern | Reason for choosing it |
|---|---|---|
| Store and browse 15 product categories | Binary Search Tree (BST) | Keeps values ordered by key and supports insertion and search. Inorder traversal prints categories in sorted order; preorder and postorder show other traversal orders. |
| SKU lookup with collisions | Hash table with separate chaining | A bucket array provides direct access by hash index. A list in each bucket stores keys that map to the same index, resolving collisions without overwriting entries. |
| Compare SKU lookup implementations | Python dictionary | Python's built-in hash map is a practical baseline for average-case constant-time key lookup and avoids implementing bucket management manually. |
| Deployment dependencies and circular dependency detection | Directed graph; BFS/Kahn and DFS topological sort | Edges represent prerequisite relationships. A topological order is valid when all nodes can be processed; if not all nodes are emitted, a cycle exists. |
| Busiest continuous 3-hour traffic window | Sliding window | Reuses the previous window sum by adding the incoming hour and removing the outgoing hour, avoiding repeated summation. |
| Gift-card combinations in sorted order values | Two pointers | Moves the left or right pointer according to whether the current sum is below or above the target, scanning the sorted list once. |

## Time and space complexity

Let `n` be the number of categories, `m` the number of SKUs, `V` the number of services, `E` the number of dependency edges, `h` the number of hourly traffic entries, and `p` the number of order values.

| Operation | Time complexity | Auxiliary space |
|---|---:|---:|
| BST insert / search | Average `O(log n)`; worst `O(n)` | `O(n)` for the tree |
| BST inorder / preorder / postorder | `O(n)` | `O(h_tree)` recursion stack; output `O(n)` |
| Chained hash insert / lookup | Average `O(1)`; worst `O(m)` | `O(m + capacity)` |
| Built-in dictionary lookup | Average `O(1)`; worst-case can degrade with collisions | `O(m)` for the dictionary |
| Build SKU datasets | `O(m)` average | `O(m)` |
| BFS topological sort / cycle detection | `O(V + E)` | `O(V)` |
| DFS topological sort / cycle detection | `O(V + E)` | `O(V)` including recursion |
| Sliding window | `O(h)` | `O(1)` |
| Two-pointer pair search | `O(p)` | `O(k)` for `k` returned pairs |

## Notes and assumptions

- The BST ignores duplicate category names. Its performance depends on tree shape; this implementation does not self-balance.
- The chained hash table uses a simple deterministic character-sum hash so the sample collision is easy to reproduce. It is for demonstrating chaining, not for production SKU hashing.
- The 100,000-SKU benchmark reports one lookup measurement per implementation. A rigorous performance study would repeat lookups and report a median or average.
- The dependency edges mean “source service must be deployed before destination service.” Both BFS and DFS may return different valid orders.
- The 24 input values represent requests per hour. The 3-hour window is a continuous group of three adjacent hourly buckets.
- The two-pointer method assumes the order values are already sorted in ascending order. It returns distinct value pairs and advances both pointers after a match.
