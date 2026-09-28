import numpy as np
temperature = np.array([32, 29, 35, 31, 28, 33, 30])
print("Average temperature:", np.mean(temperature))
print("Highest temperature:", np.max(temperature))
print("Lowest temperature:", np.min(temperature))
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]
print("Days above 30°C:")
for i in range(7):
    if temperature[i] > 30:
        print(days[i], temperature[i], "°C")
updated_temperature = temperature + 2

print("Updated temperatures:", updated_temperature)