import streamlit as st
import io
import sys
import time
import random
from contextlib import redirect_stdout, redirect_stderr
from streamlit_option_menu import option_menu




        
with st.sidebar:
    st.markdown("<h2 style='font-weight:bold; font-family:Verdana;font-size:40px;'>code_<span style='color:red;'>RED</span></h2>",unsafe_allow_html=True)

    data = option_menu(
        menu_title="Python Tutorial new",  
        options=["Python Introduction", "Variables", "Operators", "Data Types","String Method","Decision Making","Looping","Oops Concept","Python DSA","Python MYSQL","pratice","Quiz"]
    )

st.write(f"You selected: {data}")


if data == "Python Introduction":
    
    st.markdown(
    """
    <div style='display: flex; align-items: center; gap: 20px;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg' style='height: 100px;'/>
        <span style='font-size: 60px; font-weight: bold; font-family: Verdana;'> Introduction</span>
    </div>
    """,unsafe_allow_html=True)

    st.header("What is Python?")
    st.write("Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.")
    st.write("It is used for:")
    st.write("✅ web development (server-side),")
    st.write("✅ software development,")
    st.write("✅ mathematics,")
    st.write("✅ system scripting.")
    st.header("Why Python?")
    st.write("✅Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).")
    st.write("✅Python has a simple syntax similar to the English language.")
    st.write("✅Python has syntax that allows developers to write programs with fewer lines than some other programming languages.")
    st.write("✅Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.")
    st.write("✅Python can be treated in a procedural way, an object-oriented way or a functional way.")
    st.header("Python Syntax compared to other programming languages")
    st.write("✅Python was designed for readability, and has some similarities to the English language with influence from mathematics.")
    st.write("✅Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.")
    st.write("✅Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.")
    st.header("Python Install📤")
    st.write("Many PCs and Macs will have python already installed.")
    st.write("To check if you have python installed on a Windows PC, search in the start bar for Python or run the following on the Command Line (cmd.exe):")
    st.write(r"`C:\Users\Your Name>python --version`")
    st.write("To check if you have python installed on a Linux or Mac, then on linux open the command line or on Mac open the Terminal and type:")
    st.write(r"`python --version`")
    st.write("If you find that you do not have Python installed on your computer, then you can download it for free from the following website: https://www.python.org/")
    
elif data == "Variables":
    st.title("Python Variables")
    st.header("Variables")
    st.write("Variables are containers for storing data values.")
    st.header("Creating Variables")
    st.write("Python has no command for declaring a variable.")
    st.write("A variable is created the moment you first assign a value to it.")
    st.code("""
    x = 5
    y = "John"
    print(x)
    print(y)
    """,language="Python")
    st.write("Variables do not need to be declared with any particular type, and can even change type after they have been set.")
    st.write("## Example")
    st.code("""
    x = 4       # x is of type int
    x = "Sally" # x is now of type str
    print(x)
    """,language="Python")
    st.header("Case-Sensitive")
    st.write("Variable names are case-sensitive.")
    st.write("## Example")
    st.code("""
    a = 4
    A = "Sally"
    #A will not overwrite a
    """,language="Python")
