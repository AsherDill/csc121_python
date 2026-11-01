# imports
import csv



def dashboard():
    """Prints  
    40 '='
      📚  YOUR LIBRARY
    40 '='
    """

    print("="*40)
    print("📚  YOUR LIBRARY")
    print("="*40)

    print()



def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour. 
    This number should be rounded to 1 decimal place"""
    # your code here
    Rtime = pages/40
    Rtime = round(Rtime, 1)
    return(Rtime, "hours")



def load_books():
    """
    Read every book saved in books.csv and return them as a list of dictionaries.
    """
    # create an empty list called library
    library = []

    # open "books.csv" using with ... as file:
    with open("books.csv") as file:

        # create a variable called reader that holds csv.DictReader(file)
        reader = csv.DictReader(file)

        # for each row in reader:
        for row in reader:

            # create a dictionary called book:
            book = {
                        "title" : row["title"],
                        "author": row["author"],
                        "pages" : row["pages"],
                        "hours" : row["hours"]
                    }
            #     "title"  -> row["title"]
            #     "author" -> row["author"]
            #     "pages"  -> row["pages"] converted with int()
            #     "hours"  -> row["hours"] converted with float()

            # append book to library
            library.append(book)

    # return library
    return library



def format_book(book, number):
    """
    Return one book as a numbered line of text.
    """
    return f"{number}. '{book["title"]}' - {book["author"]} ({book["pages"]} pages - approx. {book["hours"]} to read)"
    #ex  1. 'Dune' - Frank Herbert (412 pages - approx. 10.3 hours to read


    # return an f-string using number, book["title"], book["author"],
    # book["pages"], and book["hours"] in the format shown above



def add_book(library):
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time
    """
    
    # get user input
    title = input("Book title: ")
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)

    # --- New this week ---
        # open "books.csv" in append mode using with ... as file:
    
    with open("books.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["title","author","pages","hours"])
        writer.writerow({"title": title,"author": author,"pages": pages,"hours": hours})
    
        # create a variable called writer that holds a csv.DictWriter
        #     pass in the file and fieldnames=["title", "author", "pages", "hours"]
        # use writer.writerow() to write the book dictionary to the file
    

    # saves as dictionary
    book = {
            "title": title,
            "author": author,
            "pages": pages,
            "hours": hours
        }

    #adds to list
    library.append(book)

    print()
    print("Book added: ", "\n")
    print(f"'{title}' - {author} ({pages} pages - aprox. {hours} to read)")



def view_books(library):
    """Print every book in library with a number in front, or a message if it's empty."""
    
        # print the value returned from format_book(library[i], i + 1)

    print()

    if len(library) > 0:
        for i in range(len(library)):
            book = library[i]
            num = i + 1
            print(format_book(book, num))
            #print(f"{i+1}. '{library[i]["title"]}' - {library[i]["author"]} ({library[i]["pages"]} pages - aprox. {library[i]["hours"]} to read")
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
    '''
    instead of:  create an empty list with the name library
    now:         set library equal to the list returned from load_books()

    call the function to show the dashboard

    the menu loop stays exactly the same as Assignment 4
    '''

    dashboard()

    library = load_books()

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
