def leap_year(n):
    if (n%4==0 and n%100!=0) or n%400==0: return "it is an leap year"
    else: return "not a leap year"
print(leap_year(2000))
    