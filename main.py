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
def main():
    print("=== Exercise 2 : Itemized Receipt Splitter ===")
    #Get names and store in a list in nameList
    names = input("Please enter your names (seperated by commas): ")
    nameList = [name.strip() for name in names.split(',') if name.strip()]
    if not nameList:
        print("No participants entered. Exiting.")
        return
    #print(nameList) test nameList list array
    #Get items and prices of items and store in a dictionary orderedItems

    #Get tax% and tip%


if __name__ == "__main__":
    main()