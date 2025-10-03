from load import airports, airlines, connections 
from costs import costs  
from plot import plot 
from scipy.optimize import linear_sum_assignment 
import numpy as np  

# Set the airport we want to use as origin
target_airport = 'Bologna'

# Load all our data
A = airports()
L = airlines() 
C = connections()

# Find the index of our target airport
cities = [row[0] for row in A]  # get list of all city names
origin = cities.index(target_airport) if target_airport in cities else 0  # find index of our target

# Check if our target airport was found
if target_airport not in cities:
    print(f"Warning: {target_airport} not found in airports, using first airport instead")

# Compute the costs matrices
tmat, fmat, pmat = costs(A, L, C, origin)

# Check if we have any valid connections
if len(tmat) == 0 or len(tmat[0]) == 0:
    # If no connections give error
    print("Error: No valid connections found")
    rows = []
    cols = []
else:
    # Convert to numpy array
    tmat_np = np.array(tmat)
    
    # Check if all values in time matrix are valid
    has_valid_values = True
    for row in tmat:
        for val in row:
            if val == float('inf') or val > 1e10:
                has_valid_values = False
    
    if has_valid_values:
        # Apply Hungarian algorithm to find optimal assignment
        rows, cols = linear_sum_assignment(tmat_np)
    else:
        # Fall back to simple assignment if data is invalid
        print("Warning: Invalid values in cost matrix")
        # Make a simple diagonal assignment
        n = min(len(tmat), len(tmat[0]))
        rows = list(range(n))
        cols = list(range(n)) 

# Only plot if we have assignments
if len(rows) > 0:
    plot(L, fmat, pmat, rows, cols, A[origin][0])
else:
    print("No assignments found, can't plot")