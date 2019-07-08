# Project Name : PyPrice
# Author : Mehedi Hasan Remon
# Facebook : facebook.com/believer.py



########## Product List ############
product = {"Bike":"$100","Car":"$200","Plane":"$300","Rocket":"$400","Space Ship":"$500"}

######### Print Basic Instruction ##########
print "\n"+"--== Mehedi Hasan Remon ==--"
print "\n"+"Enter (x) to Exit From This Program"+"\n"

############ Print All Product ############
for x in product:
    print x


########### Main Function #############
def cal(item,name):
    result = False
    for x in item:
        if x == name:
            result = True
    return result

#########Apply Our Main Function##########

###### Exit Loop Function ######
exit_var = False
while exit_var == False:

###### User Input #######
    user_var = raw_input("\n"+"Enter Your  Product Name Here : ")

###### Exit Loop Trigger ######
    if user_var == "x":
        exit_var = True

     
###### Show Price #######
    if cal(product,user_var):
        print user_var+" Price is",
        print product[user_var]
    
####### If Input Dose Not Match #######
    if cal(product,user_var) == False and user_var != "x":
        print "This Product Dosent Exist on Our Store !"
