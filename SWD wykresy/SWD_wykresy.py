import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import glob

# Get a list of all CSV files
files = glob.glob('*.csv')
# Set the DPI of your monitor (e.g., 96 for many monitors)
my_dpi = 96
width, height = 1600, 800

# Initialize lists to store x and y values
x_values = []
y_values = []

# Loop through each file
for i, file in enumerate(files):
    # Load the CSV file
    df = pd.read_csv(file)
    # Extract x and y values
    x = df.columns[2:].str.extractall('(\d+\.?\d*)')[0].astype(float).values
    y = df.iloc[0, 2:].values*1000
    # If this is the first file, store the x values
    if i == 0:
        x_values = x

    # Append the y values
    y_values.append(y)

# Convert y_values to a 2D numpy array and compute the average along the 0th axis
y_values = np.array(y_values)
y_avg = np.mean(y_values, axis=0)

# Create a bar plot
fig = plt.figure(figsize=(width/my_dpi, height/my_dpi), dpi=my_dpi)
x = [a for a in range(len(x_values))]
# Define the start and end points for each line, their colors, and line styles
lines = [((2, 150), (5, 20), 'green', '-'),  # SWD I
         ((5, 20), (23.97, 20), 'green', '-'),   # line 2,
         ((23.97, 20), (81, 200), 'green', '-'),
         ((4.24, 30), (28.61, 30), 'green', '--'),
         ((2, 600), (5, 100), 'orange', '-'),  # line 1, solid line
         ((5, 100), (23.97, 100), 'orange', '-'),   # line 2,
         ((23.97, 100), (81, 1150), 'orange', '-'),
         ((4.24, 150), (28.51, 150), 'orange', '--'),
         ((2, 3400), (5, 520), 'red', '-'),  # line 1, solid line
         ((5, 520), (23.97, 520), 'red', '-'),
         ((23.97, 520), (81, 7000), 'red', '-'),
         ((4.24, 800), (28.51, 800), 'red', '--'),
         ((2, 7000), (5, 2100), 'black', '-'),  # line 1, solid line
         ((5, 2100), (23.97, 2100), 'black', '-'), 
         ((23.97, 2100), (68, 8500), 'black', '-'),
         ((3.87, 3100), (31.42, 3100), 'black', '--'),
         # Add more lines as needed
        ]

for (x1, y1), (x2, y2), color, linestyle in lines:
    # Find the indices of the two closest values in x_values to x1 and x2
    x1_index = np.argmin(np.abs(np.array(x_values) - x1))
    x2_index = np.argmin(np.abs(np.array(x_values) - x2))

    # Interpolate the x-coordinates to the corresponding indices
    xn = [x1_index + (x1 - x_values[x1_index]) / (x_values[x1_index + 1] - x_values[x1_index]),
          x2_index + (x2 - x_values[x2_index]) / (x_values[x2_index + 1] - x_values[x2_index])]
    yn = [y1 , y2]

    plt.plot(xn, yn, color=color, linestyle=linestyle)
plt.bar(x, y_avg, log=True)
plt.xticks(x,x_values)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel(r'Przyspieszenie $[mm/s^2]$')
plt.title('SWD I')
plt.legend()
plt.grid(True)
plt.savefig('SWD I.png', dpi=my_dpi)



fig = plt.figure(figsize=(width/my_dpi, height/my_dpi), dpi=my_dpi)
# Define the start and end points for each line, their colors, and line styles
lines = [((1, 22), (6.3, 22), 'green', '-'),  # SWD II
         ((6.3, 22), (100, 190), 'green', '-'),   # line 2,
         ((1, 39), (6.3, 39), 'green', '--'),
         ((6.3, 39), (100, 300), 'green', '--'),
         ((1, 80), (6.75, 80), 'orange', '-'),  # line 1, solid line
         ((6.75, 80), (100, 600), 'orange', '-'),   # line 2,
         ((1, 130), (6.75, 130), 'orange', '--'),
         ((6.75, 130), (100, 1000), 'orange', '--'),
         ((1, 400), (6.3, 400), 'red', '-'),  # line 1, solid line
         ((6.3, 400), (100, 3400), 'red', '-'),
         ((1, 700), (6.3, 700), 'red', '--'),
         ((6.3, 700), (100, 6000), 'red', '--'),
         ((1, 3000), (8, 3000), 'black', '-'),  # line 1, solid line
         ((8, 3000), (80, 10000), 'black', '-'), 
         ((1, 5000), (8, 5000), 'black', '--'),
         ((8, 5000), (32, 10000), 'black', '--'),
         # Add more lines as needed
        ]

for (x1, y1), (x2, y2), color, linestyle in lines:
    x1_index = np.argmin(np.abs(np.array(x_values) - x1))
    x2_index = np.argmin(np.abs(np.array(x_values) - x2))

    if x1_index + 1 < len(x_values):
        x1n = x1_index + (x1 - x_values[x1_index]) / (x_values[x1_index + 1] - x_values[x1_index])
    else:
        x1n = x1_index

    if x2_index + 1 < len(x_values):
        x2n = x2_index + (x2 - x_values[x2_index]) / (x_values[x2_index + 1] - x_values[x2_index])
    else:
        x2n = x2_index

    yn = [y1 , y2]

    plt.plot([x1n, x2n], yn, color=color, linestyle=linestyle)

plt.bar(x, y_avg, log=True)
plt.xticks(x,x_values)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel(r'Przyspieszenie $[mm/s^2]$')
plt.title('SWD II')
plt.legend()
plt.grid(True)
plt.savefig('SWD II.png', dpi=my_dpi)
