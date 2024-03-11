# QN: Kenya Power proposes the introduction of smart meters that identify gadgets 
# consuming the most power in homes. Write a python program for the meters.

# Import datetime to give real time accurate data
import datetime
current_timedate = datetime.datetime.now()
# Create a class kenya_power
class kpower:
    def __init__(self):
        # A dictionary to store registred users and their power consumption
        self.consumers = {
            "Rui": 3400,
            "Sonya": 5690,
            "Derrick": 2960.5,
        }
    # A function to register new consumers
    def register_consumer(self, name, current_balance=0):
        if name in self.consumers:
            print("Sorry! Consumer", name, "already registered as at: ", current_timedate)
        else:
            self.consumers[name] = current_balance
            print("Congratulations! Consumer", name, "has been registered successfully as at: ", current_timedate)
    # A function to record power consumption
    # To find the power consumption, the consumer's balance is divided by 655.56
    def power_consumption(self, name):
        if name not in self.consumers:
            print("Sorry! Consumer", name, "does not exit!")
        else:
            power = (self.consumers[name] / 655.56)
            print("The rate of power consumption for: ", name, "is", power, "kWh as at: ", current_timedate)
    # A function to calculate the cost of energy for a consumer
    def energy_cost(self, name):
        if name not in self.consumers:
            print("Sorry! Consumer", name, "does not exit!")
        else:
            print("The energy cost for consumer", name, "is: ", self.consumers[name], "as at: ", current_timedate)
    # A function to process the payment made by the consumer
    def payment_processing(self, name, paid_amount):
        if name not in self.consumers:
            print("Sorry! Consumer", name, "does not exit!")
        else:
            current_balance = self.consumers[name] - paid_amount
            print("Payment for consumer", name, "is successful! The new amount due is: ", current_balance, "as at: ", current_timedate)
            
# Instantiating
smart_meter =  kpower()

# A loop to keep the program running
while True:
    print("\nWelcome to smart meter (2.0)👋👦How may we help you?.")
    print("1. Register a consumer account.")
    print("2. Read consumer power consumption.")
    print("3. Check current energy cost.")
    print("4. Make a payment.")
    print("5. Exit")

# Prompt the user to choose one
    pick = input("Make your choice: ")

# An if statement to perform  an action corresponding to the consumer's choice

    if pick == '1':
        name = input("Please enter the consumer's name: ")
        smart_meter.register_consumer(name)
    elif pick in ['2', '3', '4']:
        name = input("Please enter the consumer's name: ")
        if name not in smart_meter.consumers:
            print("Sorry. Consumer account doesn't exist!")
        if pick == '2':
            smart_meter.power_consumption(name)
        elif pick == '3':
            smart_meter.energy_cost(name)
        elif pick == '4':
            amount = float(input("Enter amount you want to pay: "))
            smart_meter.payment_processing(name, amount)
    elif pick == '5':
        print("Thank you for using smart meter (2.0)! Come back soon👋🎉", current_timedate)
        break
    else:
         print("Invalid pick. Try again!")
            