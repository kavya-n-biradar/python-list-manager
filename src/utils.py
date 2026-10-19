"""Utility functions for managing a to-do list stored as a Python list."""


def add_item(items, item):
    """Add a non-empty item to the list.

    Args:
        items (list): The list to add the item to.
        item (str): The item to add.

    Returns:
        bool: True if the item was added, False if it was empty.
    """
    item = item.strip()
    if not item:
        return False
    items.append(item)
    return True


def remove_item(items, position):
    """Remove the item at a 1-based position.

    Args:
        items (list): The list to remove the item from.
        position (int): The position shown to the user, starting at 1.

    Returns:
        str or None: The removed item, or None if the position is invalid
        or the list is empty.
    """
    if not 1 <= position <= len(items):
        return None
    return items.pop(position - 1)


def search_items(items, keyword):
    """Find items that contain a keyword, ignoring upper/lower case.

    Args:
        items (list): The list to search.
        keyword (str): The text to look for.

    Returns:
        list: All matching items. Empty if there is no match or the
        keyword is empty.
    """
    keyword = keyword.strip().lower()
    if not keyword:
        return []
    return [item for item in items if keyword in item.lower()]


def format_list(items):
    """Return the list as a numbered string.

    Args:
        items (list): The list to format.

    Returns:
        str: One numbered item per line, or a message if the list is empty.
    """
    if not items:
        return "The list is empty."
    lines = [f"{number}. {item}" for number, item in enumerate(items, start=1)]
    return "\n".join(lines)


def display_items(items):
    """Print the current list in a numbered format.

    Args:
        items (list): The list to display.
    """
    print(format_list(items))