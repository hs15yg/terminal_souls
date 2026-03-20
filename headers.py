colors = {
    "RED": "\033[31m",
    "BLACK": "\033[30m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
    "WHITE": "\033[37m",
}
# i create a function called star
def star():
    print("-----------menu---------------")
    option = 0
    #here i create a validator so that when the user enters anything other than 1 or 2,they get an invalid option message and the "select 1 or 2 message is repeated"
    while option != 1 and option != 2:
    # i use the try block to detect the problem and the except block to ensure the code executes without getting corrupted   
        try:
            option = int(input("which one do you want to select 1.play, 2.exit: "))
        except:
            print("enter only number")

    if option == 1:
        print("------  🎉 welcome to the game terminal souls 🎉------")
        name = input("------------ender to name: ")
        print(f"\n get ready,{name} the battle begins now🔥")
    else:
        print("you have left the game ➜] ")
    #i use print to print the result to the console
    

star()