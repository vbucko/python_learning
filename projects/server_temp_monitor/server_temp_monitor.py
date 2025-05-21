# Print the initial instruction to the user
print("Enter temperature or type 'stop'")

# Initialize the number of temperature alerts to zero
alerts = 0

# Start an infinite loop to monitor temperatures
while True:
     # Ask for user input
    temperature = input()
   
    # If the user types 'stop', we exit the loop
    if temperature == "stop":
        break

    else:
        # Convert the input string to a float number
        temp = float(temperature)
        print(f"We have converted the temperature value {temp} to the float data type")

    # Check if the temperature is within the safe range
    if temp <= 30:
        print("Everything is OK")
        
    else:
        # If temperature is too high, print a warning and increase the alert counter
        print("Warning: The temperature is too high!")
        alerts += 1
# After the loop ends, print the total number of alerts
print(f"Number of alerts: {alerts}")
    