from collections import deque
from time import perf_counter

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class CategoryBST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BSTNode(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = BSTNode(value)
                    return
                current = current.right
            else:
                return 

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def inorder(self):
        result = []

        def visit(node):
            if node:
                visit(node.left)
                result.append(node.value)
                visit(node.right)

        visit(self.root)
        return result

    def preorder(self):
        result = []

        def visit(node):
            if node:
                result.append(node.value)
                visit(node.left)
                visit(node.right)

        visit(self.root)
        return result

    def postorder(self):
        result = []

        def visit(node):
            if node:
                visit(node.left)
                visit(node.right)
                result.append(node.value)

        visit(self.root)
        return result

class ChainedHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _index(self, key):
        return sum(ord(char) for char in str(key)) % self.capacity

    def insert(self, key, value):
        index = self._index(key)
        bucket = self.buckets[index]
        for position, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[position] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._index(key)
        for stored_key, value in self.buckets[index]:
            if stored_key == key:
                return value
        return None

def build_graph(edges):
    graph = {}
    for source, destination in edges:
        graph.setdefault(source, [])
        graph.setdefault(destination, [])
        graph[source].append(destination)
    return graph


def bfs_order(graph):
    indegree = {node: 0 for node in graph}
    for neighbours in graph.values():
        for neighbour in neighbours:
            indegree[neighbour] += 1

    queue = deque(node for node in graph if indegree[node] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    return order if len(order) == len(graph) else None


def dfs_order(graph):
    state = {node: 0 for node in graph} 
    order = []

    def visit(node):
        if state[node] == 1:
            return False
        if state[node] == 2:
            return True

        state[node] = 1
        for neighbour in graph[node]:
            if not visit(neighbour):
                return False
        state[node] = 2
        order.append(node)
        return True

    for node in graph:
        if state[node] == 0 and not visit(node):
            return None

    order.reverse()
    return order


def busiest_three_hour_window(requests_per_hour):
    if len(requests_per_hour) < 3:
        raise ValueError("At least 3 hourly request counts are required.")

    current_sum = sum(requests_per_hour[:3])
    maximum_sum = current_sum
    start_index = 0

    for end_index in range(3, len(requests_per_hour)):
        current_sum += requests_per_hour[end_index]
        current_sum -= requests_per_hour[end_index - 3]
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            start_index = end_index - 2

    return start_index, start_index + 2, maximum_sum


def gift_card_pairs(sorted_order_values, gift_card_value):
    left = 0
    right = len(sorted_order_values) - 1
    pairs = []

    while left < right:
        total = sorted_order_values[left] + sorted_order_values[right]
        if total == gift_card_value:
            pairs.append((sorted_order_values[left], sorted_order_values[right]))
            left += 1
            right -= 1
        elif total < gift_card_value:
            left += 1
        else:
            right -= 1

    return pairs



print("DAY 1 - SET 1: E-COMMERCE CATALOGUE AND TRAFFIC ANALYSIS")

print("\nTASK 1: BINARY SEARCH TREE")
categories = [
    "Electronics", "Books", "Fashion", "Home", "Beauty",
    "Sports", "Toys", "Grocery", "Furniture", "Footwear",
    "Mobiles", "Laptops", "Kitchen", "Watches", "Accessories"
]
bst = CategoryBST()
for category in categories:
    bst.insert(category)

print("Categories inserted:", len(categories))
print("Inorder:", bst.inorder())
print("Preorder:", bst.preorder())
print("Postorder:", bst.postorder())
print("Search 'Mobiles':", "Found" if bst.search("Mobiles") else "Not found")
print("Search 'Automotive':", "Found" if bst.search("Automotive") else "Not found")

print("\nTASK 2: SKU HASH TABLE VS BUILT-IN DICTIONARY")
chained = ChainedHashTable(capacity=10)
chained.insert("SKU-101", "Wireless Mouse")
chained.insert("SKU-110", "USB-C Cable")  
collision_index = chained._index("SKU-101")
print("Collision demonstration:")
print(f"SKU-101 and SKU-110 bucket index: {collision_index}")
print("Bucket contents:", chained.buckets[collision_index])
print("Chained lookup SKU-110:", chained.get("SKU-110"))

sku_count = 100_000
sku_records = {f"SKU-{i:06d}": f"Product-{i}" for i in range(sku_count)}
custom_table = ChainedHashTable(capacity=200_003)
for sku, product in sku_records.items():
    custom_table.insert(sku, product)

target_sku = "SKU-099999"
start = perf_counter()
custom_result = custom_table.get(target_sku)
custom_time = perf_counter() - start

start = perf_counter()
builtin_result = sku_records.get(target_sku)
builtin_time = perf_counter() - start

print(f"SKUs loaded for benchmark: {sku_count}")
print(f"Target SKU: {target_sku}")
print("Chained hash table result:", custom_result)
print(f"Chained hash table lookup time: {custom_time:.9f} seconds")
print("Built-in dictionary result:", builtin_result)
print(f"Built-in dictionary lookup time: {builtin_time:.9f} seconds")

print("\nTASK 3: MICROSERVICE DEPENDENCY GRAPH")
deployment_edges = [
    ("cart", "pricing"),
    ("pricing", "inventory"),
    ("checkout", "cart"),
    ("checkout", "payment"),
    ("payment", "notification"),
    ("inventory", "notification")
]
graph = build_graph(deployment_edges)
print("BFS topological deployment order:", bfs_order(graph))
print("DFS topological deployment order:", dfs_order(graph))

circular_graph = build_graph([
    ("cart", "pricing"),
    ("pricing", "inventory"),
    ("inventory", "cart")
])
print("Circular dependency detected (BFS):", bfs_order(circular_graph) is None)
print("Circular dependency detected (DFS):", dfs_order(circular_graph) is None)

print("\nTASK 4: BUSIEST CONTINUOUS 3-HOUR WINDOW")
hourly_requests = [
    120, 100, 90, 80, 110, 150, 220, 300,
    450, 520, 610, 580, 490, 400, 350, 320,
    280, 260, 240, 210, 190, 170, 150, 130
]
start_hour, end_hour, request_total = busiest_three_hour_window(hourly_requests)
print("Hourly requests:", hourly_requests)
print(f"Busiest window: {start_hour:02d}:00 to {end_hour + 1:02d}:00")
print("Requests in busiest 3-hour window:", request_total)

print("\nTASK 5: GIFT-CARD PAIRS (TWO POINTERS)")
order_values = [10, 20, 30, 40, 50, 60, 70, 80, 90]
gift_card_value = 100
print("Sorted order values:", order_values)
print("Gift-card value:", gift_card_value)
print("Matching pairs:", gift_card_pairs(order_values, gift_card_value))

