import matplotlib.pyplot as plt

fig, ax=plt.subplots()

x=[1,2]
y=[1,2]

ax.plot(x,y)
plt.show()



Use the parse_dates key-word argument to parse the "date" column as dates. ****
Use the index_col key-word argument to set the "date" column as the index *****


    # Import pandas
    import pandas as pd

    # Read the data from file using read_csv
    climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")  *******!!!!! 2 STEPS




Add the data from climate_change to the plot: use the DataFrame index for the x value and the "relative_temp" column for the y values
The DataFrame index is accessed through: climate_change.index


import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')



# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]  ***** SUBSET THE TIME PERIOD BEFOREHAND

# Add the time-series for "co2" data from seventies to the plot , key part notice use of seventies
ax.plot(seventies.index, seventies["co2"])

# Show the figure




def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    # Plot the inputs x,y in the provided color
    axes.plot(x, y, color=color)

    # Set the x-axis label
    axes.set_xlabel(xlabel)

    # Set the y-axis label
    axes.set_ylabel(ylabel, color=color)

    # Set the colors tick params for y-axis
    axes.tick_params('y', colors=color)

*****SHOULD THERE BE A WAY TO END THE FUNCTION ???


The twinx method does not take any inputs and is called with empty parentheses: ax.twinx()   *******!!!!!

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', "Time (years)",
                "Relative temperature (Celsius)")

plt.show()


result is two line charts with two y axes