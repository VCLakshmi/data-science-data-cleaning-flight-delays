import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/us-daily-passengers.csv")

# convert the date into datetime format
df["date_formatted"] = pd.to_datetime(df["date"], format="mixed")

# add column day which is calculated using the formatted date.
df["day"] = df["date_formatted"].dt.strftime("%a")

print(df)
print(df.info())

# average number of passengers per day in a week.
average_passengers = df.groupby("day")["num_passengers"].mean().round(0).astype(int)
index = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
average_passengers = average_passengers.reindex(index=index)

print("\n\nAverage number of passengers flying per day in a week: ")
print(average_passengers)
average_passengers.to_csv("output/average_passengers_flying_per_day_in_a_week.csv")
print(type(average_passengers))

# plot the graph that shows the average number of passengers flying per day in a week
plt.bar(average_passengers.index, average_passengers)
plt.title("Average number of passengers flying per day in a week")
plt.xlabel("Day")
plt.ylabel("Avg number of passengers flying")
plt.savefig("output/figures/average-passengers-count-flying-per-day-in-a-week.png")
plt.show()