elif data == "Operators":
    st.title("Python Operators")
    st.header("Python Operators")
    st.write("Operators are used to perform operations on variables and values.")
    st.write("In the example below, we use the + operator to add together two values:")
    st.write("## Example")
    st.code("""
    print(10 + 5)
    """)
    st.write("Python divides the operators in the following groups:")
    st.write("- Arithmetic operators")
    st.write("- Assignment operators")
    st.write("- Comparison operators")
    st.write("- Logical operators")
    st.write("- Identity operators")
    st.write("- Membership operators")
    st.write("- Bitwise operators")
    st.write("## Python Arithmetic Operators")
    st.write("### Arithmetic operators are used with numeric values to perform common mathematical operations:")
    st.write("#### Example:   `+ - * /  % ** //` ")
    st.write("## Python Assignment Operators")
    st.write("### Assignment operators are used to assign values to variables:")
    st.write("#### Example:   `== !> > < >= <=`")
    st.write("## Python Comparison Operators")
    st.write("### Comparison operators are used to compare two values:")
    st.write("#### Example:   `= += -= *= /= %= **= //= &= |= >>= <<=`")
    st.write("## Python Logical Operators")
    st.write("### Logical operators are used to combine conditional statements:")
    st.write("#### Example:   `AND OR NOT`")
    st.write("## Python Identity Operators")
    st.write("### Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:")
    st.write("#### Example:   ` IS ISNOT`")
    st.write("## Python Membership Operators")
    st.write("### Membership operators are used to test if a sequence is presented in an object:")
    st.write("#### Example:   `IN INNOT`")
    st.write("## Python Bitwise Operators")
    st.write("### Bitwise operators are used to compare (binary) numbers:")
    st.write("#### Example:   `& \ ^ ~ << >>`")
elif data == "Data Types":
    st.title("Python Data Types")
    st.header("Data Types")
    st.write("## Built-in Data Types")
    st.write("In programming, data type is an important concept.")
    st.write("Variables can store data of different types, and different types can do different things.")
    st.write("Python has the following data types built-in by default, in these categories:")
    st.write("- ### Text Type:	str")
    st.write("- ### Numeric Types:	int, float, complex")
    st.write("- ### Sequence Types:	list, tuple, range")
    st.write("- ### Mapping Type:	dict")
    st.write("- ### Set Types:	set, frozenset")
    st.write("- ### Boolean Type:	bool")
    st.write("- ### Binary Types:	bytes, bytearray, memoryview")
    st.write("- ### None Type:	NoneType")
    st.write("# Getting the Data Type")
    st.write("You can get the data type of any object by using the type() function:")
    st.write("Example")
    st.code("""
    x = 5
    print(type(x))
    """,language="Python")
    st.write("# Setting the Data Type")
    st.write("### Example")
    
    col1,col2 = st.columns(2)
    with col1:
        st.write(" `x = str('Hello World')`")
        st.write(" `x = int(20)`")
        st.write(" `x = float(20.5)`")
        st.write(" `x = complex(1j)`")
        st.write(" `x = list(('apple', 'banana', 'cherry'))`")
        st.write(" `x = tuple(('apple', 'banana', 'cherry'))`")
        st.write(" `x = range(6)`")
        st.write(" `x = dict(name='John', age=36)`")
        st.write(" `x = set(('apple', 'banana', 'cherry'))`")
        st.write(" `x = frozenset(('apple', 'banana', 'cherry'))`")  
        st.write(" `x = bool(5)`")   
        st.write(" `x = bytes(5)`")
        st.write(" `x = bytearray(5)`")
        st.write(" `x = memoryview(bytes(5))`")
    
    with col2:
        st.write("String")
        st.write("Integer")
        st.write("Float")
        st.write("Complex")
        st.write("List")
        st.write("Tuple")
        st.write("Range")
        st.write("Dictionary")
        st.write("Set")
        st.write("Frozenset")
        st.write("Boolean")
        st.write("Bytes")
        st.write("Bytearray")
        st.write("Memoryview")
elif data == "String Method":
    st.title("String Method")
    col1 = st.columns(1)[0]
    with col1:
        st.header("method")
        st.write("#### `capitalize()   : Converts the first character to upper case`")
        st.write("#### `casefold()     : Converts string into lower case`")
        st.write("#### `center()       : Returns a centered string`")
        st.write("#### `count()        : Returns the number of times a specified value occurs in a string`")
        st.write("#### `encode()       : Returns an encoded version of the string`")
        st.write("#### `endswith()     : Returns true if the string ends with the specified value `")
        st.write("#### `expandtabs()   : Sets the tab size of the string`")
        st.write("#### `find()         : Searches the string for a specified value and returns the position of where it was found`")
        st.write("#### `format()       : Formats specified values in a string`")
        st.write("#### `format_map()   : Formats specified values from a dictionary in a string`")
        st.write("#### `index()        : Searches the string for a specified value and returns the position of where it was found`")
        st.write("#### `isalnum()      : Returns True if all characters in the string are alphanumeric`")
        st.write("#### `isalpha()      : Returns True if all characters in the string are in the alphabet`")
        st.write("#### `isascii()      : Returns True if all characters in the string are ascii characters`")
        st.write("#### `isdecimal()    : Returns True if all characters in the string are decimals`")
