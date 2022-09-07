print("hello")
allBooks = ["book1", "book2", "book3", "book4", "book5"]

shelf1 = ["book1", "bookk2", "book3"]

shelf2 = ["book4", "book5"]

takeaway = ["book3"]

Q1 = input("what are u asking for?")
if Q1 in shelf1:
    print("shelf 1")
elif Q1 in shelf2:
    print("shelf 2")
else:
    print("i dont have it")

if Q1 in takeaway and allBooks:
    print("taken")