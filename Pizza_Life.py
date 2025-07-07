import random
import time

class PizzaMan:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.energy = 100
        self.orders_completed = 0

    def take_order(self):
        if self.energy < 10:
            print("You're too tired to take more orders.")
            return False
        print("\nA customer wants to order a pizza.")
        choice = input("Do you accept the order? (y/n): ").strip().lower()
        if choice == 'y':
            print("Order accepted!")
            return True
        else:
            print("Order declined.")
            self.energy -= 5
            return False

    def make_pizza(self):
        print("Making pizza...")
        time.sleep(1)
        success = random.choice([True, True, True, False])  # 75% chance of success
        if success:
            print("Pizza made successfully!")
            self.energy -= 15
            return True
        else:
            print("You burned the pizza! No money for this order.")
            self.energy -= 15
            return False

    def deliver_pizza(self):
        print("Delivering pizza to customer...")
        time.sleep(1)
        tip = random.randint(3, 10)
        print(f"Pizza delivered! You earned $15 and got a tip of ${tip}.")
        self.money += 15 + tip
        self.energy -= 15
        self.orders_completed += 1

    def rest(self):
        print("Taking a break...")
        time.sleep(1)
        self.energy = min(100, self.energy + 30)
        print("You feel refreshed!")

    def status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Money: ${self.money}")
        print(f"Energy: {self.energy}/100")
        print(f"Orders completed: {self.orders_completed}")
        print("-------------------------")


def main():
    print("Welcome to Pizza Man: A Day in the Life!")
    name = input("What's your name, Pizza Man? ")
    hero = PizzaMan(name)

    for hour in range(9, 18):  # 9 AM to 5 PM
        print(f"\nIt is now {hour}:00.")
        hero.status()
        if hero.energy < 20:
            print("You look tired. Maybe take a break?")
            hero.rest()
            continue

        if hero.take_order():
            if hero.make_pizza():
                hero.deliver_pizza()
        # Random event
        if random.random() < 0.2:
            print("Unexpected rush! You get an extra order but lose more energy.")
            hero.energy -= 10

    print("\nThe workday is over!")
    hero.status()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
