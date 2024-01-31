#7.14
""" class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    triangle1.set_base(float(input()))
    triangle1.set_height(float(input()))

    triangle2.set_base(float(input()))
    triangle2.set_height(float(input()))
      
    print('Triangle with smaller area:')  

    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info()
    else:
        triangle2.print_info() """

#7.15
""" class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        return self.wins / (self.wins + self.losses)
    
    def print_standing(self):
        percent = self.get_win_percentage()
        print(f'Win percentage: {percent:.2f}')
        print(f'Congratulations, Team {self.name} has a winning average!') if percent > 0.5 else print(f'Team {self.name} has a losing average.')


if __name__ == "__main__":
    team = Team()
   
    user_name = input()
    user_wins = int(input())
    user_losses = int(input())
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    
    team.print_standing() """

#7.16
""" class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    vending = VendingMachine()
    # TODO: Purchase input number of drinks
    vending.purchase(int(input()))
    # TODO: Restock input number of bottles
    vending.restock(int(input()))
    # TODO: Report inventory
    vending.report() """