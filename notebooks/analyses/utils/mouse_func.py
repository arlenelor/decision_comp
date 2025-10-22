import numpy as np 


def time_normalize(x_coord, y_coord, n_time_steps): 
    '''
    Takes in the original x and y coordinates, and returns the normalized coordinates accordingly. 

    Inputs: 
    - x_coord: Numpy array (of x coordinates)
    - y_coord: Numpy array (of y coordinates)

    Returns: 
    - x_coord_norm: Numpy array (of time normalized x coordinates)
    - y_coord_norm: Numpy array (of time normalized y coordinates)
    '''
    
    # Define time
    len_time = len(y_coord)
    orig_time = np.linspace(0, 1, len_time) # define original time
    norm_time = np.linspace(0, 1, n_time_steps) # define normalized time 

    # Apply linear interpolation to x and y coordinates accordingly
    x_coord_norm = np.interp(norm_time, orig_time, x_coord) 
    y_coord_norm = np.interp(norm_time, orig_time, y_coord)

    return x_coord_norm, y_coord_norm

def dist_from_end(x_coords, y_coords): 
    '''
    Takes in the x and y coordinates, and finds the distance from the end point (final decision). 

    Inputs: 
    - x_coord: Numpy array (of x coordinates)
    - y_coord: Numpy array (of y coordinates)

    Returns: 
    - coord_distances: Numpy array (of the distances from start point)
    '''

    # Define the beginning coordinates
    x_end, y_end = x_coords[-1], y_coords[-1]

    # Get the distance from the start of each timepoint
    coord_distances = np.sqrt((x_coords - x_end)**2 + (y_coords - y_end)**2)

    return coord_distances

def get_cumulative_max_x_deviation(x_coords):
    """
    Calculates the maximum x-deviation from straight path up to each timepoint, and returns array 
    of the cumulative maximum x-deviation. 

    Inputs: 
    - x_coord: Numpy array (of x coordinates)
    
    Outputs: 
    - cumulative_max: Numpy array (of the cumulative max deviation of the given x coordinates) 

    """
    # compute the straight line trajectory
    x_straight = np.linspace(x_coords[0], x_coords[-1], len(x_coords))
    
    # for each timepoint, calculates the difference with the corresponding point in the straight line
    x_deviations = np.abs(x_coords - x_straight) # apply absolute deviation
    
    # Cumulative maximum deviation
    cumulative_max = np.maximum.accumulate(x_deviations)
    
    return cumulative_max

    

