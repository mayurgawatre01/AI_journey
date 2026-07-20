import pandas as pd
s=pd.Series([10,20,],index=["mayur","soham","abhi","Ram"])
print(s)


df=pd.DataFrame({
    "math":[10,20,30],
    "english":[40,50,60],
    "Science":[30,60,70]
})





# Declare scores
physics = pd.Series([85, 95], index=['Bob', 'Alice'])
maths = pd.Series([80, 90], index=['Alice', 'Bob'])
chemistry = pd.Series([70], index=['Alice'])

# Add all subjects together
total = maths + physics + chemistry
print(total)