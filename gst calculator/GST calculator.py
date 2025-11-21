# mini project on gst calculator
# it will calculate the gst
# two types of gst -- 1) center type (CGST)
#                     2) state type (SGST)

cp = float(input("enter the cost of production  = "))
cg1 = float(input("enter tax % imposed by centre, eg:- cgst = "))
sg1 = float(input("enter tax % imposed by state, eg:- sgst = "))

amount_cg1 = ((cg1/100)*cp)
amount_sg1 = ((sg1/100)*cp)

total = cp + amount_cg1 + amount_sg1  # total amount

print("total cost of production : rs = ", total)