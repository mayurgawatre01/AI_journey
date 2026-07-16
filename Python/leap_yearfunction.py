def leap_year(n):
    if (n%4==0 and n%100!=0) or n%400==0: return True
    else: return False

print(leap_year(2024) )
print(leap_year(1900) )
print(leap_year(2000) )
print(leap_year(2100) )
print(leap_year(2400) )