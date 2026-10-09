import numpy as np
from scipy.optimize import linprog

def solve_logistics_optimisation():
    print("==================================================")
    print(" Caterpillar-Inspired Logistics Optimisation Model ")
    print("==================================================\n")
    
    # Objective: Minimise delivery costs from 2 warehouses to 3 dealership hubs
    # Cost matrix (per unit routing):
    # Warehouses -> Hub 1, Hub 2, Hub 3
    # WH 1:         [R4,    R5,    R6]
    # WH 2:         [R6,    R4,    R3]
    c = [4, 5, 6, 6, 4, 3]

    # Inequality constraints (Supply limits at Warehouses)
    # WH1 supply <= 500 units; WH2 supply <= 400 units
    A_ub = [,  # WH1 allocations
        [0, 0, 0, 1, 1, 1]   # WH2 allocations
    ]
    b_ub = [500, 400]

    # Equality constraints (Exact demand required at dealership Hubs)
    # Hub 1 demand = 200, Hub 2 demand = 300, Hub 3 demand = 350
    A_eq = [,  # Hub 1 demand,  # Hub 2 demand
        [0, 0, 1, 0, 0, 1]   # Hub 3 demand
    ]
    b_eq = [200, 300, 350]

    # Bounds: Allocations cannot be negative values
    bounds = [(0, None)] * 6

    # Solve using the HiGHS optimisation solver algorithm
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if result.success:
        print("Optimisation Successful!")
        print(f"Optimal Minimum Operating Cost: R{result.fun:,.2f}\n")
        
        # Format the output data allocation matrix
        allocations = result.x
        print("Optimal Distribution Matrix (Units to Route):")
        print(f"  • Warehouse 1 to Hub 1: {allocations[0]:.0f} units")
        print(f"  • Warehouse 1 to Hub 2: {allocations[1]:.0f} units")
        print(f"  • Warehouse 1 to Hub 3: {allocations[2]:.0f} units")
        print(f"  • Warehouse 2 to Hub 1: {allocations[3]:.0f} units")
        print(f"  • Warehouse 2 to Hub 2: {allocations[4]:.0f} units")
        print(f"  • Warehouse 2 to Hub 3: {allocations[5]:.0f} units")
    else:
        print("Optimisation failed. Please check constraints.")

if __name__ == "__main__":
    solve_logistics_optimisation()
