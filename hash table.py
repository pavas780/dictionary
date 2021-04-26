arr =[]
with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")
print(arr)
'''What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
What was the temperature on Jan 9?
What was the temperature on Jan 4?'''
a=0
for i in range(len(arr)):
    if i<7:
        a+=arr[i]

print('the average temperature in first week of Jan is '"{:.2f}".format(a/7))
print(' the maximum temperature in first 10 days of Jan is ',max(arr),'F')

#part2
'''What was the temperature on Jan 9?
What was the temperature on Jan 4?'''

weather_dict = {}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("")
print(weather_dict['Jan 9'])
print(weather_dict['Jan 4'])

