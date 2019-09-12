# Command Line Todo List

```
Usage: todo [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add     Add an item to the end of the list: `todo add "item text"`
  edit    Edit the text of an item: `todo edit 5 "new text"`
  init    Initialize list, only run this once
  list    List all todo items in order
  move    Move an item up or down the list: `todo move 4 up`
  remove  Remove an item by number: `todo remove 5`
```

## Installation

Prerequesite: python3

1. Download `todo.py`
2. Place it on your path
   * Optionally, rename it to `todo`
3. Make it executable
4. Run `todo.py init`
   * Or `todo init` if you have renamed the file
  
