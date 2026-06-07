# What Is a Function?

# A function is a reusable block of code.

# Without functions:

# print("Ghost of Tsushima")
# print("Ghost of Tsushima")
# print("Ghost of Tsushima")

# With a function:

def show_game():                 #def is a keyword that tells Python we're defining a function.
    print("Ghost of Tsushima")

# Then:

show_game()                      # this calls the function, which runs the code inside it.
show_game()                      # We can call the function as many times as we want.
show_game()

# Output:

# Ghost of Tsushima
# Ghost of Tsushima
# Ghost of Tsushima


# Why Developers Use Functions
# Functions help us:
# Avoid repeating code
# Organize programs
# Make code easier to read
# Reuse logic


# What if we want:

# Hello Sujoy
# Hello Kratos
# Hello Geralt

# without creating 3 different functions?

# We use parameters.

def greet(name):
    print("Hello", name)
greet("Sujoy")
greet("Kratos")
greet("Geralt")

#This will output: 
# Hello Sujoy
# Hello Kratos                     as we have passed different arguments to the same function, 
# # Hello Geralt                   which allows us to reuse the same code with different inputs.
               