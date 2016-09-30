System = input("Which system would you like to use? USC or Metric?")
#this is the initial prompt to find out which system the user wants to use
Distance = input("How far did you drive?")
if  System == "USC":
    print ("Miles")
else:
    print("Km")
Gas = input("How much gas did you use?")
if System == "USC":
    print("Gallons")
else:
    print("Liters")
Consumption = float(Distance / Gas)
if System == "USC": print("mpg")
else:
    print ('1/100km')
if System == "USC": Distance *1.60934 and Gas * 3.78541
else: Distance * .62371
Gas * .264172
print ("Gas Consumption Ratin")
if Consumption >20: print ("Extremely Poor")
if Consumption > 20: print ("Extremely Poor")
 elif Consumption > 15 and Consumption :=<20  print ("Poor") 
elif Consumption > 10 and Consumption =<15   print ("Average") 
elif: Consumption > 8 and Consumption =<10     print ("Good") 
elif: Consumption <= 8: print("Excellent")
