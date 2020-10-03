# NSAC-Hypnos
from datetime import datetime
def sleeptime(n):
        """Enter in 24 hours format"""
        print("Day T minus ", n)
        print("When you get to bed today?")
        print("HH")
        shh=int(input())
        print("approx MM")
        smm=int(input())
        sleep=datetime(shh,smm,00)
        print("when did you wake up?"
        print("HH")
        whh=int(input())
        print("approx MM")
        wmm=int(input())
        wake=datetime(whh,wmm,00)
        n=n-1
        sleeptime=wake-sleep
        print("your sleep time is", sleep.total_seconds()/60**2, "hours", sleep.total_seconds()/60, "minutes")

def meals(n):
        print("Day T minus", n)
        Print("did you had a meal right now?")
        ans=input()
        If(ans=='y'):
                Varmeal=[]
                Varmeal.append(datetime.currenttime())
                Print("thanks for your response, your mealtime has been recorded"
        Else:
                Print("why you called this func! Press enter to exit")
