user_age = int(input("Please enter your age: "))
maximum_heart_rate = 220 - user_age
print("Your maximum heart rate is", maximum_heart_rate, "beats per minute")
minimum_target_heart_rate = 0.5 * maximum_heart_rate
maximum_target_heart_rate = 0.85 * maximum_heart_rate
print("Your target heart rate is between", minimum_target_heart_rate, "-", maximum_target_heart_rate,
      "beats per minute")
