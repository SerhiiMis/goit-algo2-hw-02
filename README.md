# 📘 Homework Assignment: Greedy and Dynamic Programming

## ✅ Task 1: 3D Printer Queue Optimization

**Goal:**  
Optimize the 3D printing job queue using a **greedy algorithm**, respecting priorities and printer constraints.

**Requirements:**

- Input: List of print jobs with `id`, `volume`, `priority`, `print_time`.
- Output:
  - `"print_order"`: list of job IDs in print order.
  - `"total_time"`: total printing time (minutes).
- Constraints:
  - Printer has `max_volume` and `max_items` limits.
  - Higher priority jobs must be printed earlier.
  - Group models together without exceeding limits.
  - Group print time = max print time of models in group.
- Use `dataclass` for data structures.

---

## 🌟 Task 2: Rod Cutting Problem (Memoization and Tabulation)

**Goal:**  
Find the best way to cut a rod to maximize profit, using **Dynamic Programming** with:

- **Memoization**
- **Tabulation**

**Requirements:**

- Input: rod `length` and list of `prices`.
- Output:
  - `"max_profit"`: maximum total profit.
  - `"cuts"`: list of segment lengths.
  - `"number_of_cuts"`: number of cuts made.

**Constraints:**

- Rod length > 0.
- Prices list is non-empty, all values > 0.

**Expected Output Example:**

```python
{
    "max_profit": 12,
    "cuts": [2, 2, 1],
    "number_of_cuts": 2
}
```
