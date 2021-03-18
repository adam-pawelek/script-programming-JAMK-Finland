def division (number1, number2):
    try:
        outcome = number1 / number2
        return outcome
    except ZeroDivisionError:
        print("ZeroDivisionError you was trying divide by 0!!!!!")
    except TypeError:
        print ("One or both of your parameters are wrong type!")
  
    
