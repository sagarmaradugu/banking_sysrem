
customer_names= ['jane smith','iason jordan','david morgan','brain john','jack swift']
customer_pins = ['0123','2575','7275','2312','5049']
customer_balances = [10000,20000,20000,40000,10000]
deposit = 0
withdraw = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

while True:
    print("=========================================")
    print("----------welcome to my bank-------------")
    print("*****************************************")
    print("=<<  1. open a new account          >>==")
    print("=<<  2. with draw money             >>==")
    print("=<<  3. deposit money               >>==")
    print("=<<  4. check customer & balance    >>==")
    print("=<<  5. exit/quit                   >>==")

    choice_number = input("select your choice from above menu::")
    if choice_number == '1':
        print("choice number 1 is selected by customer")

        NOC = eval(input("no of customers::"))

        i = i + NOC
        if i > 5:
            print("\n")
            print("customer registration is exceeded")
            i = i - NOC
        else:
            while counter_1 <= i:
                name = input("Enter full name:")
                customer_names.append(name)
                pin = str(input("create your pin:"))
                customer_pins.append(pin)
                balance = 0
                deposit = eval(input("enter your deposit amount to start account:"))
                balance = balance + deposit
                customer_balances.append(balance)
                print("\nName=",end=" ")
                print(customer_names[counter_2])
                print("Pin=",end=" ")
                print(customer_pins[counter_2])
                print("Balance=",end=" ")
                print(customer_balances[counter_2],end=" ")
                print("/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nyour name is added to customers system")
                print("your pin is added to customer system")
                print("your balance is added to customer system")
                print("----new account created successfully----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(customer_names)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")

        main_menu = input("please press enter key to go back to menu to perform another function or exit...")
    elif choice_number == '2':
        j = 0
        print("choice number 2 is selected by customer")
        while j < 1:
            k = -1
            name = input("please input name:")
            pin = input("please input pin:")
            while k < len(customer_names) - 1:
                k = k+1
                if name == customer_names[k]:
                    if pin == customer_pins[k]:
                        j = j + 1
                        print("your current balance:",end=" ")
                        print(customer_balances[k],end=" ")
                        print("-/Rs\n")
                        balance = (customer_balances[k])

                        withdraw = eval(input("input value to withdraw:"))
                        if withdraw > balance:
                            deposit = eval(input("Please Deposit a higher Value because your Balance mentioned above is not enough :"))
                            balance = balance + deposit
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n")  # 1000-500=500
                            balance = balance - withdraw
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            customer_balances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            balance = balance - withdraw
                            print("\n")
                            print("----Withdraw Successfull!----")
                            customer_balances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                print("your name and pin does not match\n")
                break
            main_menu = input("please press enter key to go back to main menu to perform another function or exit.. ")
    elif choice_number == '3':
        print("choice number 3 is selected by the customer")
        n = 0
        while n < 1:
            k =- 1
            name = input("please input name:")
            pin = input("please input pin:")
            while k < len(customer_names) - 1:
                k = k + 1
                if name == customer_names[k]:
                    if pin == customer_pins[k]:
                        n = n + 1
                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.
                        print("Your Current Balance: ", end=" ")
                        print(customer_balances[k], end=" ")
                        print("-/Rs")
                        balance = (customer_balances[k])
                        # This statement below takes the depositionn from the customer.
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition  # 1000+500=1500
                        customer_balances[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("your name and pin does not match\n")
                break
        main_menu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choice_number == '4':
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        # The while loop below will keeping running until all the customers and balances are shown.
        while k <= len(customer_names) - 1:
            print("->.Customer =", customer_names[k])
            print("->.Balance =", customer_balances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
            # This statement below helps the user to go back to the start of the program (main menu).
        main_menu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choice_number == '5':
        # These statements would be just showed to the customer.
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")


















