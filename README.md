# NSAC-Hypnos
from datetime import datetime
def sleeptime(n):
        """Enter in 24 hours format"""
        print("Day T minus ", n)
        print("When you get to bed today?")
        print("HH")
        input(int(shh))
        print("approx MM")
        input(int(smm))
        sleep=datetime(shh,smm,00)
        print("when did you wake up?"
        print("HH")
        input(int(whh))
        print("approx MM")
        input(int(wmm))
        wake=datetime(whh,wmm,00)
        n=n-1
        sleeptime=wake-sleep
        print("your sleep time is", sleep.total_seconds()/60**2, "hours", sleep.total_seconds()/60, "minutes")