elif data == "Decision Making":
    st.title("Condition")
    st.header("if Statement")
    st.write("Python supports the usual logical conditions from mathematics:")
    st.write("- Equals: a == b")
    st.write("- Not Equals: a != b")
    st.write("- Less than: a < b")
    st.write("- Less than or equal to: a <= b")
    st.write("- Greater than: a > b")
    st.write("- Greater than or equal to: a >= b")
    st.write("These conditions can be used in several ways, most commonly in 'if statements' and loops.")
    st.header("Example")
    st.code("""
    a = 33
    b = 200
    if b > a:
            print("b is greater than a")
    """,language="python")
    st.header("elif Statement")
    st.write("The elif keyword is Python's way of saying 'if the previous conditions were not true, then try this condition'.")
    st.header("Example")
    st.code("""
    a = 33
    b = 33
    if b > a:
            print("b is greater than a")
    elif a == b:
            print("a and b are equal")
    """,language="Python")
    st.header("else Statement")
    st.write("The else keyword catches anything which isn't caught by the preceding conditions.")
    st.header("Example")
    st.code("""
    a = 200
    b = 3
    if b > a:
            print("b is greater than a")
    elif a == b:
            print("a and b are equal")
    else:
            print("a is greater than b")
    """,language="Python")
    st.header("Nested if")
    st.write("You can have if statements inside if statements, this is called nested if statements.")
    st.header("Example")
    st.code("""
    x = 41
    if x > 10:
            print("Above ten,")
            if x > 20:
            print("and also above 20!")
    else:
            print("but not above 20.")
    """,language="Python")

elif data == "Looping":
    st.title("Python Looping")
    st.write("Python has two primitive loop commands:")
    st.write("- while loops")
    st.write("- for loops")
    st.header("While Looping")
    st.write("With the while loop we can execute a set of statements as long as a condition is true.")
    st.header("Example")
    st.code("""
    i = 1
    while i < 6:
      print(i)
      i += 1
     """,language="Python")
    st.header("For Looping")
    st.write("A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).")
    st.write("This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.")
    st.header("Example")
    st.code("""
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
            print(x)
     """,language="Python")
    st.title("Nested Looping")
    st.write("A nested loop is a loop inside a loop.")
    st.write("The 'inner loop' will be executed one time for each iteration of the 'outer loop':")
    st.header("Example")
    st.code("""
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    for x in adj:
            for y in fruits:
               print(x, y)

    """,language="Python")
    st.title("Pass Statement")
    st.write("for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.")
    st.header("Example")
    st.code("""
    for x in [0, 1, 2]:
            pass
    """,language="Python")
    st.title("Break Statement")
    st.write("With the break statement we can stop the loop before it has looped through all the items:")
    st.header("Example")
    st.code("""
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
            print(x)
            if x == "banana":
               break
    """,language="Python")

