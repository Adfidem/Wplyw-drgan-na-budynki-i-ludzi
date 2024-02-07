import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


import glob



# Get a list of all CSV files
filesX = glob.glob('X/*.csv')
filesY = glob.glob('Y/*.csv')
filesZ = glob.glob('Z/*.csv')
# Set the DPI of your monitor (e.g., 96 for many monitors)
my_dpi = 96
width, height = 1600, 800
nfile = glob.glob('n.txt')
n = 64
for filename in nfile:
    with open(filename, 'r') as f:
        # Read the contents of the file
        contents = f.read()
        # Extract the number from the contents
        n = float(''.join(filter(str.isdigit, contents)))


def get_data(files):
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
 
    return x_values, y_values

Xx_values, Xy_values = get_data(filesX)
Yx_values, Yy_values = get_data(filesY)
Zx_values, Zy_values = get_data(filesZ)

# Convert y_values to a 2D numpy array and compute the average along the 0th axis
Xy_values = np.array(Xy_values)
Xy_avg = np.mean(Xy_values, axis=0)
Yy_values = np.array(Yy_values)
Yy_avg = np.mean(Yy_values, axis=0)
Zy_values = np.array(Zy_values)
Zy_avg = np.mean(Zy_values, axis=0)


# Create a bar plot
fig = plt.figure(figsize=(width/my_dpi, height/my_dpi), dpi=my_dpi)
x = [a for a in range(len(Xx_values))]
# Define the start and end points for each line, their colors, and line styles
lines = [((1, 3.57), (1.25, 3.57), 'green', '-'),  # SWD I
         ((1.25, 3.57), (1.6, 3.57), 'green', '-'),
         ((1.6, 3.57), (2, 3.57), 'green', '-'),
         ((2, 3.57), (2.5, 4.46), 'green', '-'),
         ((2.5, 4.46), (3.15, 5.7), 'green', '-'),
         ((3.15, 5.7), (4, 7.14), 'green', '-'),
         ((4, 7.14), (5, 8.93), 'green', '-'),
         ((5, 8.93), (6.3, 11.4), 'green', '-'),
         ((6.3, 11.4), (8, 14.3), 'green', '-'),
         ((8, 14.3), (10, 17.9), 'green', '-'),
         ((10, 17.9), (12.5, 22.5), 'green', '-'),
         ((12.5, 22.5), (16, 28.6), 'green', '-'),
         ((16, 28.6), (20, 35.7), 'green', '-'),
         ((20, 35.7), (25, 44.6), 'green', '-'),
         ((25, 44.6), (31.5, 56.39), 'green', '-'),
         ((31.5, 56.39), (40, 71.4), 'green', '-'),
         ((40, 71.4), (50, 89.3), 'green', '-'),
         ((50, 89.3), (63, 113), 'green', '-'),
         ((63, 113), (80, 143), 'green', '-'),
         # Add more lines as needed
        ]

for (x1, y1), (x2, y2), color, linestyle in lines:
    x1_index = np.argmin(np.abs(np.array(Xx_values) - x1))
    x2_index = np.argmin(np.abs(np.array(Xx_values) - x2))

    if x1_index + 1 < len(Xx_values):
        x1n = x1_index + (x1 - Xx_values[x1_index]) / (Xx_values[x1_index + 1] - Xx_values[x1_index])
    else:
        x1n = x1_index

    if x2_index + 1 < len(Xx_values):
        x2n = x2_index + (x2 - Xx_values[x2_index]) / (Xx_values[x2_index + 1] - Xx_values[x2_index])
    else:
        x2n = x2_index
        
    yn = [y1*n , y2*n]

    plt.plot([x1n, x2n], yn, color=color, linestyle=linestyle)

plt.bar(x, Xy_avg, log=True)
plt.xticks(x,Xx_values)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel(r'RMS przyspieszenia $[mm/s^2]$')
plt.title('X')
plt.legend()
plt.grid(True)
plt.savefig('X.png', dpi=my_dpi)


