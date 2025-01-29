import datetime
def getTime():

    #get the raw time
    raw_time = datetime.datetime.now()

    #formatting it:
    formatted_time = raw_time.strftime("%H:%M")
    
    
    return formatted_time


def TimeInput(timestamp):
    while True:
        user_input = input(f"Enter the {timestamp} time(UTC) in HH:MM 24 hour-format: ")
        
        if not ":" in user_input:       
            print("try again loser maybe with a colon this time")
        else:
            split_user_input = user_input.split(":")
            if (len(split_user_input[0]) == 2) and (len(split_user_input[1]) == 2):
                break
            else:
                print ("ensure there are two numbers on each side")
            
    return user_input
            


DARK_MODE_START = TimeInput('start')
DARK_MODE_END = TimeInput('end')
testMode = False


def testerDecorator(func):
    global testMode
    def wrapper(*args):
        result = func(*args)
        if testMode:
            print (f"From: {args}, {result} was returned")
        return result
    return wrapper

@testerDecorator
def is_dark_mode(givenTime):
    current = int(givenTime.replace(":","")) #removes : from time string to convert to int
    start = int(DARK_MODE_START.replace(":","")) # same thing for start
    end = int(DARK_MODE_END.replace(":","")) # same thing for end
    # START = 2200
    # END = 700
    if end < start: #crosses over midnight
        return (start <= current or end > current)
    elif end == start: #all the time
        return True
    else: #doesnt cross over midnight(same day)
        return (start <= current < end)


def tests():
    """
    will run is_dark_mode and set testMode to true
    this tells the decorator to print the function arg along with the result
    
    """
    global testMode
    testMode = True
    (is_dark_mode("21:00"))
    (is_dark_mode("05:30"))
    (is_dark_mode("12:00"))
    (is_dark_mode("20:00"))
    (is_dark_mode("06:00"))
    (is_dark_mode("19:59"))
    (is_dark_mode("06:01"))
    (is_dark_mode("00:00"))
    (is_dark_mode("23:59"))
    (is_dark_mode("02:00"))
    (is_dark_mode("03:50"))
    (is_dark_mode("01:30"))
    testMode = False
print (is_dark_mode(getTime()))