# function with a default parameter value
def my_function(country="Norway"):
    print("I am from " + country)


# passing an argument overrides the default
my_function("Sweden")
my_function("Pakistan")

# calling with no argument uses the default ("Norway")
my_function()

my_function("Brazil")
