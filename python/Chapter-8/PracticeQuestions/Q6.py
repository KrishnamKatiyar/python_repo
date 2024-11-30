# Q6 - Write a python function which converts inches to cms.

def inchesToCms(inc):
    cms = inc * 2.54
    return cms

inches = float(input("Enter the measurment in inches : "))

print(f"There are {inchesToCms(inches)}cm in {inches}inches")
