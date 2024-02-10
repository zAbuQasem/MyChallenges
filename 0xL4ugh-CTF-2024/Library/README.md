# Library [Hard]
## Description
Built a book library, however my friend says that I made a nasty mistake!

> Author: zAbuQasem


## Solution
This challenge features a [format string vulnerability](https://python-forum.io/thread-11421.html) in Python that could be used to add a book with the flag in the title, then using the search functionality to leak the flag using regex injection.

- Vulnerable Snippet
```py
 elif choice == "7":
            choice = console.input("\n[bold blue]Book Manager:[/bold blue]\n1. Save Existing\n2. Create new book\n[bold blue]Enter your choice (1-2): [/bold blue]")
            if choice == "1":
                title = console.input("[bold blue]Enter Book title to save: [/bold blue]").strip()
                file = SaveFile(library.display_books(title=title))
                save_book(file.file, content="Hello World")
            else:
                save_file = SaveFile()
                title = console.input("[bold blue]Enter book title: [/bold blue]").strip()
                author = console.input("[bold blue]Enter book author: [/bold blue]")
                isbn = console.input("[bold blue]Enter book ISBN: [/bold blue]")
                num_copies = int(console.input("[bold blue]Enter number of copies: [/bold blue]"))
                title = title.format(file=save_file) ####>>> HERE
                book = Book(title,author, isbn)
                isbn_to_book[isbn] = book
                library.add_book(book, num_copies)
                save_book(title)
```
