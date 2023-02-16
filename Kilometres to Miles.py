def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles


kilometers = float(input("Enter the distance in kilometers: "))
miles = km_to_miles(kilometers)
print("The distance in miles is:", miles)
