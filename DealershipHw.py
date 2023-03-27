class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print("Starting engine...")
        self.engine_on = True

    def make_noise(self):
        print("mmmmmmmmmmmm!")


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)





class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("Vroom vroom!")


bikes = [Motorcycle("Harley Davidson", 5000, 10000, 120),
         Motorcycle("Honda", 10000, 5000, 90),
         Motorcycle("Kawasaki", 8000, 7000, 110)]

trucks = [Truck("Ford", 20000, 20000),
          Truck("Chevrolet", 15000, 15000),
          Truck("Dodge", 18000, 18000)]

vehicles_to_compare = []
print('Welcome to GC Bikes and Trucks!')
while True:
    print("Please choose a category to view (type 'bikes' or 'trucks', or 'done' to compare/purchase):")
    selection = input().lower()

    if selection == "bikes":
        print("Here are the available bikes:")
        for i, bike in enumerate(bikes):
            print(f"{i + 1}. {bike.make} ({bike.miles} miles, ${bike.price}, the top speed is: {bike.top_speed})")

    elif selection == "trucks":
        print("Here are the available trucks:")
        for i, truck in enumerate(trucks):
            print(f"{i + 1}. {truck.make} ({truck.miles} miles, ${truck.price})")

    elif selection == "done":
        break

    else:
        print("Invalid selection. Please try again.")
        continue

    print("Enter the number of a vehicle to add it to your comparison list, or enter 'done':")
    while True:
        add_selection = input().lower()

        if add_selection == "done":
            break

        try:
            index = int(add_selection) - 1
            if selection == "bikes":
                vehicle = bikes.pop(index)

            else:
                vehicle = trucks.pop(index)
            vehicles_to_compare.append(vehicle)
            print(f"Added {vehicle.make} to your comparison list.")
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")
            continue

print("Here are the vehicles you have selected to compare:")
for vehicle in vehicles_to_compare:
    print(f"{vehicle.make} ({vehicle.miles} miles, ${vehicle.price})")
    vehicle.start_engine()
    vehicle.make_noise()

print("Would you like to purchase one of these vehicles? (y/n)")
purchase_selection = input().lower()

if purchase_selection == "y":
    print("Which vehicle would you like to purchase? (enter the number)")
    while True:
        purchase_index = input()
        try:
            index = int(purchase_index) - 1
            vehicle = vehicles_to_compare[index]
            print(f"You have purchased the {vehicle.make} for ${vehicle.price}. Congratulations!")
            break
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")
            continue
