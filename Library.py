import os
import mysql.connector

# classes


class ViewOrder:
    def __init__(self, orderID, staffID, staffFName, staffLName, memberID, memberFName, memberLName, bookIsbn, bookTitle, bookAuthor, rentDate, dueDate, status, returnDate):
        self.orderID = orderID
        self.staffID = staffID
        self.staffFName = staffFName
        self.staffLName = staffLName
        self.memberID = memberID
        self.memberFName = memberFName
        self.memberLName = memberLName
        self.bookIsbn = bookIsbn
        self.bookTitle = bookTitle
        self.bookAuthor = bookAuthor
        self.rentDate = rentDate
        self.dueDate = dueDate
        self.status = status
        self.returnDate = returnDate

################################################################
# Function
################################################################
# Database Function


# return dbcursor.fetchall()
def search_using_keywords_MySQL(inputString, attribute, table):
    # Extract keywords
    keywords = inputString.split(" ")

    # Build SQL to search
    sql = f"SELECT * FROM {table} WHERE "
    for i in range(len(keywords)):
        if i == 0:
            sql += f"{attribute} LIKE '%" + keywords[i] + "%'"
        else:
            sql += f" OR {attribute} LIKE '%" + keywords[i] + "%'"

    # Execute the SQL
    dbcursor.execute(sql)

    # Return Fetchall result from SQL
    return dbcursor.fetchall()


def search_using_keywords_MySQL_selective_attribute(inputString, attribute, table, atributesToShow):
    # Extract keywords
    keywords = inputString.split(" ")

    # Build SQL to search
    sql = f"SELECT {atributesToShow} FROM {table} WHERE "
    for i in range(len(keywords)):
        if i == 0:
            sql += f"{attribute} LIKE '%" + keywords[i] + "%'"
        else:
            sql += f" OR {attribute} LIKE '%" + keywords[i] + "%'"

    # Execute the SQL
    dbcursor.execute(sql)

    # Return Fetchall result from SQL
    return dbcursor.fetchall()


def connect_to_database():  # Return VOID
    global db
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="3020",
        database="librarydatabase"
    )

    # Create a cursor object to execute SQL queries
    global dbcursor
    dbcursor = db.cursor()

# Login Section
################################################################


def welcome_window():  # RETURN VOID
    os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN

    print("Welcome to CodeX Library")
    print("Choose your login as:")
    print("1. Member")
    print("2. Staff")
    print("3. Admin")

    # Choose Tittle
    choice = input("Please ENTER your choice: ")
    while (True):
        if ("1" <= choice <= "3" and len(choice) == 1):
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN
            print("Choose your login as:")
            print("1. Member")
            print("2. Staff")
            print("3. Admin")
            print("You Have Enter INVALID Value!")
            choice = input("Please RE-ENTER your choice: ")

    # Assign tittle
    global title
    if choice == "1":
        title = "Member"
    if choice == "2":
        title = "Staff"
    if choice == "3":
        title = "Admin"


def check_login(email, password):  # RETURN True or False

    # Execute the SELECT query to check if the email and password combination exists
    sql = f"SELECT * FROM {title} WHERE email = %s AND password = %s"

    # parameters = (email, password)
    parameters = (email, password)
    dbcursor.execute(sql, parameters)

    # Fetch the result of the query
    result = dbcursor.fetchone()

    global currID

    # Check if the result is not None (i.e., the email and password combination exists)
    if result is not None:
        currID = result[0]
        return True
    else:
        return False


def login_UI():  # return
    os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN

    print(f"Please ENTER E-Mail and Password to login as {title}")

    email = input("E-Mail: ")
    password = input("Password: ")
    while True:
        if check_login(email, password):
            os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN
            print("Login Successfull")
            print("Press ENTER to continue ...")
            input
            break
        else:
            os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN
            print("Email and Password is INVALID")
            print(f"Please Re-Enter E-Mail and Password to login as {title}")
            email = input("E-Mail: ")
            password = input("Password: ")
################################################################

# Member UI & Function
################################################################


# Search_book Menu
###################################################################################################
def search_book_by_title():
    os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN

    # Input bookTitle
    bookTitle = input("Search book title: ")

    results = search_using_keywords_MySQL(bookTitle, "title", "book")
    if len(results) > 0:
        for book in results:
            print(book)
        input("Press ENTER to back to Search MENU")
    else:
        print("No books found with title:", bookTitle)
        input("Press ENTER to back to Search MENU")


