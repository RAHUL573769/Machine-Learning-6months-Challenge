class AtmMachine:
    def __init__(self):
        self.pin = 0
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi!!. how can I help you?
        1. Press 1 to create a PIN.
        2. Press 2 to change a Pin
        """)

        if (user_input == "1"):
            self.createpin()

    def createpin(self):
        user_pin = input("Enter your Pin")
        self.pin = user_pin
        user_balance = int(input("Enter your Balance"))
        self.balance = user_balance
        print(f'Your balanace is {self.balance} and Pin is {self.pin=}')
        self.menu()
