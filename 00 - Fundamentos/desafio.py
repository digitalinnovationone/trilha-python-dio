menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[0] Exit

=> """

balance = 0
limit = 500
statement = ""
withdraws_num = 0
WITHDRAWS_LIMIT = 3

while True:

    option = input(menu)

    if option == "1":
        value = float(input("Insert the deposit value: "))

        if value > 0:
            balance += value
            statement += f"Deposit: R$ {value:.2f}\n"

        else:
            print("Invalid amount.")

    elif option == "2":
        value = float(input("Insert the withdraw value: "))

        balance_exceeded = value > balance

        limit_exceeded = value > limit

        withdraws_exceeded = withdraws_num >= WITHDRAWS_LIMIT

        if balance_exceeded:
            print("Not enough balance.")

        elif limit_exceeded:
            print("Withdraw value exceeds the limit.")

        elif withdraws_exceeded:
            print("Maximum number of withdraws reached.")

        elif value > 0:
            balance -= value
            statement += f"Withdraw: R$ {value:.2f}\n"
            withdraws_num += 1

        else:
            print("Operation failed! Invalid amount.")

    elif option == "3":
        print("\n================ STATEMENT ================")
        print("No transactions were made." if not statement else statement)
        print(f"\nBalance: R$ {balance:.2f}")
        print("==========================================")

    elif option == "0":
        break

    else:
        print("Invalid option.")
