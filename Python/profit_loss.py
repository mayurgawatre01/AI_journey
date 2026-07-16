def pro_los(cost_price,selling_price):
    x=selling_price-cost_price 
    if x>0 :return "profit"
    else: return "Loss"    
print(pro_los(3000,500))