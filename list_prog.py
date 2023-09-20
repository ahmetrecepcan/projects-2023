import colorama
oddlist = list()
evenlist = list()
list1 = list()


while True:
    number = input(colorama.Fore.BLUE + "Please Enter A Number (For Exit Press Enter- github:https://github.com/ahmetrecepcan/arcan-projects)). \n")
    try:
        if number == "":
            break
        else:
            if number not in list1:
                list1.append(number)
            else:
                print(colorama.Fore.RED + "The Number You Typed Has Been Entered Already. Please Enter Another Number.")
        kalan = int(number) % 2
        if kalan == 0:
            evenlist.append(number)
        else:
            oddlist.append(number)
    except ValueError:
        print(colorama.Fore.RED, "You Can Only Enter Numbers")

print(colorama.Fore.MAGENTA, ("Odd Numbers in the List"), oddlist)
print(colorama.Fore.MAGENTA, ("Even Numbers in List"), evenlist)