#Input validation function
#only takes integer and will print a ValueError exception if prompt is not an integer
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a numeric value.")

#main run
while True:
        print("=== Exercise 2 : Itemized Receipt Splitter ===")
        #create a list to store participants names
        user_input = input("\nEnter participant names (separated by commas):")
        name_list = [name.strip() for name in user_input.split(",")]
        #create a dictionary to contain all ordered items
        ordered_items = {}

        while True:
            user_input = input("\nEnter item name (or 'done' to finish):").strip()
            if user_input.lower() == "done":
                print("continue")

                break
        break