# Create a bar plot
fig = plt.figure(figsize=(width/my_dpi, height/my_dpi), dpi=my_dpi)
x = [a for a in range(len(Xx_values))]
# Define the start and end points for each line, their colors, and line styles
lines = [((1, 3.57), (1.25, 3.57), 'green', '-'),  # SWD I
         ((1.25, 3.57), (1.6, 3.57), 'green', '-'),
         ((1.6, 3.57), (2, 3.57), 'green', '-'),
         ((2, 3.57), (2.5, 4.46), 'green', '-'),
         ((2.5, 4.46), (3.15, 5.7), 'green', '-'),
         ((3.15, 5.7), (4, 7.14), 'green', '-'),
         ((4, 7.14), (5, 8.93), 'green', '-'),
         ((5, 8.93), (6.3, 11.4), 'green', '-'),
         ((6.3, 11.4), (8, 14.3), 'green', '-'),
         ((8, 14.3), (10, 17.9), 'green', '-'),
         ((10, 17.9), (12.5, 22.5), 'green', '-'),
         ((12.5, 22.5), (16, 28.6), 'green', '-'),
         ((16, 28.6), (20, 35.7), 'green', '-'),
         ((20, 35.7), (25, 44.6), 'green', '-'),
         ((25, 44.6), (31.5, 56.39), 'green', '-'),
         ((31.5, 56.39), (40, 71.4), 'green', '-'),
         ((40, 71.4), (50, 89.3), 'green', '-'),
         ((50, 89.3), (63, 113), 'green', '-'),
         ((63, 113), (80, 143), 'green', '-'),
         # Add more lines as needed
        ]

for (x1, y1), (x2, y2), color, linestyle in lines:
    x1_index = np.argmin(np.abs(np.array(Xx_values) - x1))
    x2_index = np.argmin(np.abs(np.array(Xx_values) - x2))

    if x1_index + 1 < len(Xx_values):
        x1n = x1_index + (x1 - Xx_values[x1_index]) / (Xx_values[x1_index + 1] - Xx_values[x1_index])
    else:
        x1n = x1_index

    if x2_index + 1 < len(Xx_values):
        x2n = x2_index + (x2 - Xx_values[x2_index]) / (Xx_values[x2_index + 1] - Xx_values[x2_index])
    else:
        x2n = x2_index
        
    yn = [y1*n , y2*n]

    plt.plot([x1n, x2n], yn, color=color, linestyle=linestyle)

plt.bar(x, Yy_avg, log=True)
plt.xticks(x,Xx_values)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel(r'RMS przyspieszenia $[mm/s^2]$')
plt.title('Y')
plt.legend()
plt.grid(True)
plt.savefig('Y.png', dpi=my_dpi)


# Create a bar plot
fig = plt.figure(figsize=(width/my_dpi, height/my_dpi), dpi=my_dpi)
x = [a for a in range(len(Xx_values))]
# Define the start and end points for each line, their colors, and line styles
lines = [((1, 10), (1.25, 8.9), 'green', '-'),  # SWD I
         ((1.25, 8.9), (1.6, 7.91), 'green', '-'),
         ((1.6, 7.91), (2, 7.07), 'green', '-'),
         ((2, 7.07), (2.5, 6.31), 'green', '-'),
         ((2.5, 6.31), (3.15, 5.7), 'green', '-'),
         ((3.15, 5.7), (4, 5), 'green', '-'),
         ((4, 5), (5, 5), 'green', '-'),
         ((5, 5), (6.3, 5), 'green', '-'),
         ((6.3, 5), (8, 5), 'green', '-'),
         ((8, 5), (10, 6.25), 'green', '-'),
         ((10, 6.25), (12.5, 7.81), 'green', '-'),
         ((12.5, 7.81), (16, 10), 'green', '-'),
         ((16, 10), (20, 12.5), 'green', '-'),
         ((20, 12.5), (25, 15.6), 'green', '-'),
         ((25, 15.6), (31.5, 19.73), 'green', '-'),
         ((31.5, 19.73), (40, 25), 'green', '-'),
         ((40, 25), (50, 31.3), 'green', '-'),
         ((50, 31.3), (63, 39.4), 'green', '-'),
         ((63, 39.4), (80, 50), 'green', '-'),
         # Add more lines as needed
        ]

for (x1, y1), (x2, y2), color, linestyle in lines:
    x1_index = np.argmin(np.abs(np.array(Xx_values) - x1))
    x2_index = np.argmin(np.abs(np.array(Xx_values) - x2))

    if x1_index + 1 < len(Xx_values):
        x1n = x1_index + (x1 - Xx_values[x1_index]) / (Xx_values[x1_index + 1] - Xx_values[x1_index])
    else:
        x1n = x1_index

    if x2_index + 1 < len(Xx_values):
        x2n = x2_index + (x2 - Xx_values[x2_index]) / (Xx_values[x2_index + 1] - Xx_values[x2_index])
    else:
        x2n = x2_index
        
    yn = [y1*n , y2*n]

    plt.plot([x1n, x2n], yn, color=color, linestyle=linestyle)

plt.bar(x, Zy_avg, log=True)
plt.xticks(x,Xx_values)
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel(r'RMS przyspieszenia $[mm/s^2]$')
plt.title('Z')
plt.legend()
plt.grid(True)
plt.savefig('Z.png', dpi=my_dpi)
