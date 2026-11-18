from collections import deque

class BSTNode:
    def __init__(self, claim_id):
        self.claim_id = claim_id
        self.left = None
        self.right = None


class ClaimBST:
    def __init__(self):
        self.root = None

    def insert(self, claim_id):
        if self.root is None:
            self.root = BSTNode(claim_id)
            return

        current = self.root
        while True:
            if claim_id < current.claim_id:
                if current.left is None:
                    current.left = BSTNode(claim_id)
                    return
                current = current.left
            elif claim_id > current.claim_id:
                if current.right is None:
                    current.right = BSTNode(claim_id)
                    return
                current = current.right
            else:
                return  

    def search(self, claim_id):
        current = self.root
        while current:
            if claim_id == current.claim_id:
                return True
            current = current.left if claim_id < current.claim_id else current.right
        return False

    def inorder(self):
        result = []

        def visit(node):
            if node:
                visit(node.left)
                result.append(node.claim_id)
                visit(node.right)

        visit(self.root)
        return result

    def preorder(self):
        result = []

        def visit(node):
            if node:
                result.append(node.claim_id)
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
                result.append(node.claim_id)

        visit(self.root)
        return result

def normalize_policy_number(policy_number):
    return "".join(str(policy_number).split()).casefold()


def claim_key(claim):
    return (
        normalize_policy_number(claim["policy_number"]),
        str(claim["incident_date"]).strip()
    )


def find_duplicate_claims(claims):
    claims_by_key = {}
    for claim in claims:
        key = claim_key(claim)
        claims_by_key.setdefault(key, []).append(claim["claim_id"])

    return {
        key: claim_ids
        for key, claim_ids in claims_by_key.items()
        if len(claim_ids) > 1
    }


def build_graph(edges):
    graph = {}
    for start, end in edges:
        graph.setdefault(start, [])
        graph.setdefault(end, [])
        graph[start].append(end)
    return graph


def shortest_path_bfs(graph, start, destination):
    if start not in graph or destination not in graph:
        return None

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()
        if node == destination:
            return path

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None


def has_cycle_dfs(graph):
    state = {node: 0 for node in graph}

    def visit(node):
        state[node] = 1
        for neighbour in graph[node]:
            if state[neighbour] == 1:
                return True
            if state[neighbour] == 0 and visit(neighbour):
                return True
        state[node] = 2
        return False

    for node in graph:
        if state[node] == 0 and visit(node):
            return True
    return False


def longest_high_claim_run(daily_claim_counts, threshold=100):
    best_start = None
    best_end = None
    best_length = 0

    current_start = None
    current_length = 0

    for index, count in enumerate(daily_claim_counts):
        if count > threshold:
            if current_start is None:
                current_start = index
            current_length += 1

            if current_length > best_length:
                best_start = current_start
                best_end = index
                best_length = current_length
        else:
            current_start = None
            current_length = 0

    return best_start, best_end, best_length



def merge_sorted_claim_lists(region_a, region_b):
    i = 0
    j = 0
    merged = []

    while i < len(region_a) and j < len(region_b):
        if region_a[i] <= region_b[j]:
            merged.append(region_a[i])
            i += 1
        else:
            merged.append(region_b[j])
            j += 1

    merged.extend(region_a[i:])
    merged.extend(region_b[j:])
    return merged


