def dashboard():
    """Prints  
    40 '='
      📚  YOUR LIBRARY
    40 '='
    """

    for i in range (40):
        print("=", end="")
    print()

    print("📚  YOUR LIBRARY")

    for i in range (40):
        print("=", end="")
    print()

def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour. 
    This number should be rounded to 1 decimal place"""
    # your code here
    Rtime = pages/40
    Rtime = round(Rtime, 1)
    return(Rtime, "hours")


def add_book(library):
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time
    """
    # your code here
    # get user input in title case for "Book title: "
    title = input("Book title: ")
    # get user input for "Author: "
    author = input("Author: ")
    # get user input as an int for "Page count: " 
    pages = int(input("Page count: "))
    # call estimate_reading_time by passing in pages
    hours = estimate_reading_time(pages)
    # use an f-string to print "'{title}' by {author} -- approx. {hours} to read"
    book = {
            "title": title,
            "author": author,
            "pages": pages,
            "hours": hours
        }
    library.append(book)

    print()
    print("Book added: ", "\n")
    print(f"'{title}' - {author} ({pages} pages - aprox. {hours} to read)")

def view_books(library):
    print()

    if len(library) > 0:
        for i in range(len(library)):
          print(f"{i+1}. '{library[i]["title"]}' - {library[i]["author"]} ({library[i]["pages"]} pages - aprox. {library[i]["hours"]} to read")
    else:
        print("Your library is empty. Add a book first!")
    print()
    
def show_menu():
    print("1) View books")
    print("2) Add a book")
    print()
    print("q) Quit")
    option = input("> ")
    return option

def main():
    dashboard()
    library = []
    while True:
        option = show_menu()
        if option == "1":
            view_books(library)
        elif option == "2":
            add_book(library)
        else:
            option = option.lower()
            if option == "q" or option == "quit" or option == "exit":
                print("Goodbye!")
                break
            else:
                print("Sorry, that option isn't available.")
                print()


if __name__ == "__main__":
    main()
