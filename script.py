#Create a Menu Class 
class Menu:
  
  #First Constructor 
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  #Constructor to print info
  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + " - " + str(self.end_time) + "."

#Method to calculate bill 
  def calculate_bill(self, purchased_items):
    total_bill = 0
    for i in purchased_items:
       total_bill += self.items.get(i, 0)
    return total_bill 

#Menus listed out -- I defined the menu items in a variable to make it easier to read. Menu is created on second line of each menu

#Brunch  
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("Brunch", brunch_items, 11, 16)
print(brunch)

#Early Bird
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("Early Bird", early_bird_items, 15, 18)

#Dinner
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("Dinner", dinner_items, 17, 23)

#Kids
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids", kids_items, 11, 21)

#Test Print
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


#Create a franchise class
class Franchise:
  
  #First Constructor
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  #Print Contructor 
  def __repr__(self):
    return "Come join us at: " + self.address

#Available menus method based on time
  def available_menus(self, time):
    menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menu_list.append(menu)
    return menu_list

#Create franchises -- I defined address in a variable and then injected that variable into Franchise class to make it easier to read franchise is created on second line

#flagship
og_address = "1232 West End Road"
flagship_store = Franchise(og_address, [brunch, early_bird, dinner, kids])

#new installment
new_address = "12 East Mulberry Street"
new_installment = Franchise(new_address, [brunch, early_bird, dinner, kids])

#Test Print
print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))


#Creating Businesses
class Business:
  #First Constructor
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#Create initial Business
first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#Building a Business from scratch

#Items on menu
arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

#Creating menu 
arepas_menu = Menu('Arepas', arepas_items, 10, 20)

#Franchise Address
arepas_address = '189 Fitzgerald Avenue'

#Creating franchise
arepas_place = Franchise(arepas_address, [arepas_menu])

#Creating business with franchise information
new_business = Business("Take a' Arepa", [arepas_place])

#Test print
print(new_business.name)
print(new_business.franchises[0])