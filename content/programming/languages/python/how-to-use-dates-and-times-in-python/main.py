from datetime import datetime

# .now()
my_time = datetime.now()
print(my_time)

my_time = datetime(2087, 7, 23, 18, 43, 3, 690)
print(my_time)

my_time = datetime(2087, 7, 23)
print(my_time)

# strftime()
my_time = datetime(2020, 1, 6, 14, 37, 53)
print(datetime.strftime(my_time, '%Y'))

my_time = datetime.strptime('2020-01-17 13:24:03', '%Y-%m-%d %H:%M:%S')
print(type(my_time))
print(my_time)