def search_book_by_isbn():
    os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN

    # Input ISBN
    isbn = input("Search book ISBN: ")

    # Fetch the result of the query
    results = search_using_keywords_MySQL(isbn, "isbn", "Book")
    if len(results) > 0:
        for book in results:
            print(book)
        input("Press ENTER to back to Search MENU")

    else:
        print("No books found with ISBN:", isbn)
        input("Press ENTER to back to Search MENU")


def display_search_book_menu():
    os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN
    print("Search book by: ")
    print("1. Title")
    print("2. ISBN")
    print("(Enter '-1' to BACK)")


def search_book():
    while True:
        display_search_book_menu()
        choice = input("ENTER your action: ")
        while (True):
            if ("1" <= choice <= "2" and len(choice) == 1) or choice == "-1":
                if choice == "-1":
                    break
                if choice == "1":
                    search_book_by_title()
                    break
                if choice == "2":
                    search_book_by_isbn()
                    break
            else:
                display_search_book_menu()
                print("!!!You Have Enter INVALID Value!!!")
                choice = input("RE-ENTER your action: ")
        if choice == "-1":
            break
###################################################################################################


# view_your_Order Menu
###################################################################################################
def display_view_order_menu():
    os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN

    results = search_using_keywords_MySQL_selective_attribute(
        currID, "memberID", "`order`", "orderID, isbn, status")
    if len(results) > 0:
        for order in results:
            print(order)

    else:
        print("No orders found")

    print("Enter orderID to view detail")
    print("(Enter '-1' to LOG OUT)")


def view_order_detail(orderID):
    # Build SQL to search
    sql = f"""SELECT 
    o.orderID, 
    o.staffID, 
    s.fName AS staffFName, 
    s.lName AS staffLName, 
    o.memberID, 
    m.fName AS memberFName, 
    m.lName AS memberLName, 
    o.isbn, 
    b.title AS bookTitle, 
    b.author AS bookAuthor, 
    o.rentDate, 
    o.dueDate, 
    o.status, 
    o.returnDate
FROM 
    `Order` o 
    INNER JOIN Staff s ON o.staffID = s.staffID 
    INNER JOIN Member m ON o.memberID = m.memberID 
    INNER JOIN Book b ON o.isbn = b.isbn
    where orderID = {orderID}"""

    # Execute the SQL
    dbcursor.execute(sql)

    # Return Fetchall result from SQL
    result = (dbcursor.fetchone())
    order = ViewOrder(result[0], result[1], result[2], result[3], result[4], result[5], result[6],
                      result[7], result[8], result[9], result[10], result[11], result[12], result[13])
    os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN
    print(f"""OrderID: {order.orderID} Status: {order.status}
StaffID: {order.staffID}  Name: {order.staffFName} {order.staffLName}
MemberID: {order.memberID} Name: {order.memberFName} {order.memberLName}
Book ISBN: {order.bookIsbn}
Book Title: {order.bookTitle}
Book Author: {order.bookAuthor}
Rent Date: {order.rentDate}       Due Date: {order.dueDate}
Return Date: {order.returnDate}""")
    input("(Press ENTER to return)")


def view_your_order():
    while True:
        display_view_order_menu()

        # Make Choice
        choice = input("ENTER orderID: ")
        while (True):
            if ("000000" <= choice <= "999999" and len(choice) == 6) or choice == "-1":
                if choice == "-1":
                    break
                else:
                    view_order_detail(choice)
                    break
            else:
                # CLEAR SCREEN
                display_view_order_menu()
                print("!!!You Have Enter INVALID Value!!!")
                choice = input("RE-ENTER OrderID: ")
        if choice == "-1":
            break


###################################################################################################

def display_member_menu():
    os.system("cls" if os.name == "nt" else "clear")  # CLEAR SCREEN
    print("Member Menu:")
    print("1. Search Book")
    print("2. View Your Order")
    print("3. Edit Personal Information")
    print("(Enter '-1' to LOG OUT)")


def member_UI():
    while True:
        display_member_menu()
        # Make Choice
        choice = input("ENTER your action: ")
        while (True):
            if ("1" <= choice <= "3" and len(choice) == 1) or choice == "-1":
                if choice == "-1":
                    break
                if choice == "1":
                    search_book()
                    break
                if choice == "2":
                    view_your_order()
                    break
            else:
                display_member_menu()
                print("!!!You Have Enter INVALID Value!!!")
                choice = input("RE-ENTER your action: ")
        if choice == "-1":
            break


################################################################


# MAIN
connect_to_database()
welcome_window()
login_UI()
if title == "Member":
    member_UI()
# if title == "Staff":
    # staff_UI()
# if title == "Admin":
    # admin_UI()
