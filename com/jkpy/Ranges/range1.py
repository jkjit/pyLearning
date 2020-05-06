income = int(input("What is your income? $"))
if income < 9701:
    tax = 0.1 * income
elif 9701 <= income < 39476:
    tax = 970 + 0.12 * (income - 9700)
elif 39476 <= income < 84201:
    tax = 4543 + 0.22 * (income - 39475)
elif 84201 <= income < 160726:
    tax = 14382.5 + 0.24 * (income - 84200)
elif 160726 <= income < 204101:
    tax = 32748.5 + 0.32 * (income - 160725)
elif 204101 <= income < 510301:
    tax = 46628.5 + 0.35 * (income - 204100)
else:
    tax = 153798.5 + 0.37 * (income - 510300)
print(f"Your tax on that income is ${tax:.2f}")
