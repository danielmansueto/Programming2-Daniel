# https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c

'''
Energy Efficiency of Chicago Schools (35pts)
Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
We will use this data at the link above to look at schools.  
We will visualize the efficiency of schools by scatter plot.  
We hypothesize that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)

Challenge (for fun if you have time... not required):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

with open('Chicago_Energy_Benchmarking.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

header = data.pop(0)
print(header)

greenhouse = []
square_footage = []
school_name = []

for school in data:
    if school[6] == "K-12 School":
        try:
            ghg = float(school[20])
            square_feet = float(school[7])
            school_name.append(school[2])
            greenhouse.append(ghg)
            square_footage.append(square_feet)
        except:
            print(school[0], school[2], "didn't work")

print(school_name)
print(greenhouse)
print(square_footage)


plt.figure(1, tight_layout=True, figsize=(12, 7), facecolor="lightgrey")
plt.scatter(square_footage, greenhouse, color="lightblue")

plt.xlabel('Building Square Footage')
plt.ylabel('Greenhouse Gas Emissions')
plt.title('Energy Emissions of Chicago K-12 Schools')

# parker
parker = [x for x in data[school_name.index("Francis W Parker School")]]
print(parker)

fwp_ghg = int(parker[20])
fwp_sqft = int(parker[7])
print(fwp_ghg)
print(fwp_sqft)

plt.scatter(fwp_sqft, fwp_ghg, color="blue", label='Francis Parker School')

# latin
latin = [x for x in data[school_name.index("Latin School of Chicago Upper School")]]
#print(latin)

latin_ghg = int(latin[20])
latin_sqft = int(latin[7])

plt.scatter(latin_sqft, latin_ghg, color="red", label='Latin Upper School')

# top and bottom 3 schools

new_data = []
for i in range(len(school_name)):
    new_data.append([school_name[i], greenhouse[i], square_footage[i]])

print(new_data)
print(new_data[0])
print(new_data[0][1]/new_data[0][2])
new_data.sort(key=lambda x: x[1]/x[2])
print("THIS")
print(new_data)

for i in range(3):
    plt.annotate(new_data[i][0], xy=(float(new_data[i][1]), float(new_data[i][2])), color='orange')

for i in range(3):
    plt.annotate(new_data[-i - 1][0], xy=(float(new_data[-i - 1][1]), float(new_data[-i - 1][2])), color='purple')

# best fit line
m, b = np.polyfit(square_footage, greenhouse, 1)

fit_x = [0, 700000]
fit_y = [b, 700000 * m]
plt.plot(fit_x, fit_y)


plt.legend()
plt.show()