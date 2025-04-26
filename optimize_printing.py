from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    jobs = [PrintJob(**job) for job in print_jobs]
    constraints = PrinterConstraints(**constraints)

    # Sort jobs by priority first (1 highest), then by print time (shorter first)
    jobs.sort(key=lambda job: (job.priority, job.print_time))

    print_order = []
    total_time = 0
    current_group = []
    current_volume = 0

    for job in jobs:
        if (current_volume + job.volume <= constraints.max_volume and
            len(current_group) + 1 <= constraints.max_items):
            current_group.append(job)
            current_volume += job.volume
        else:
            # Print current group
            if current_group:
                total_time += max(j.print_time for j in current_group)
                print_order.extend(j.id for j in current_group)
            # Start new group
            current_group = [job]
            current_volume = job.volume

    # Print remaining group
    if current_group:
        total_time += max(j.print_time for j in current_group)
        print_order.extend(j.id for j in current_group)

    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Testing
def test_printing_optimization():
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Test 1:")
    print(optimize_printing(test1_jobs, constraints))

    print("\nTest 2:")
    print(optimize_printing(test2_jobs, constraints))

    print("\nTest 3:")
    print(optimize_printing(test3_jobs, constraints))

if __name__ == "__main__":
    test_printing_optimization()
