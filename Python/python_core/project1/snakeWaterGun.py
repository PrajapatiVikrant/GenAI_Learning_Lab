computer = -1
you = input("Enter s for snake, w for water and g for gun: ")

youDict = {"s":1, "w":-1, "g":0}
youNum = youDict[you]


if computer == -1 and youNum == 1:
    print("You win")
elif computer == 1 and youNum == -1:
    print("Computer wins")
elif computer == 0 and youNum == -1:
    print("You win")
elif computer == -1 and youNum == 0:
    print("Computer wins")
elif computer == 1 and youNum == 0:
    print("You win")
elif computer == 0 and youNum == 1:
    print("Computer wins")
else:    print("It's a tie")