# data = []
# with open("weather_data.csv", 'r', newline='') as csvFile:
#     for line in csvFile:
#         data.append(line)
#
# print(data)

# using csv
# import csv
# with open("weather_data.csv", 'r') as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(float(row[1]))
#     print(temperatures)

# using pandas library
# import pandas
# data = pandas.read_csv('weather_data.csv')
# temp = data['temp']
#
# monday = data[data.day == "Monday"]
# temp_F = monday.temp*(9/5)+32
# print(temp_F)

# squirrel data set
import pandas
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240602.csv')
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
new_data = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_squirrels_count, gray_squirrels_count, red_squirrels_count]
}
new_df = pandas.DataFrame(new_data)
new_df.to_csv("squirrel_fur_color_count.csv")