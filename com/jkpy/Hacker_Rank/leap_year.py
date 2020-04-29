print("Please enter year in YYYY format to find out Leap Year or not : \n")
proceed = True
def leap(year):
    if year%4 == 0 and (year%100 !=0 or year%400 == 0):
        print(f'Your entered year {year} is a Leap Year !!Congrats...')
    else:
        print(f'Your entered year {year} is not a Leap Year . Sorry!!!')

def leap_one(year):
    if year%4 == 0:
        if(year%100!=0):
            print(f'Your entered year {year} is a Leap Year !!Congrats...')
        else:
            if year%400==0:
                print(f'Your entered year {year} is a Leap Year !!Congrats...')
            else:
                print(f'Your entered year {year} is NOT Leap Year !!Congrats...')
        # print(f'Your entered year {year} is a Leap Year !!Congrats...')
    else:
        print(f'Your entered year {year} is NOT a Leap Year . Sorry!!!')

while proceed:
    # year = int(input())
    user_input = input()
    if user_input == "":
        proceed = False
    else:
        year = int(user_input)
        leap_one (year)

# leap(year)