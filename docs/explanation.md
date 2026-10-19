# List Operations Explanation

This project stores a to-do list in a Python list and manages it with functions in `src/utils.py`.

## List operations used

| Operation | Where | What it does |
|---|---|---|
| `list.append(item)` | `add_item` | Adds an item to the end of the list |
| `list.pop(index)` | `remove_item` | Removes the item at an index and returns it |
| `len(list)` | `remove_item` | Gives the number of items, used to check a position is valid |
| `enumerate(list, start=1)` | `format_list` | Gives each item with a number starting from 1 |
| List comprehension with `in` | `search_items` | Builds a new list of items containing a keyword |
| `"\n".join(lines)` | `format_list` | Joins the numbered lines into one string |

## How each function works

- **add_item:** strips spaces from the text and refuses empty input, so the list never holds blank items.
- **remove_item:** users count from 1, but lists count from 0, so it removes index `position - 1`. A position outside `1` to `len(items)` returns `None` instead of crashing.
- **search_items:** compares lowercase versions, so "buy" finds "Buy milk".
- **format_list / display_items:** show a numbered list, or "The list is empty." when there is nothing to show.

## Edge cases handled

- Empty list when viewing or deleting
- Empty item when adding
- Invalid menu choices (anything other than 1 to 5)
- Delete position that is not a number, or is out of range
- Search with no match, or with an empty keyword

## Program in action (text log)

```
PASTE YOUR OWN TERMINAL OUTPUT HERE
```

Screenshot: `screenshots/program_run.png`