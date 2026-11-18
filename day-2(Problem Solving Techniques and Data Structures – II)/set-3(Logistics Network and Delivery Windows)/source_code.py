from collections import deque

class HubNode:
    def __init__(self, code):
        self.code = code
        self.left = None
        self.right = None


class HubBST:
    def __init__(self):
        self.root = None

    def insert(self, code):
        if self.root is None:
            self.root = HubNode(code)
            return

        current = self.root
        while True:
            if code < current.code:
                if current.left is None:
                    current.left = HubNode(code)
                    return
                current = current.left
            elif code > current.code:
                if current.right is None:
                    current.right = HubNode(code)
                    return
                current = current.right
            else:
                return 

    def search(self, code):
        current = self.root
        while current:
            if code == current.code:
                return True
            current = current.left if code < current.code else current.right
        return False

    def height(self):
        def measure(node):
            if node is None:
                return -1
            return 1 + max(measure(node.left), measure(node.right))
        return measure(self.root)

    def inorder(self):
        result = []

        def visit(node):
            if node:
                visit(node.left)
                result.append(node.code)
                visit(node.right)

        visit(self.root)
        return result

def build_tracking_lookup(parcels):
    return {parcel["tracking_number"]: parcel for parcel in parcels}


def find_duplicate_scans(scan_events):
    seen = set()
    duplicates = set()

    for event in scan_events:
        key = (event["tracking_number"], event["hub_code"])
        if key in seen:
            duplicates.add(key)
        else:
            seen.add(key)

    return sorted(duplicates)


def build_adjacency_list(hubs, routes):
    graph = {hub: [] for hub in hubs}
    for start, end in routes:
        graph[start].append(end)
        graph[end].append(start)  
    return graph


def shortest_route_bfs(graph, start, destination):
    if start not in graph or destination not in graph:
        return None

    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == destination:
            return path

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    return None


def reachable_hubs_dfs(graph, start):
    if start not in graph:
        return []

    visited = set()
    order = []

    def visit(hub):
        visited.add(hub)
        order.append(hub)
        for neighbour in graph[hub]:
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return order


def highest_average_window(parcel_counts, window_size=4):
    if window_size <= 0:
        raise ValueError("Window size must be positive.")
    if len(parcel_counts) < window_size:
        return None

    current_sum = sum(parcel_counts[:window_size])
    best_sum = current_sum
    best_start = 0

    for end in range(window_size, len(parcel_counts)):
        current_sum += parcel_counts[end]
        current_sum -= parcel_counts[end - window_size]
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = end - window_size + 1

    average = best_sum / window_size
    return best_start, best_start + window_size - 1, best_sum, average


def normalize_route(route_description):
    return [token.casefold() for token in route_description.replace(",", " ").replace("/", " ").split()]


def is_route_palindrome(route_description):
    hub_codes = normalize_route(route_description)
    left = 0
    right = len(hub_codes) - 1

    while left < right:
        if hub_codes[left] != hub_codes[right]:
            return False
        left += 1
        right -= 1

    return True


def run_tests():
    print("\nTEST CASES")

    empty_bst = HubBST()
    assert empty_bst.height() == -1
    assert empty_bst.search("HUB-A") is False
    assert empty_bst.inorder() == []

    test_bst = HubBST()
    for code in ["HUB-B", "HUB-A", "HUB-C", "HUB-A"]:
        test_bst.insert(code)
    assert test_bst.inorder() == ["HUB-A", "HUB-B", "HUB-C"]
    print("PASS: BST empty tree, search, and duplicate insertion")

    assert build_tracking_lookup([]) == {}
    assert find_duplicate_scans([]) == []
    scan_test = [
        {"tracking_number": "TRK-1", "hub_code": "HUB-A"},
        {"tracking_number": "TRK-1", "hub_code": "HUB-B"},
        {"tracking_number": "TRK-1", "hub_code": "HUB-A"},
    ]
    assert find_duplicate_scans(scan_test) == [("TRK-1", "HUB-A")]
    print("PASS: Hash lookup empty input and repeated same-hub scan")

    assert shortest_route_bfs({}, "HUB-A", "HUB-B") is None
    assert reachable_hubs_dfs({}, "HUB-A") == []
    small_graph = build_adjacency_list(["A", "B", "C"], [("A", "B"), ("B", "C")])
    assert shortest_route_bfs(small_graph, "A", "C") == ["A", "B", "C"]
    assert reachable_hubs_dfs(small_graph, "A") == ["A", "B", "C"]
    print("PASS: Graph empty input, BFS route, and DFS reachability")

    assert highest_average_window([], 4) is None
    assert highest_average_window([1, 2, 3], 4) is None
    assert highest_average_window([5, 5, 5, 5], 4) == (0, 3, 20, 5.0)
    print("PASS: Sliding window empty/short input and exact-size window")

    assert is_route_palindrome("")
    assert is_route_palindrome("HUB-A / HUB-B / HUB-A")
    assert not is_route_palindrome("HUB-A / HUB-B")
    print("PASS: Palindrome empty route, separators, and non-palindrome")


