def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function1(name): # name is a parameter
  print("Hello", name)

my_function1("Emil") # "Emil" is an argument


def my_function2(country = "Norway"):
  print("I am from", country)

my_function2("Sweden")
my_function2("India")
my_function2()
my_function2("Brazil")
