height = (float(input('what is your height(in cm):')))/100
weight = float(input('what is your weight(in kg):'))
BMI = float(weight/(height*height))
if BMI < 18.4:
    print('your BMI is',BMI, ',too light!')
elif 18.5 <= BMI <= 23.9:
    print('your BMI is', BMI, ',perfect!')
elif 24 <= BMI <= 26.9:
    print('your BMI is', BMI, ',a little too heavy!')
else:
    print('your BMI is',BMI, ',too heavy!!!!!!!!')