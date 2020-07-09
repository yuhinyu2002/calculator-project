#num = input ("What is your weight in pounds?")
#planet = input ("Choose a planet: Mars, Venus, Mercury, Jupiter, Saturn")
#new = None

#num= float(num)
#if planet == "Mars":
    #new = num/9.81 * 3.711
#elif planet == "Venus":
    #elif planet == "Mercury"
    #new = num/9.81 * 3.7
#elif 

salary = input("What is your yearly salary")
bonuses = input("How much bonus will you make this year?")


income = None

total_income = None

salary = float(salary)
bonuses = float(bonuses)
if 0 <= salary <= 8500:
    income = (salary + bonuses)*0.96
if 8500 < salary <= 11700:
    income = (salary + bonuses)*0.955
if 11700 < salary <= 13900:
    income = (salary + bonuses)*0.955
if 13900 < salary <= 21400:
    income = (salary + bonuses)*0.9475
if 21400 < salary <= 80650:
    income = (salary + bonuses)*0.9379
if 80650 < salary <= 215400:
    income = (salary + bonuses)*0.9351
if 8215400 < salary <= 1077550:
    income = (salary + bonuses)*0.9315


if 0 <= income <= 9875:
    total_income = income*0.9
if 9875 < income <=40125:
    total_income = income*0.88
if 40125 < income <= 85525:
    total_income = income*0.78
if 85525 < income <= 163300:
    total_income = income*0.76
if 163300 < income <= 207350:
    total_income = income*0.68
if 207350 < income <= 518400:
    total_income = income*0.65
print (total_income)





