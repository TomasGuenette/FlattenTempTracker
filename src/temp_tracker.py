#List of temperatures
Temperatures = []

#Record a new temperature
def insert(newTemp):
    if(0<=newTemp<=110):
        Temperatures.append(newTemp)
    else:
        raise ValueError('Temperature wasnt between 0 and 110 F')

#Returns the highest temperature seen so far.
def get_max():
    return max(Temperatures)

#Returns the lowest temperature seen so far.
def get_min():
    return min(Temperatures)

#Returns the mean of all temperatures seen so far.
def get_mean():
    return sum(Temperatures)/len(Temperatures)