elif data == "Oops Concept":
    st.title("Opps")
    st.header("What is Opps")
    st.write("OOP stands for Object-Oriented Programming.")
    st.write("Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.")
    st.header("Advantages of OOP")
    st.write("- Provides a clear structure to programs")
    st.write("- Makes code easier to maintain, reuse, and debug")
    st.write("- Helps keep your code DRY (Don't Repeat Yourself)")
    st.write("- Allows you to build reusable applications with less code")
    st.write("Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.")
    st.header("Python Classes/Objects")
    st.write("Python is an object oriented programming language.")
    st.write("Almost everything in Python is an object, with its properties and methods.")
    st.write("A Class is like an object constructor, or a 'blueprint' for creating objects.")
    st.header("Example")
    st.code("""
    class MyClass:
            x = 5
    p1 = MyClass()
    print(p1.x)
    
    """,language="Python") 
    st.header("Python Inheritance")
    st.write("Inheritance allows us to define a class that inherits all the methods and properties from another class.")
    st.write("Parent class is the class being inherited from, also called base class.")
    st.write("Child class is the class that inherits from another class, also called derived class.")
    st.header("Example")
    st.code("""
    class Person:
            def __init__(self, fname, lname):
              self.firstname = fname
              self.lastname = lname
            def printname(self):
              print(self.firstname, self.lastname)
    x = Person("John", "Doe")
    x.printname()
    """,language="Python")
    st.header("Add the __init__() Function")
    st.write("So far we have created a child class that inherits the properties and methods from its parent.")
    st.write("We want to add the __init__() function to the child class (instead of the pass keyword).")
    st.header("Example")
    st.code("""
    class Student(Person):
            def __init__(self, fname, lname):
                Person.__init__(self, fname, lname)
    """,language="python")  
    st.header("Python Iterators")
    st.write("An iterator is an object that contains a countable number of values.")
    st.write("An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.")
    st.write("Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().")
    st.header("Example")
    st.code("""
    class MyNumbers:
            def __iter__(self):
              self.a = 1
              return self

            def __next__(self):
              x = self.a
              self.a += 1
              return x

    myclass = MyNumbers()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))

    """,language="Python")
    st.header("Python Polymorphism")
    st.write("The word 'polymorphism' means 'many forms', and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.")
    st.header("Function Polymorphism")
    st.write("An example of a Python function that can be used on different objects is the len() function.")
    st.header("Example")
    st.code("""
    class Car:
            def __init__(self, brand, model):
              self.brand = brand
              self.model = model

            def move(self):
              print("Drive!")

    class Boat:
            def __init__(self, brand, model):
              self.brand = brand
              self.model = model

            def move(self):
              print("Sail!")

    class Plane:
            def __init__(self, brand, model):
              self.brand = brand
              self.model = model

            def move(self):
              print("Fly!")

              car1 = Car("Ford", "Mustang")       #Create a Car object
              boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
              plane1 = Plane("Boeing", "747")     #Create a Plane object

             for x in (car1, boat1, plane1):
     x.move()
    """,language="Python")
elif data == "Python DSA":
    st.title("DSA")
    st.header("What is DSA?")
    st.write("Data Structures are a way of storing and organizing data in a computer.")
    st.write("Python has built-in support for several data structures, such as lists, dictionaries, and sets.")
    st.write("Other data structures can be implemented using Python classes and objects, such as linked lists, stacks, queues, trees, and graphs.")
    st.write("- Lists and Arrays")
    st.write("- Stacks")
    st.write("- Queues")
    st.write("- Linked Lists")
    st.write("- Hash Tables")
    st.write("- Trees")
    st.write("-Binary Trees") 
    st.write("- Binary Search Trees")
    st.write("- AVL Trees")
    st.write("- Graphs")
    st.header("Algorithms")
    st.write("Algorithms are a way of working with data in a computer and solving problems like sorting, searching, etc.")
    st.write("- Linear Search")
    st.write("- Binary Search")
    st.write("- Bubble Sort")
    st.write("- Selection Sort")
    st.write("- Insertion Sort")
    st.write("- Quick Sort")
    st.write("- Counting Sort")
    st.write("- Radix Sort")
    st.write("- Merge Sort")

