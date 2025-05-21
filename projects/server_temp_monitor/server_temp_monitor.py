print("Enter temperature or type 'stop'")
alerts = 0

while True:
    temperature = input()
    if temperature == "stop":
        break

    else:
        temp = float(temperature)
        print(f"We have converted the temperature value {temp} to the float data type")
    if temp <= 30:
        print("Everything is OK")
        
    else:
        print("Warning: The temperature is too high!")
        alerts += 1

print(f"Number of alerts: {alerts}")
    