def run_tests():
    print("\nTEST CASES")

    empty_bst = ClaimBST()
    assert empty_bst.inorder() == []
    assert empty_bst.search(10) is False

    test_bst = ClaimBST()
    test_bst.insert(20)
    test_bst.insert(10)
    test_bst.insert(30)
    test_bst.insert(20) 
    assert test_bst.inorder() == [10, 20, 30]
    assert test_bst.search(30) is True
    print("PASS: BST empty input, search, and duplicate insertion")

    assert find_duplicate_claims([]) == {}
    sample_claims = [
        {"claim_id": "C101", "policy_number": "POL 123", "incident_date": "2026-01-10"},
        {"claim_id": "C102", "policy_number": "pol123", "incident_date": "2026-01-10"},
        {"claim_id": "C103", "policy_number": "POL-123", "incident_date": "2026-01-10"},
        {"claim_id": "C104", "policy_number": "POL 999", "incident_date": "2026-01-11"},
    ]
    duplicate_groups = find_duplicate_claims(sample_claims)
    assert duplicate_groups[("pol123", "2026-01-10")] == ["C101", "C102"]
    print("PASS: Hashing empty input and case/space-normalized duplicate claims")

    assert shortest_path_bfs({}, "A", "B") is None
    approval_graph = build_graph([
        ("registration", "assessment"),
        ("assessment", "surveyor"),
        ("surveyor", "settlement"),
        ("assessment", "settlement")
    ])
    assert shortest_path_bfs(approval_graph, "registration", "settlement") == [
        "registration", "assessment", "settlement"
    ]
    assert has_cycle_dfs(approval_graph) is False
    cyclic_graph = build_graph([
        ("registration", "assessment"),
        ("assessment", "surveyor"),
        ("surveyor", "assessment")
    ])
    assert has_cycle_dfs(cyclic_graph) is True
    print("PASS: Graph shortest path and DFS cycle detection")

    assert longest_high_claim_run([]) == (None, None, 0)
    assert longest_high_claim_run([20, 100, 99]) == (None, None, 0)
    assert longest_high_claim_run([120, 130, 90, 150, 160, 170, 80]) == (3, 5, 3)
    print("PASS: Sliding-window empty input and consecutive-day run")

    assert merge_sorted_claim_lists([], []) == []
    assert merge_sorted_claim_lists([1, 3], []) == [1, 3]
    assert merge_sorted_claim_lists([1, 3, 5], [2, 3, 6]) == [1, 2, 3, 3, 5, 6]
    print("PASS: Two-pointer merge empty lists and duplicate values")


print("DAY 1 - SET 2: INSURANCE CLAIMS PROCESSING")

print("\nTASK 1: CLAIM ID BINARY SEARCH TREE")
claim_ids = [105, 102, 108, 101, 104, 107, 110, 103, 106, 109, 112, 100, 111, 113, 114]
bst = ClaimBST()
for claim_id in claim_ids:
    bst.insert(claim_id)

print("Claim IDs inserted:", len(claim_ids))
print("Inorder:", bst.inorder())
print("Preorder:", bst.preorder())
print("Postorder:", bst.postorder())
print("Search claim 107:", "Found" if bst.search(107) else "Not found")
print("Search claim 999:", "Found" if bst.search(999) else "Not found")
print("Sorted traversal: Inorder (left, root, right)")

print("\nTASK 2: HASH-BASED DUPLICATE CLAIM DETECTION")
claims = [
    {"claim_id": "CLM-201", "policy_number": "POL 7788", "incident_date": "2026-03-12"},
    {"claim_id": "CLM-202", "policy_number": "pol7788", "incident_date": "2026-03-12"},
    {"claim_id": "CLM-203", "policy_number": "POL 9911", "incident_date": "2026-03-12"},
    {"claim_id": "CLM-204", "policy_number": " POL 7788 ", "incident_date": "2026-03-12"},
    {"claim_id": "CLM-205", "policy_number": "POL 7788", "incident_date": "2026-03-13"}
]
duplicates = find_duplicate_claims(claims)
for key, claim_ids_found in duplicates.items():
    print(f"Normalized key {key}: duplicate claim IDs {claim_ids_found}")
print("Collision handling: hash maps compare keys within collision buckets; unequal keys remain separate.")

print("\nTASK 3: CLAIM APPROVAL GRAPH")
approval_edges = [
    ("registration", "assessment"),
    ("assessment", "surveyor"),
    ("surveyor", "settlement"),
    ("assessment", "settlement")
]
graph = build_graph(approval_edges)
path = shortest_path_bfs(graph, "registration", "settlement")
print("Shortest path registration -> settlement:", path)
print("Cycle detected in approval graph:", has_cycle_dfs(graph))

loop_edges = approval_edges + [("settlement", "assessment")]
loop_graph = build_graph(loop_edges)
print("Cycle detected after adding settlement -> assessment:", has_cycle_dfs(loop_graph))

print("\nTASK 4: LONGEST RUN WITH MORE THAN 100 CLAIMS")
daily_counts = [80, 120, 135, 110, 95, 140, 155, 160, 90, 105, 115, 125, 70, 130]
start, end, length = longest_high_claim_run(daily_counts)
print("Daily claim counts:", daily_counts)
if length:
    print(f"Longest qualifying run: day {start + 1} to day {end + 1} ({length} consecutive days)")
else:
    print("No days exceeded 100 claims.")

print("\nTASK 5: MERGE TWO REGIONAL CLAIM LISTS")
north_region = [101, 104, 108, 115, 120]
south_region = [102, 104, 109, 112, 121]
print("North region:", north_region)
print("South region:", south_region)
print("Merged sorted claims:", merge_sorted_claim_lists(north_region, south_region))

run_tests()

