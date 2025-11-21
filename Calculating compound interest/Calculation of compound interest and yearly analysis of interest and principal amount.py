# mini project

# write a program to find the compound interest

def com_int(p, n, r):
    print('start balance\t','\tInterest\t','\tEnding balance')
    x = r/100  # calculate interest

    tot = 0
    for i in range(1,n+1):
        z_new = p * (1 + x) ** i - p  # new interest
        z_old = p * (1 + x) ** (i-1) - p  # old interest
        tot = tot + (z_new - z_old)

        if i == 1:
            print('{0:.2f}\t'.format(p),end='')
            print('\t\t{0:.2f}\t'.format(z_new - z_old),end='')
            print('\t\t{0:.2f}\t'.format(z_new + p))
        else:
            print('{0:.2f}\t'.format(p + z_old), end='')
            print('\t\t{0:.2f}\t'.format(z_new - z_old), end='')
            print('\t\t{0:.2f}\t'.format(z_new + p))
    print('Total interest deposited:RS {0:.2f}'.format(tot))

p = int(input('Enter the principal amount: '))
r = int(input('Enter the rate of interest: '))
n = int(input('Enter the number of year: '))
com_int(p,n,r)
