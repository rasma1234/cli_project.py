warehouse1 = ["Brand new laptop", "Exceptional monitor", "Cheap tablet", "Funny laptop", "Second hand smartphone", "Brand new smartphone", "Cheap router", "Second hand laptop", "Elegant tablet", "Funny tablet", "Second hand headphones", "Exceptional tablet", "Brand new smartphone", "Cheap mouse", "Elegant headphones", "Brand new headphones", "Second hand smartphone", "High quality smartphone", "Brand new keyboard", "Second hand headphones", "Elegant router", "Exceptional router", "Second hand smartphone", "Exceptional monitor", "Almost new tablet", "High quality monitor", "Second hand monitor", "Brand new keyboard", "Almost new keyboard", "High quality headphones", "Elegant laptop", "Elegant router", "Almost new monitor", "Almost new headphones", "Second hand keyboard", "Brand new tablet", "Elegant laptop", "Almost new keyboard", "Exceptional router", "High quality keyboard", "Exceptional router", "Elegant router", "Cheap keyboard", "High quality monitor", "High quality keyboard", "Funny keyboard", "Cheap mouse", "Cheap monitor", "Funny headphones", "Elegant mouse", "Cheap smartphone", "High quality mouse", "Funny keyboard", "Second hand monitor", "Almost new router", "Almost new mouse", "Elegant smartphone", "Second hand router", "Second hand mouse", "Second hand tablet", "Exceptional tablet", "High quality smartphone", "Brand new headphones", "Exceptional monitor", "Elegant mouse", "Cheap laptop", "High quality smartphone", "Cheap monitor", "Funny monitor", "Almost new mouse", "Elegant headphones", "Cheap mouse", "Exceptional smartphone", "Cheap monitor", "Exceptional tablet", "Almost new tablet", "Second hand headphones", "Cheap tablet", "Elegant mouse", "Second hand mouse", "Cheap laptop", "Cheap keyboard", "Elegant router", "Elegant headphones", "Second hand monitor", "Funny router", "Elegant mouse", "Elegant headphones", "Brand new mouse", "Exceptional tablet", "Funny router", "Second hand headphones", "Brand new laptop", "Second hand router", "Cheap mouse", "Funny keyboard", "Elegant headphones", "Brand new laptop", "Elegant laptop", "Second hand mouse"]
warehouse2 = ["High quality tablet", "Second hand headphones", "Second hand laptop", "Exceptional tablet", "Exceptional headphones", "Brand new smartphone", "Elegant laptop", "High quality tablet", "Brand new headphones", "Exceptional mouse", "Cheap mouse", "Cheap headphones", "High quality headphones", "Brand new keyboard", "Brand new smartphone", "Almost new mouse", "Second hand router", "High quality monitor", "High quality smartphone", "Second hand headphones", "Elegant monitor", "High quality mouse", "Almost new keyboard", "Exceptional headphones", "High quality smartphone", "Exceptional smartphone", "High quality tablet", "Cheap mouse", "Cheap monitor", "Funny monitor", "Elegant monitor", "Funny smartphone", "Second hand mouse", "Almost new headphones", "Cheap headphones", "High quality router", "Exceptional keyboard", "Funny keyboard", "Exceptional laptop", "Cheap keyboard", "Second hand mouse", "Elegant router", "Cheap router", "Funny mouse", "Funny laptop", "Elegant tablet", "Exceptional mouse", "Funny headphones", "Elegant tablet", "Second hand laptop", "Brand new headphones", "Second hand headphones", "Cheap router", "Exceptional mouse", "Elegant router", "Exceptional monitor", "Exceptional keyboard", "Funny headphones", "Second hand headphones", "Almost new router", "Brand new tablet", "Funny mouse", "Elegant mouse", "High quality router", "Second hand keyboard", "Second hand router", "Brand new monitor", "Funny mouse", "Funny tablet", "Elegant keyboard", "Cheap router", "Funny router", "Second hand monitor", "Elegant smartphone", "Brand new monitor", "Second hand monitor", "Second hand keyboard", "Cheap mouse", "Brand new keyboard", "Exceptional mouse", "Elegant router", "Brand new mouse", "Exceptional keyboard", "Elegant smartphone", "Exceptional tablet", "Second hand keyboard", "Almost new headphones", "Brand new tablet", "Brand new tablet", "Exceptional headphones", "Funny smartphone", "Funny smartphone", "Second hand tablet", "Cheap router", "Almost new keyboard", "Elegant router", "Brand new tablet", "High quality tablet", "Almost new router", "High quality monitor"]

user_name = input("What is your user_name? ")
print((f" Hello, {user_name}! \n What would you like to do? \n 1. list items by warehouse \n 2. search an item and place an order \n 3. Quit "))

user_option = input("Type the number of the operation: ")

if user_option == "1":
    print("Items in warehouse 1: ")
    for item in warehouse1:
        print("-", item)
    print("Items in warehouse 2: ")
    for item in warehouse2:
        print("-", item)
    exit()

elif user_option == "2":
    user_search = input("What is the name of the item? ")
elif user_option == "3": 
    print("Thank you for your visit", user_name)
else:
    print("******************************************")
    print(user_option, "Is not a valid operation.")
    print("******************************************")
    print("Thank you for your visit", user_name)
    exit()
both_warehouses = warehouse1 + warehouse2
item_available = both_warehouses.count(user_search)
print("Amount available: ", item_available)


w1 = user_search in warehouse1
w2 = user_search in warehouse2
if w1 and w2:
    print("Item found in both warehouses")
elif w1:
    print("Item found in warehouse 1")
elif w2:
    print("Item found in warehouse 2")
else:
    print("Location not in stock.")
    print("Thank you for your visit", user_name)
    exit()

order = input("Would you like to order this item?(y/n)")
if order == "n":
    print("Thank you for your visit", user_name)
elif order == "y":
    desired_amount = int(input("How many would you like? "))
    
if desired_amount > item_available:
    print("There are not this many available. The maximum amount that can be ordered is ", item_available )

    max_order = input("Would you like to order the maximum available?(y/n) ")

    if max_order == "y":
        print(item_available, user_search, "have been ordered.")
        print("Thank you for your visit", user_name)
    elif max_order == "n":
        print("Thank you for your visit", user_name)

