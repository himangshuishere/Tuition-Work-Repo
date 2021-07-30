#purchase discount total pay

purchase = float(input("Enter the net payment: "))

if purchase >= 1000:
	discount = purchase*(10/100)
	netPayment = purchase - discount

elif purchase >=2000:
	discount = purchase*(15/100)
	netPayment = purchase - discount

elif purchase >= 3000:
	discount = purchase*(20/100)
	netPayment = purchase - discount

else:
	discount = purchase*(25/100)
	netPayment = purchase - discount


print("Total purchase amount: ", purchase)
print("Discount received: ", discount)
print("Net Payable: ", netPayment)