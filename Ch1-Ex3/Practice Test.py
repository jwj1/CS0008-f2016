numgoods= input("please enter # of goods ordered")
    (int)numgoods
instate= input("if in state order type order type true else enter false")
if numgoods >= 1 and <= 1000:
    discount = .1
elif numgoods >= 1001 and <= 5000:
    discount = .15
elif numgoods >=5001 and <= 10000:
    discount = .20
elif numgoods > 10000:
    discount = .20 + (numgoods * .01)
else :error
Total_Cost= numgoods * .5
Total_Cost_Dis= Total_Cost * discount

if numgoods >=1 and <= 500:
