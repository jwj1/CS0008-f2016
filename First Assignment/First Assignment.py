System = input("Which system would you like to use? USC or Metric?")
#this is the initial prompt to find out which system the user wants to use
Distance = input("How far did you drive?")
Gas = input("How much gas did you use?")
unit = vars("USC or Metric")
if  System == "USC":
    DU = Distance
    print DU
    print ("Miles")
    GU = Gas
    print GU
    print ("Gallons")
    DM = DU * 1.60934
    print DM
    print ("Km")
    GM = GU * 3.78541
    print GM
    print ("Liters")
else:
    DM = Distance
    print DM
    print("Km")
    GM = Gas
    print GM
    print ("Liters")
    DU = DM *.621371
    print DU
    print ("Miles")
    GU = GM * .264172
    print GU
    print ("Gallons")
# compute consumption
# USC
ConsumptionUS = float(DU / GU)
# Metric
ConsumptionM = float(DM / GM)
if System == "USC":
    print ConsumptionUS
    print "mpg"
    print ConsumptionM
    print "1/100km"
else:
    print ConsumptionM
    print "1/100km"
    print ConsumptionUS
    print "mpg"

#
#Consumption = float(Distance / Gas)
#if System == "USC":
#    print("mpg")
#else:
#    print ('1/100km')
#if System == "USC":
#    DistanceU = Distance *1.60934
#    Gas * 3.78541
#else:
#    Distance * .62371
#Gas * .264172

print ("Gas Consumption Rating")
if ConsumptionM > 20:
    print ("Extremely Poor")
elif ConsumptionM > 15 and ConsumptionM =< 20:
    print ("Poor")
elif ConsumptionM > 10 and ConsumptionM =< 15:
    print("Average")
elif ConsumptionM > 8 and ConsumptionM =< 10:
    print ("Good")
elif ConsumptionM < 8:
    print ("Excellent")

format("6.3f")