# Python List Manager

A command-line to-do list manager built with Python functions and lists, for the CodeMore Python Programming Internship (Week 1, Task 2).

## Features

- Add, view, search and delete items
- Handles an empty list, empty input and invalid menu choices
- Functions are separated from the menu code and covered by unit tests

## Project Structure

```
python-list-manager/
├── README.md
├── src/
│   ├── main.py      # interactive menu
│   └── utils.py     # list functions
├── docs/
│   └── explanation.md
└── tests/
    └── test_utils.py
```

## Requirements

- Python 3.8 or newer. No external libraries.

## Setup and How to Run

```bash
git clone https://github.com/kavya-n-biradar/python-list-manager.git
cd python-list-manager
python src/main.py
```

Choose an option from the menu: `1` Add, `2` View, `3` Search, `4` Delete, `5` Exit.

## Run the Tests

```bash
python -m unittest discover tests
```

## Documentation

See [`docs/explanation.md`](docs/explanation.md) for the list operations used and a log of the program running.

## What I Learned

- How to write functions with parameters, return values and docstrings
- How to use list methods such as `append`, `pop` and list comprehensions
- How to keep logic in `utils.py` and user interaction in `main.py`
- How to handle edge cases and write simple unit tests

## Author

Kavya Biradar