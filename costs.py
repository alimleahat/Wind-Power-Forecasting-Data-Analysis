from distance import dist

def costs(airports, airlines, conns, origin=0):
    # Get number of airports and airlines
    nA = len(airports)
    nL = len(airlines)
    
    # Initialize matrices for time, fuel and price
    t = [[1e6]*nA for _ in range(nL)] 
    f = [[0]*nA   for _ in range(nL)] 
    p = [[0]*nA   for _ in range(nL)]  
    
    # Loop through each airline
    for i, (name, spd, ff, pf) in enumerate(airlines):
        # Get connection matrix for this airline
        mat = conns.get(name, [])
        
        # Check connections to all possible destinations
        for j in range(nA):
            # If connection exists (equals 1 in the matrix)
            if mat and mat[origin][j] == 1:
                # Calculate distance using Haversine formula
                d = dist(airports[origin][1], airports[origin][2], airports[j][1], airports[j][2])
                
                # Calculate time
                t[i][j] = d/spd
                
                # Calculate fuel = distance * fuel factor
                f[i][j] = d*ff
                
                # Calculate price = distance * price factor
                p[i][j] = d*pf
    
    # Return all three matrices
    return t, f, p