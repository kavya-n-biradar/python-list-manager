"""Interactive command-line to-do list manager."""

from utils import add_item, display_items, remove_item, search_items

MENU = """
===== To-Do List Manager =====
1. Add item
2. View items
3. Search items
4. Delete item
5. Exit
"""


def read_number(prompt):
    """Ask the user for a whole number.

    Args:
        prompt (str): The message to show.

    Returns:
        int or None: The number entered, or None if it was not a number.
    """
    try:
        return int(input(prompt))
    except ValueError:
        return None


def handle_add(items):
    """Ask for an item and add it to the list."""
    item = input("Enter item: ")
    if add_item(items, item):
        print("Item added.")
    else:
        print("Item cannot be empty.")


def handle_search(items):
    """Ask for a keyword and show the matching items."""
    keyword = input("Search for: ")
    results = search_items(items, keyword)
    if results:
        print("Matches:")
        for result in results:
            print(f"- {result}")
    else:
        print("No matching items found.")


def handle_delete(items):
    """Show the list, ask which item to delete and remove it."""
    if not items:
        print("The list is empty. Nothing to delete.")
        return
    display_items(items)
    position = read_number("Enter the number of the item to delete: ")
    if position is None:
        print("Invalid input. Please enter a number.")
        return
    removed = remove_item(items, position)
    if removed is None:
        print("That number is not in the list.")
    else:
        print(f"Removed: {removed}")


def main():
    """Run the menu loop until the user chooses to exit."""
    items = []
    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            handle_add(items)
        elif choice == "2":
            display_items(items)
        elif choice == "3":
            handle_search(items)
        elif choice == "4":
            handle_delete(items)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()