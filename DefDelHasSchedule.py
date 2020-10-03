#Format:`0 1 2 3 4 5 6 7 8 9 10.......23 in x:00 hour time slots
'''
var = [representation, explanation,attributes]
'''
S = [" S ","Sleep"]
NC = ["N C","Not Working On Console"]
NCY = ["N C","Not Working On Console","Prioritize Bright Light Exposure"]
NCO = ["N C","Not Working On Console","Do not wear sunglasses-See Light"]
O1 = ["O 1","Working on console for ORBIT 1","Prioritize Bright Light Exposure"]
MS = ["M S","Take Melatonin Chronobiological Medicine and sleep"]
NAP = ["NAP","Take a 90 min Nap"]
free = ["   ","Nothing scheduled"]
GR = ["gre","Nothing Scheduled","Wear Sunglasses-Avoid Light"] # gre is placeholder for gray color
YL = ["yel","Nothing Scheduled","Prioritize Bright Light Exposure"] # yel is placeholder for yellow color
OR = ["ora","Nothing ScheduledL,"Do not Wear Sunglasses-See Light"]
#Assigning default values
NCday1 = NCday2 = [S,S,S,S,S,S,free,free,NC,NC,NC,NC,NC,NC,NC,NC,free,free,free,free,free,free,S]
3dbo1 = [S,S,S,S,S,S,S,free,free,free,free,free,free,free,free,free,free,free,free,free,free,free]
2dbo1 = [YL,YL,S,S,S,S,S,S,free,free,free,free,free,free,free,free,free,free,free,free,free,free,free]
1o1 = [YL,YL,YL,YL,S,S,S,S,S,S,S,S,free,free,free,free,free,free,NAP,NAP,free,free,YL,O1]
2o1 = 3o1 = 4o1 = 5o1 = 6o1 = 7o1 = [O1,O1,O1,O1,O1,O1,O1,O1,YL,MS,S,S,S,S,S,free,free,free,NAP,NAP,free,free,YL,O1]
Po1 = [O1,O1,O1,O1,O1,O1,O1,O1,YL,MS,S,S,S,S,S,free,free,free,NAP,NAP,free,free,YL,O1]
Po1NC1 = [S,S,S,S,S,S,S,S,YL,NCY,NCY,NCY,NCY,NCY,NCO,NCO,NCO,OR,OR,OR,free,GR,GR,MS]
Po1NC2 = [S,S,S,S,S,S,S,S,YL,NCY,NCY,NCY,NCY,NCO,NCO,NCO,NCO,OR,OR,free,free,GR,GR,MS]
Po1NC3 = [S,S,S,S,S,S,S,S,YL,NCY,NCY,NCY,NCO,NCO,NCO,NCO,NCO,OR,free,free,free,GR,GR,MS]
Po1NC4 = [S,S,S,S,S,S,S,S,YL,NCY,NCY,NCO,NCO,NCO,NCO,NCO,NCO,OR,free,free,free,free,free,MS]
Offday1 = Offday2 = [S,S,S,S,S,S,S,S,free,free,free,free,free,free,free,free,free,free,free,free,free,free,S]
#Making a double-dimensional array for storing the whole default schedule
wholeSched=[NCday1,3dbo1,2dbo1,1o1,2o1,3o1,4o1,5o1,6o1,7o1,Po1,Po1NC1,Po1NC2,Po1NC3,Po1NC3,Offday1,Offday2]
#Finish of Assigning Default Schedule
def offsetScheduleDelay(offhours,li):
  for i in range(offhours):
    temp = li[len(li)-1]
    for i in range(0,24):
      li[i+1]=li[i]
    li[0] = temp
def offsetScheduleHasten(offhours,li):
  for i in range(offhours):
    temp = li[0]
    for i in range(1,25):
      li[i-1]=li[i]
    li[len-1] = temp
    
