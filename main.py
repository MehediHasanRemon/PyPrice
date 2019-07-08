#Product List
product = {"Bike":"$100","Car":"$200","Plane":"$300","Rocket":"$400","Space Ship":"$500"}

#Print All Product
for x in product:
    print x


#Main Function
def cal(item,name):
    result = False
    for x in item:
        if name == x:
            result = True
    return result

