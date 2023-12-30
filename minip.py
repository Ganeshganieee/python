''''print('Welcome to BOOK MY SHOW')
name=input('please enter your name:- ')
seats=int(input('please enter the number of seats,you want tp book:- '))
category=int(input('please select 1--> diomand class /n selcet 2--> gold class /n selcet 3--> silver class'))
if category ==1:
    amount=seats*200
elif category==2:
    amount=seats*150
elif category==3:
    amount=seats*100
print(f'Hi{name} you have booked{seats} seats and total {amount}')'''


print('Welcome to BOOK MY SHOW')
name=input('please enter your name:- ')
seats=int(input('enter a seats: '))
option=int(input('enter option here: '))
match option:
    case 1:
        print('diamond class')
        amt=seats*200
    case 2:
        print('golden class')
        amt=seats*150
    case 3:
        print('silver class')
        amt=seats*100
    case _:
        print('invalid option')
        amt=None
print(amt)
