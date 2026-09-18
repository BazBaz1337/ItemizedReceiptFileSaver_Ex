#Input validation function
#only takes integer and will print a ValueError exception if prompt is not an integer
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Please enter a valid number.")
        except ValueError:
            print("Please enter a numeric value.")
#main run
def main():
        print("=== Exercise 2 : Itemized Receipt Splitter ===")
        #Get participants
        #create a list to store participants names
        names = input("\nEnter names separated by a comma: ")
        name_list = [name.strip() for name in names.split(",")if name.strip()]
        if not name_list:
            print("No names entered. Exiting.")
            return
        #Get ordered Items
        #create a dictionary to store ordered items and its prices
        ordered_items = []
        while True:
            items = input("\nEnter items name (or 'done' to finish): ").strip()
            if items.lower() == "done":
                break
            price = get_positive_float(f"Enter price {items} $")
            ordered_items.append({"item": items, "price": price})
        if not ordered_items:
            print("No items entered. Exiting.")
            return

        #print(name_list + ordered_items) #test code
if __name__ == "__main__":
    main()