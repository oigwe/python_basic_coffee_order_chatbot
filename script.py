# Main Function

def coffee_bot():

  print('Welcome to the cafe!')

  # Drink Size
  size = get_size()
  print("Size:", size, "\n")

  # Drink Type
  drink_type = get_drink_type()
  print("Drink Type: ", drink_type, "\n")

  # Drink Temperature
  drink_temp = hot_or_cold()
  print("Temperature: ", drink_temp, "\n")

  # Order Confirmation Message Template
  message = "\nAlright, that's a " + size + " " + drink_temp + " "+ drink_type

  # Milk Choice
  if drink_type == 'Latte':
    milk_option = order_latte()
    message += " made with " + milk_option
  
  # Order Confirmation Message
  print(message)

  # Customer Name
  name = input('\nCan I get your name please? \n>')

  # Order Status
  return 'Thanks, ' +  name + "! Your drink will be ready shortly."

# ----------------------------------------------

# Helper Functions

# Error Function
def print_message():
  return "\n I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response. \n>"


# Drink Size Function
def get_size():

  coffee_size_res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ').lower()
  
  if coffee_size_res == 'a':
    return 'Small'
  elif coffee_size_res == 'b':
    return 'Medium'
  elif coffee_size_res == 'c':
    return 'Large'
  else: 
    print(print_message())
    return get_size()


# Hot or Cold Function
def hot_or_cold():
  temperature_res = input('Would you like your drink hot or iced? \n[a] Iced \n[b] Hot \n>').lower()

  if temperature_res == 'a':
    return 'Iced'
  elif temperature_res == 'b': 
    return 'Hot'
  else:
    print(print_message())
    return hot_or_cold();

# Drink Type Function
def get_drink_type():
  
  drink_type_res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>').lower()

  if drink_type_res == 'a':
    return 'Brewed Coffee'
  elif drink_type_res == 'b':
    return 'Mocha'
  elif drink_type_res == 'c':
    return 'Latte'
  else: 
    print(print_message())
    return get_drink_type()


# Milk Option Function
def order_latte():

  milk_option_res = input('And what kind of milk would you like added to your latte? \n[a] 2% Milk \n[b] Non-Fat Milk \n[c] Soy Milk \n>').lower()

  if milk_option_res == 'a':
    return '2% Milk'
  elif milk_option_res == 'b':
    return 'Non-Fat Milk'
  elif milk_option_res == 'c':
    return 'Soy Milk'
  else: 
    print(print_message())
    return order_latte()

# Call coffee_bot()!

print(coffee_bot())