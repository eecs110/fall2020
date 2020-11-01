try:
    # wrap the "try" block around the thing that may potentially error:
    val = 'adasdasdasdasdas'
    result = int(val)
except:
    # write some code that will gracefully handle the error in the event
    # that the error happens:
    print(val, 'cannot be converted to an int!')