# Global list representing the plate stack
plate_stack = []

# https://dev-10.teachable.com/courses/python-basics/lectures/50942528

# Function to add a plate to the top of the stack
def add_plate():
    plate_size = int(input("Enter the size of the plate to add: "))

    if plate_size <= 0:
        print("Warning: Plate size must be a positive integer.")
        return

    # If the stack is empty, add the plate
    if not plate_stack:
        plate_stack.append(plate_size)
    # Check if the plate is smaller than or equal to the top plate
    elif plate_size <= plate_stack[-1]:
        plate_stack.append(plate_size)
    else:
        print("Warning: Cannot place a larger plate on top of a smaller plate.")

# Function to print the plates in the stack
def print_plates():
    if not plate_stack:
        print("The plate stack is empty.")
    else:
        print("Plate stack (from top to bottom):")
        for plate in reversed(plate_stack):
            print(f"Plate size: {plate}")

# Function to remove a given number of plates from the top of the stack
def remove_plates():
    num_plates = int(input("Enter the number of plates to remove: "))

    if num_plates <= 0:
        print("Warning: Number of plates must be a positive integer.")
        return

    if num_plates > len(plate_stack):
        print("Warning: Cannot remove more plates than are in the stack.")
    else:
        for _ in range(num_plates):
            removed_plate = plate_stack.pop()
            print(f"Removed plate of size: {removed_plate}")

# Main function to run the menu
def main():
    while True:
        print("\nMenu:")
        print("1. Add a plate")
        print("2. Print plates")
        print("3. Remove plates")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_plate()
        elif choice == '2':
            print_plates()
        elif choice == '3':
            remove_plates()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select from the menu.")

# Run the program
if __name__ == "__main__":
    main()
