# Day 1 — Python Data Structures and Algorithms Assignments

This repository contains three Day 1 assignments that apply Python data structures and algorithm patterns to practical business scenarios.

## Assignments

### Set 1 — Retail Order Desk

This assignment focuses on order searching, sorting, duplicate detection, stack and queue operations, and the coin change problem using Python.

**Tasks covered**
1. **Searching:** Linear search and binary search to retrieve an order by ID.
2. **Sorting:** Bubble sort and merge sort to rank orders by amount in descending order.
3. **Duplicate Detection:** A set-based approach using `customerId`, `amount`, and the creation minute.
4. **Stack and Queue:** Custom stack for undo operations and custom queue for dispatch.
5. **Coin Change:** Greedy and dynamic-programming approaches using amount `6` and denominations `[1, 3, 4]`.

**Files**
| File | Description |
|---|---|
| `source_code.py` | Python source code implementing all five tasks. |
| `orders.csv` | Input dataset containing 50,003 order records. |
| `output_and_complexity.md` | Console output, time/space complexity analysis, and data-structure rationale. |

**Requirements**
- Python 3
- No external Python packages required

**Run**
Keep `set1.py` and `orders.csv` in the same folder. The program opens the input file using the exact filename `orders.csv`.

```bash
python source_code.py
```

If the downloaded CSV has a different name, rename it to `orders.csv` before running the script.

### Set 2 — Retail Banking Transaction Review

This assignment reviews a retail bank's card transactions using searching, sorting, duplicate detection, queue and stack operations, and divide-and-conquer.

**Tasks covered**
1. Linear and binary search over 100,000 sorted transaction IDs, with comparison counts.
2. Insertion sort and merge sort of a customer statement by timestamp, including stability.
3. Duplicate posting detection using account, amount, merchant, and a 60-second timestamp window.
4. Array-based FIFO queue for manual review and LIFO stack for reversing adjustments.
5. Divide-and-conquer and brute-force methods for finding the minimum and maximum transaction amounts.

**Files**
| File | Description |
|---|---|
| `source_code.py` | Supplied Python source code implementing the five tasks. |
| `output_and_complexity.md` | Actual console output, complexity table, and data-structure rationale. |

**Requirements**
- Python 3
- No external packages required

**Run**
```bash
python source_code.py
```

### Set 3 — Hospital Appointment Desk

This assignment models a hospital appointment desk using searching, sorting, duplicate-slot detection, queue and stack data structures, and dynamic programming.

**Tasks covered**
1. Linear and binary search over 20,000 patient records, with 1,000 lookups.
2. Selection sort and quick sort by urgency and arrival time, with swap counts and timings.
3. Double-booking detection using a set of patient-and-slot keys.
4. Scratch-built circular queue for walk-in tokens and stack for recent patient history.
5. Dynamic programming and greedy comparison for selecting non-overlapping appointments.

**Files**
| File | Description |
|---|---|
| `source_code.py` | Supplied Python source code implementing all five tasks. |
| `output_and_complexity.md` | Actual console output, complexity table, data-structure rationale, and a typed selection-sort trace. |

**Requirements**
- Python 3
- No external packages required

**Run**
```bash
python source_code.py
```

## Execution Output and Complexity

Each assignment includes an `output_and_complexity.md` file containing its captured execution output and complexity analysis. Refer to the corresponding file in each set's folder for the detailed results.

## Suggested Folder Structure

```text
Day-1/
├── Set-1-Retail-Order-Desk/
│   ├── source_code.py
│   ├── orders.csv
│   └── output_and_complexity.md
├── Set-2-Retail-Banking/
│   ├── source_code.py
│   └── output_and_complexity.md
└── Set-3-Hospital-Appointment-Desk/
    ├── source_code.py
    └── output_and_complexity.md
```

## General Notes

- Run each script from its own assignment folder.
- For Set 1, keep `orders.csv` in the same folder as `set1.py`.
- The execution timings recorded in output files can vary depending on the machine and system load.