print("DAY 1 - SET 3: LOGISTICS NETWORK AND DELIVERY WINDOWS")

print("\nTASK 1: HUB CODE BINARY SEARCH TREE")
insertion_order = [
    "HUB-M", "HUB-F", "HUB-T", "HUB-B", "HUB-J",
    "HUB-P", "HUB-W", "HUB-A", "HUB-D", "HUB-H"
]
bst = HubBST()
for hub in insertion_order:
    bst.insert(hub)

print("Insertion order:", insertion_order)
print("Inorder traversal:", bst.inorder())
print("Tree height (edges):", bst.height())
print("Search HUB-P:", "Found" if bst.search("HUB-P") else "Not found")
print("Search HUB-Z:", "Found" if bst.search("HUB-Z") else "Not found")

sorted_bst = HubBST()
for hub in sorted(insertion_order):
    sorted_bst.insert(hub)
print("Height after sorted insertion:", sorted_bst.height())
print("Effect of sorted input: the BST becomes skewed like a linked list; height can reach n-1.")

print("\nTASK 2: PARCEL TRACKING HASH MAP AND DUPLICATE SCANS")
parcels = [
    {"tracking_number": "TRK-1001", "destination": "North"},
    {"tracking_number": "TRK-1002", "destination": "South"},
    {"tracking_number": "TRK-1003", "destination": "West"},
]
tracking_lookup = build_tracking_lookup(parcels)
print("Tracking lookup TRK-1002:", tracking_lookup.get("TRK-1002"))

scan_events = [
    {"tracking_number": "TRK-1001", "hub_code": "HUB-M"},
    {"tracking_number": "TRK-1002", "hub_code": "HUB-F"},
    {"tracking_number": "TRK-1001", "hub_code": "HUB-M"},
    {"tracking_number": "TRK-1001", "hub_code": "HUB-T"},
    {"tracking_number": "TRK-1003", "hub_code": "HUB-F"},
    {"tracking_number": "TRK-1002", "hub_code": "HUB-F"},
]
print("Duplicate scans (tracking number, hub):", find_duplicate_scans(scan_events))

print("\nTASK 3: HUB ROUTE GRAPH")
hubs = ["HUB-M", "HUB-F", "HUB-T", "HUB-B", "HUB-J",
        "HUB-P", "HUB-W", "HUB-A", "HUB-D", "HUB-H"]
routes = [
    ("HUB-M", "HUB-F"),
    ("HUB-M", "HUB-T"),
    ("HUB-F", "HUB-B"),
    ("HUB-F", "HUB-J"),
    ("HUB-T", "HUB-P"),
    ("HUB-T", "HUB-W"),
    ("HUB-B", "HUB-A"),
    ("HUB-J", "HUB-D"),
    ("HUB-P", "HUB-H"),
    ("HUB-W", "HUB-H"),
]
graph = build_adjacency_list(hubs, routes)
print("Adjacency list:")
for hub, neighbours in graph.items():
    print(f"  {hub}: {neighbours}")
print("Fewest-hop route HUB-M -> HUB-H:", shortest_route_bfs(graph, "HUB-M", "HUB-H"))
print("Hubs reachable from central depot HUB-M (DFS):", reachable_hubs_dfs(graph, "HUB-M"))

print("\nTASK 4: HIGHEST-AVERAGE 4-HOUR WINDOW")
hourly_counts = [40, 55, 60, 70, 85, 100, 120, 150, 180, 160, 140, 130,
                    110, 95, 90, 80, 75, 70, 65, 60, 55, 50, 45, 40]
result = highest_average_window(hourly_counts, 4)
start, end, total, average = result
print("Hourly parcel counts:", hourly_counts)
print(f"Best window: {start:02d}:00 to {end + 1:02d}:00")
print("Parcels in window:", total)
print(f"Highest average per hour: {average:.2f}")

print("\nTASK 5: PALINDROME DELIVERY ROUTE")
route = "HUB-A / HUB-B / HUB-C / HUB-B / HUB-A"
print("Route description:", route)
print("Normalized route:", normalize_route(route))
print("Is palindrome:", is_route_palindrome(route))

run_tests()


