name = input("what is your name?")
print(f"Hello { name }, did it run as expected?")
answer = input().lower()
print(answer)
if answer == "yes":
    print("Good!")
else:
    error1 = input("What was the problem? ")