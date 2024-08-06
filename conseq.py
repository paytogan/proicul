import pandas as pd

# Sample position data
positions = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Convert positions to a dataframe
trajectory_df = pd.DataFrame(positions, columns=['x', 'y'])

# Display the trajectory dataframe
print(trajectory_df)
