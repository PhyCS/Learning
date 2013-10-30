'''
Created on Oct 12, 2013

@author: srausch
'''
def check(n):
    q = raw_input("You chose " + str(n) + " is that correct? [Y]es/[N]o:")
    if q.lower() == "y" or q.lower() == "yes":
        return "Good"
    else:
        print "Bummer! Let's try again."
        return pick_number(n = input("Pick a number: "))
        
def pick_number(n):
    if str(type(n)) == "<type 'int'>":
        return check(n)
    else:
        print "Please select an integer."
        return pick_number(n = input("Pick a number: "))
        
print pick_number(n = input("Pick a number: "))