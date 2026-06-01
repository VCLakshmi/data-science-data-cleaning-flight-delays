import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/flights.csv")
print("Atlanta airport flights data 2023:")
print(df)

# new dataframe that only revolves around scheduled flight time vs actual flight time.
departure = df[["scheduled", "actual"]]
print("\n\nSeparating scheduled and actual flight time")
print(departure)

# find the data types used for these colums
print(departure.info())

# convert the strings to datetime format
departure["scheduled"] = pd.to_datetime(departure["scheduled"])
departure["actual"] = pd.to_datetime(departure["actual"])
print("\n\nConverting the scheduled and actual flight time data into python datetime type:")
print(departure)

departure.to_csv("data/processed/flights.csv")

print(departure.info())

departure["delay"] = departure.eval('actual - scheduled')
departure["is_late"] = departure["delay"].dt.total_seconds() > 900
departure["day_name"] = departure["actual"].dt.strftime("%a")
print(departure)

departure.to_csv('output/departures-check-point.csv', index=False, sep='\t')


delay_percentage = departure.groupby("day_name")["is_late"].mean() * 100
print("\nPercentage of flights delayed each day in a week:")
#print(delay_percentage)


# reindex
index = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
delay_percentage = delay_percentage.reindex(index)
print(delay_percentage)

plt.bar(delay_percentage.index, delay_percentage)
plt.xlabel("Days")
plt.ylabel("Percentage delayed")
plt.title("Percentage of flight delayed each day of the week")
plt.savefig("output/figures/percentage-flight-delayed-each-day-of-the-week.png")
plt.show()
