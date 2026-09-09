def dashboard():
    """Prints  
    40 '='
      📚  YOUR LIBRARY
    40 '='
    """
    # your code here
    # to do this without for loops print("================================================") 
    
    for i in range (40):
        print("=", end="")
    print()

    print("📚  YOUR LIBRARY")

    for i in range (40):
        print("=", end="")
    print()

# funtion name should be shorter
def estimate_reading_time(pages):
    """Return estimated reading time in hours, assuming 40 pages/hour. 
    This number should be rounded to 1 decimal place"""
    # your code here
    # shold convert to float first
    Rtime = pages/40
    # maby round
    return(Rtime, "hours")


def add_book():
    """
    This function takes in user input for title, author, and page count.
    Create a variable called hours that calls the function estimate_reading_time
    """

    # your code here
    # should be list
    # get user input in title case for "Book title: "
    title = input("Book title: ")
    # get user input for "Author: "
    author = input("Author: ")
    # get user input as an int for "Page count: " 
    pages = int(input("Page count: "))
    # call estimate_reading_time by passing in pages
    hours = estimate_reading_time(pages)
    # use an f-string to print "'{title}' by {author} -- approx. {hours} to read"
    print()
    print("Book added: ", "\n")
    # print("'", title, "'", " by ", author, " -- aprox. ", hours, " to read", sep="")
    print(f"'{title}' by {author} -- aprox. {hours} to read")


def main():
    dashboard()
    # should be in a while loop
    add_book()


if __name__ == "__main__":
    main()
