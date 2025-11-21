# number of days in a month

print('program will print number of days in a given month')

flag = 1  # assumes user enters valid input

# get month from user
month = int(input('enter the month(1-12) = '))

# check if entered month = 2 i.e., february
if month == 2:
    year = int(input('enter year = '))
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        num_days = 29
    else:
        num_days = 28

    # if entered month is one from (jan,mar,may,july,aug,oct,or dec)
elif month in (1,3,5,7,8,10,12):
    num_days = 31

    # if entered month is one from (april,june,sept,nov)
elif month in (4,6,9,11):
    num_days = 30

else:
    print('please enter valid month')
    flag = 0

    # finally print num_days
if flag == 1:
    print('There are',num_days,' days in ',month,' month.')
