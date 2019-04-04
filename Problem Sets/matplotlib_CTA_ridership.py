# CTA Ridership (28pts)

#  Get the csv from the following data set.
#  https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
#  This shows CTA ridership by year going back to the 80s


#1  Make a plot of rail usage for the most current 10 year period.  (year on x axis, and ridership on y) (5pts)
#2  Plot bus usage for the same years as a second line on your graph. (5pts)
#3  Plot bus and rail usage together on a third line on your graph. (5pts)
#4  Add a title and label your axes. (5pts)
#5  Add a legend to show data represented by each of the three lines. (5pts)
#6  What trend or trends do you see in the data?  Offer at least two hypotheses which might explain the trend(s). (3pts)

import matplotlib.pyplot as plt
import csv

with open('../Notes/Imports/CTA.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

header = data.pop(0)
print(header)
plt.figure(1, tight_layout=True, figsize=(12, 8), facecolor="lightblue")


# part 1

year = [x[0] for x in data]
rail_riders = [x[3] for x in data]

ten_years_ago = year[-10:]
past_rail = rail_riders[-10:]

ten_years = [int(x) for x in ten_years_ago]
ten_years_rail = [int(x) for x in past_rail]

plt.xticks(ten_years, rotation=50, fontsize=12)

# part 2

bus_usage = [x[1] for x in data]

bus = [x[1] for x in data]
past_bus = bus[-10:]
ten_bus = [int(x) for x in past_bus]

plt.plot(ten_years, ten_bus, color='lightblue', label="Bus")

# part 3
total = [x[4] for x in data]
total_ten = total[-10:]
ten_total = [int(x) for x in total_ten]

# part 4
plt.plot(ten_years, ten_years_rail, color="lightpink", label="Train")
plt.title("Rail Usage Over Past 10 Years")
plt.xlabel("Year")
plt.ylabel("Hundreds of Millions of People")

plt.plot(ten_years, ten_total, color='yellow', label="Total")

# part 5
plt.legend()

plt.show()

# part 6
'''
I see that overall, CTA usage has gone down in the past 10 years. Bus usage is down also, though train usage has risen a 
small amount. I would think that the overall usage being down is due to new companies like Uber and Lyft which have 
exploded in popularity over the past couple of years. Another reason could be many cities like Chicago are trying to 
reduce emissions by improving bike lanes and other other eco-friendly modes of transportation. 
'''