elif data == "Python MYSQL":
    st.title("Python MYSQL")
    st.write("Python can be used in database applications.")
    st.write("One of the most popular databases is MySQL.")
    st.header("MySQL Database")
    st.write("To be able to experiment with the code examples in this tutorial, you should have MySQL installed on your computer.")
    st.write("You can download a MySQL database at https://www.mysql.com/downloads/.")
    st.header("Install MySQL Driver")
    st.write("Python needs a MySQL driver to access the MySQL database.")
    st.write("We recommend that you use PIP to install 'MySQL Connector'.")
    st.write("PIP is most likely already installed in your Python environment.")
    st.write("Navigate your command line to the location of PIP, and type the following:")
    st.write("Download and install 'MySQL Connector':")
    st.write(r"`C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector-python`")
    st.header("Test MySQL Connector")
    st.write("To test if the installation was successful, or if you already have 'MySQL Connector' installed, create a Python page with the following content:")
    st.write("demo_mysql_test.py:")
    st.code("""
    import mysql.connector
     """,language="Python")
    st.header("Create Connection")
    st.write("Start by creating a connection to the database.")
    st.write("Use the username and password from your MySQL database:")
    st.write("demo_mysql_connection.py:")
    st.code("""
    import mysql.connector
            mydb = mysql.connector.connect(
               host="localhost",
               user="yourusername",
               password="yourpassword"
    )

    print(mydb)
    """,language="Python")
    st.title("Python MySQL Create Database")
    st.header("Create Database")
    st.write("To create a database in MySQL, use the 'CREATE DATABASE' statement:")
    st.header("Example")
    st.code("""
    import mysql.connector
    mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
            print(x)
    """,language="Python")
    st.title("Python MySQL Create Table")
    st.header("Create Table")
    st.write("To create a table in MySQL, use the 'CREATE TABLE' statement.")
    st.write("Make sure you define the name of the database when you create the connection")
    st.header("Example")
    st.code("""
    import mysql.connector
    mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="mydatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    """,language="Python")
    st.title("Python MySQL Insert Into Table")
    st.header("Insert Into Table")
    st.write("To fill a table in MySQL, use the 'INSERT INTO' statement.")
    st.header("Explain")
    st.code("""
    import mysql.connector
    mydb = mysql.connector.connect(
       host="localhost",
       user="yourusername",
       password="yourpassword",
       database="mydatabase"
    )

    mycursor = mydb.cursor()

   sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
   val = ("John", "Highway 21")
   mycursor.execute(sql, val)

   mydb.commit()

   print(mycursor.rowcount, "record inserted.")

    """,language="Python")
    st.title("Python MySQL Select From")
    st.header("Select From a Table")
    st.write("To select from a table in MySQL, use the 'SELECT' statement:")
    st.header("Example")
    st.code("""
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
    print(x)
    """,language="Python")
    st.title("Python MySQL Where")
    st.header("Select With a Filter")
    st.write("When selecting records from a table, you can filter the selection by using the 'WHERE' statement:")
    st.header("Example")
    st.code("""
    import mysql.connector
    mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="mydatabase"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
   for x in myresult:
            print(x)
    """,language="Python")
    st.title("Python MySQL Order By")
    st.header("Sort the Result")
    st.write("Use the ORDER BY statement to sort the result in ascending or descending order.")
    st.write("The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.")
    st.header("Example")
    st.code("""
    import mysql.connector
    mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM customers ORDER BY name"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
    print(x)
    """,language="Python")
    st.title("Python MySQL Delete From By")
    st.header("Delete Record")
    st.write("You can delete records from an existing table by using the 'DELETE FROM' statement:")
    st.header("Example")
    st.code("""
    import mysql.connector
    mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")
    """,language="Python")
  
