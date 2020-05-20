def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

# Variable
num = 3

print(
    factorial(10)
)

# create set
thisset = {"apple", "banana", "cherry"}

print(thisset)

# Dictionary/Hash 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(
    thisdict["brand"]
)
