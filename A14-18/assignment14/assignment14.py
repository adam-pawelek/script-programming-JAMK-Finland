def division (number1, number2):
    try:
        outcome = number1 / number2
        return outcome
    except ZeroDivisionError:
        print("ZeroDivisionError you was trying divide by 0!!!!!")
    