elif data == "pratice":
    st.markdown("<h2 style='font-weight:bold; font-family:Verdana;font-size:40px;'><span style='color:red;'>Pratice the Code</span></h2>",unsafe_allow_html=True)

    st.write("## Enter your Python code below and click **Run Code** to excecute it.")
    code_input =st.text_area(" Write your python code here: ","print('Hello , Streamlit!')", height=200 )
    if st.button("Run Code"):
        buffer = io.StringIO()
        try:
            with redirect_stdout(buffer),redirect_stderr(buffer):
                exec(code_input,{})
                output = buffer.getvalue()
        except Exception as e:
            output = str(e)
        st.subheader("Output:")
        st.code(output, language="Python")



elif data == "Quiz":
    st.markdown(
    """
    <h2 style='font-weight:bold; font-family:Verdana; font-size:40px;'>
        📝 <span style='color:#306998;'>Python</span>&nbsp;&nbsp;
        <span style='color:#FFD43B;'>Quiz</span>
    </h2>
    """,
    unsafe_allow_html=True
)

    python_questions = [
        {
            "question": "What is the output of: print(type([]))?",
            "options": ["<class 'list'>", "<type 'list'>", "<list>", "list"],
            "answer": "<class 'list'>"
        },
        {
            "question": "Which of these is not a valid Python data type?",
            "options": ["tuple", "list", "array", "set"],
            "answer": "array"
        },
        {
            "question": "What will this code return: bool('False')?",
            "options": ["False", "None", "True", "0"],
            "answer": "True"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "function", "def", "lambda"],
            "answer": "def"
        },
        {
            "question": "What does the len() function do?",
            "options": [
                "Returns the number of characters in a string",
                "Returns the number of items in an object",
                "Both of the above",
                "None of the above"
            ],
            "answer": "Both of the above"
        },
        {
            "question": "What is the result of: 3 * 1**3?",
            "options": ["3", "1", "9", "27"],
            "answer": "3"
        },
        {
            "question": "What is the output of: print('5' + '5')?",
            "options": ["10", "55", "Error", "None"],
            "answer": "55"
        },
        {
            "question": "Which of the following is used to handle exceptions?",
            "options": ["try-except", "if-else", "for-while", "switch-case"],
            "answer": "try-except"
        },
        {
            "question": "Which method can be used to convert a string to lowercase?",
            "options": [".lower()", ".downcase()", ".tolowercase()", ".casefold()"],
            "answer": ".lower()"
        },
        {
            "question": "How do you start a comment in Python?",
            "options": ["//", "/*", "#", "--"],
            "answer": "#"
        }
    ]

    TOTAL_QUESTIONS = len(python_questions)

    
    if 'q_idx' not in st.session_state:
        st.session_state.q_idx = 0
        st.session_state.score = 0
        st.session_state.answers = []

    def next_question():
        st.session_state.q_idx += 1

    if st.session_state.q_idx < TOTAL_QUESTIONS:
        q = python_questions[st.session_state.q_idx]
        st.subheader(f"Question {st.session_state.q_idx + 1} of {TOTAL_QUESTIONS}")
        st.write(q["question"])
        selected = st.radio("Choose an option:", q["options"], key=st.session_state.q_idx)

        if st.button("✅ Submit Answer"):
            st.session_state.answers.append(selected)
            if selected == q["answer"]:
                st.session_state.score += 1
            next_question()
            st.rerun()
    else:
        st.title("🎉 Quiz Completed!")
        st.success(f"Your Score: {st.session_state.score} / {TOTAL_QUESTIONS}")
        st.balloons()

        for i, user_answer in enumerate(st.session_state.answers):
            q = python_questions[i]
            correct = q["answer"]
            st.write(f"**Q{i + 1}: {q['question']}**")
            if user_answer == correct:
                st.success(f"✅ Your answer: {user_answer}")
                st.image("https://emojiterra.com/data/animated-emoji/1f44d.gif", width=100, caption="Good Luck")
            else:
                st.error(f"❌ Your answer: {user_answer} | Correct: {correct}")
                st.image("https://emojiterra.com/data/animated-emoji/1f61e.gif", width=100, caption="Try again!")
            st.markdown("---")

        if st.button("🔁 Restart Quiz"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


