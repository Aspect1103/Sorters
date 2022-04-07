import Sorters
import random

randomLimit = 10000


def loopDriver(f):
    size = 0
    for amount in range(4):
        print("amount")
        f.append("amount")
        for iteration in range(100):
            print("iteration")
            if amount == 0:
                size = 10
            elif amount == 1:
                size = 100
            elif amount == 2:
                size = 1000
            elif amount == 3:
                size = 10000
            numbers, totalTime = Sorters.gnome([random.randint(0, randomLimit) for _ in range(size)])
            f.append(totalTime)
    with open("results.txt", "w") as file:
        for i in f:
            file.write(str(i) + "\n")


def normalDriver():
    choice = input('''Which sort do you want to use:
     1. Bubble sort
     2. Insertion sort
     3. Selection sort
     4. Merge sort
     5. Quick sort
     6. Bogo sort
     7. Gnome sort
    Pick an option: ''')

    size = int(input("How many items?: "))

    if choice == "1":
        numbers, totalTime = Sorters.bubble([random.randint(0, randomLimit) for _ in range(size)])
        print("Sorted list is", numbers, "taking", totalTime, "seconds to complete")
    elif choice == "2":
        numbers, totalTime = Sorters.insertion([random.randint(0, randomLimit) for _ in range(size)])
        print("Sorted list is", numbers, "taking", totalTime, "seconds to complete")
    elif choice == "3":
        numbers, totalTime = Sorters.selection([random.randint(0, randomLimit) for _ in range(size)])
        print("Sorted list is", numbers, "taking", totalTime, "seconds to complete")
    elif choice == "4":
        numbers, totalTime = Sorters.merge([random.randint(0, randomLimit) for _ in range(size)])
        print("Sorted list is", numbers, "taking", totalTime, "seconds to complete")
    elif choice == "5":
        numbers, totalTime = Sorters.quick([random.randint(0, randomLimit) for _ in range(size)])
        print("Sorted list is", numbers, "taking", totalTime, "seconds to complete")
    elif choice == "6":
        numbers, totalTime = Sorters.bogo([random.randint(0, randomLimit) for _ in range(size)])
        print("Sorted list is", numbers, "taking", totalTime, "seconds to complete")
    elif choice == "7":
        numbers, totalTime = Sorters.gnome([random.randint(0, randomLimit) for _ in range(size)])
        print("Sorted list is", numbers, "taking", totalTime, "seconds to complete")


# normalDriver()
loopDriver([])
