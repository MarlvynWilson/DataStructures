
#Cars avaulable at Marlvyn's Dealership and their various prices
cars={"Nissan Navara": 100000, "Nissan Patrol": 120000, "Nissan Altima": 70000,\
      "Lamborghini Gallardo":1000000, "Lamborghini Countach": 800000,\
      "Lamborghini Aventador": 900000, "Toyota Corolla": 80000, "Toyota Camry": 90000,\
      "Toyota Fortuner": 100000, "Toyota Hilux": 120000, "Toyota Yaris": 50000,\
      "Honda Accord": 90000, "Honda Civic": 80000, "Honda CRV": 110000,\
      "Ford Escape": 80000, "Ford Explorer": 100000, "Ford Fusion": 60000,"Ford Focus": 50000,\
      "Hyundai Elanta": 60000, "Hyundai SantaFe": 80000, "Hyundai Veloster": 60000,\
      "Mitsubishi Pajero": 90000, "Mitsubishi L300": 80000, "Bugatti Veyron": 1100000,\
      "Bugatti Chiron": 1200000," Tesla Model X": 140000, "Tesla Model Y": 160000,\
      "Tesla Model S": 150000, "Tesla Roadster": 180000, "Tesla Cybertruck": 220000}
carName = input("Enter the name of your preferred car:")
if carName in cars:
    print(carName,("is available"))
else:
    print(("Sorry,"),carName,("is not available"))
carPrice = cars[carName]
print(("The price of"),carName,("is $"),carPrice)