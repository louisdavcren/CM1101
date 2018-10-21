# Imports


# Introduction (ready to play etc) ??
print("Press enter when you're ready to play")

# Items in inventory
def list_of_items(items):

    # Create a string of items
    string of items = ""
    for item in items:
        if item != items[len(items) -1]:
            string_of_items = string_of_items + item['name'] + ", "
        else:
            string_of_items = string_of_items + item['name']
    return string_of_items

# Items in the location
def print_location_items:

# Print location
def print_location(location):

    # Introduce location
    print("You're currently located in the " + location['name'] "...")
    # Describe location
    print(location["description"])
    print("")
    # Display items in location
    print_location_items(location)

# Available exits
def exits_leads_to(exits, direction):

    return locations[exits[direction]]['name']

# Valid exits
def is_valid_exit:

    return chosen_exit in exits

# Print exits
def print_exit(direction, leads_to):

    print("GO " + direction.upper() + " to " + leads_to + ".")

# Print menu
def print_menu(exits, location_items, inv_items):

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    # Item options
    for item in location_items:
        print("TAKE " + item['id'].upper() + " to take " + item['name'] + ".")
    for item in in_items:
        print("DROP " + item['id'].upper() + " to drop " + item['name'] + ".")

    print("What do you want to do?")
    
# Execute Functions
# Execute go
def execute_go(direction):
    
    global current_location
    current_location = move(current_location['exits'], direction)

# Execute take
def execute_take:

    found = False

    for item in current_location['items']:
        if item_id == item['id'] and inventory_mass(inventory) + item['mass'] <= mass_capacity :
            inventory.append(item)
            current_location['items'].remove(item)
            found = True
            print(item_id, " added to inventory")
# OPTIONAL - MASS CAPACITY FUNCTION 
        elif inventory_mass(inventory) + item['mass'] > mass_capacity :
            print("You've reach your maximum mass capacity")
            # Display mass status
            print("You're carrying", inventory_mass(inventory) + item['mass'], "kg, this is too much!")
            return
    # Necessary reject
    if found == False:
        print("You cannot take that.")

# Execute drop
def execute_drop(item_id):

    success = False
    for items in inventory:
        if item_id == items['id']:
            current_location['items'].append(items)
            inventory.remove(items)
            print(items['name'], "dropped")
            success = True
    if success == False:
        print("You cannot drop that item")
            

# Execute command
def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")

# Inventory mass
def inventory_mass(inventory):

    # Original mass
    x = 0

    # Adding mass to the inventory
    for item in inventory:
        x += item['mass']

    # Returning the new mass
    return x

# Menu
def menu(exits, location_items, inv_items):

    # Display menu
    print_menu(exits, location_items, in_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user=_input = normalise_input(user_input)

    # Return the input
    return normalise_user_input

# Move
def move(exits, direction):

    return locations[exits[direction]]


# MAIN FUNCTION
def main():

    while True:
        # Print status
        print_location(current_location)
        print_inventory_items(inventory)
        print_health(health)

        # Show possible actions
        command = menu(current_location['exits'], current_location['items'], inventory)

        # Execute the user's commands
        execute_command(command)

        # Game complete
        # Leah is safe -(with luke or solo)



        return False
        
        




