p = float(input("enter amount: "))
r = float(input("enter interest: "))
t = float(input("enter years: "))

interest_calc = input("compounded [yearly/half-yearly/quaterly/monthly]: ")

d = {'yearly': 12 , 'half-yearly': 6,'quaterly': 3,'monthly': 1 }

n = (t*12) / d[interest_calc]
print(n)

amount = p*(1+((r/100)*(d[interest_calc]/12)))**n

print(amount)