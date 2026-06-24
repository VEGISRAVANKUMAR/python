rides = ["bike", "car", "auto"]

choose = input("Select vehicle: ")

if choose in rides:
    km = int(input("Enter distance in km: "))

    if choose == "bike":
        if km in range(1, 9):
            price = km * 5
            print(f"You are charged {price} rupees")

        elif km in range(10, 16):
            price = (km - 8) * 6 + 64
            print(f"You are charged {price} rupees")

        elif km in range(16, 25):
            price = (km - 8) * 10 + 94
            print(f"You are charged {price} rupees")

        elif km in range(26, 30):
            price = (km - 8) * 15 + 169
            print(f"You are charged {price} rupees")

        elif km >= 30:
            print("No Ride")
            
    if choose == "auto":
        if km in range(1, 11):
            price = km * 8
            print(f"You are charged {price} rupees")

        elif km in range(12, 20):
            price = (km - 10) * 10 + 80
            print(f"You are charged {price} rupees")

        elif km in range(20, 36):
            price = (km - 10) * 12 + 180
            print(f"You are charged {price} rupees")

        elif km in range(36, 60):
            price = (km - 10) * 15 + 340
            print(f"You are charged {price} rupees")

        elif km >=60:
            print("No Ride")
            
    if choose == "car":
        if km in range(1, 51):
            price = km * 12
            print(f"You are charged {price} rupees")

        elif km in range(51, 81):
            price = (km - 8) * 15 + 600
            print(f"You are charged {price} rupees")

        elif km in range(81, 120):
            price = (km - 8) * 17 + 1050
            print(f"You are charged {price} rupees")

        elif km in range(120, 200):
            price = (km - 8) * 18 + 1730
            print(f"You are charged {price} rupees")

        elif km >=200:
            print("No Ride")
else:
    print("Invalid vehicle")