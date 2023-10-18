account_balance = 2400
permission = "yes"

process = (lambda withdraw, balance:
            ("Withdraw amount and update account balance", balance - withdraw))(400, account_balance)
            if permission == "yes":
            else(lambda withdraw, balance:
                ("Withdraw not allowed", balance))

final, account_balance = process

deposit_amount = 600
account_balance += deposit_amount

print(f"Withdraw amount:{final}")
print(f"Account balance after the deposit: {account_balance}")





