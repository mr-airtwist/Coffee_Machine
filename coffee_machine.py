def attention(x):
    print(f'Sorry, not enough {x}!')


class CoffeeMachine:
    def __init__(self):
        self.water = 0
        self.milk = 0
        self.coffee = 0
        self.cups = 0
        self.money = 0

    def first_fill(self):
        self.water += 400
        self.milk += 540
        self.coffee += 120
        self.cups += 9
        self.money += 550

    def remaining(self):
        return f'''The coffee machine has:
               {self.water} ml of water
               {self.milk} ml of milk
               {self.coffee} g of coffee beans
               {self.cups} disposable cups
               ${self.money} of money'''

    def fill(self):
        self.water += int(input('Write how many ml of water you want to add: '))
        self.milk += int(input('Write how many ml of milk you want to add: '))
        self.coffee += int(input('Write how many grams of coffee beans you want to add: '))
        self.cups += int(input('Write how many disposable cups you want to add: '))

    def buy(self, x):
        if x == '1':
            if self.water < 250:
                attention('water')
            elif self.coffee < 16:
                attention('coffee')
            elif self.cups < 1:
                attention('cups')
            else:
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                print('I have enough resources, making you a coffee!')
        elif x == '2':
            if self.water < 350:
                attention('water')
            elif self.milk < 75:
                attention('milk')
            elif self.coffee < 20:
                attention('coffee')
            elif self.cups < 1:
                attention('cups')
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
        elif x == '3':
            if self.water < 200:
                attention('water')
            elif self.milk < 100:
                attention('milk')
            elif self.coffee < 12:
                attention('coffee')
            elif self.cups < 1:
                attention('cups')
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                print('I have enough resources, making you a coffee!')
        else:
            print()

    def take(self):
        take_money = self.money
        self.money -= self.money
        return take_money


coffee_machine = CoffeeMachine()
coffee_machine.first_fill()
while True:
    print()
    action = input('Write action (buy, fill, take, remaining, exit): ')
    print()
    if action == 'buy':
        type_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
        coffee_machine.buy(type_coffee)
    elif action == 'fill':
        coffee_machine.fill()
    elif action == 'take':
        print(f'I gave you ${coffee_machine.take()}')
    elif action == 'remaining':
        print(coffee_machine.remaining())
    elif action == 'exit':
        break
