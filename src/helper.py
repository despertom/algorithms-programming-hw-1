def check_preference(pref, n):
    pref = int(pref)
    if pref <= 0 or pref > n:
        raise ValueError("Preferences out of allowed range.")
    return pref

def check_row(pref_row, n):
    if len(pref_row) != n:
        raise ValueError("Too few/many preferences.")
    if len(set(pref_row)) != n:
        raise ValueError("Cannot use the same preference over.")
    return pref_row

# Accept user input
def get_input():
    try:
        # n must be non negative (?)
        n = int(input())
        if n < 0:
            raise ValueError("Input was negative.")
        
        # Preferences must be from 1 - n
        preferences_hospital = [
            check_row([check_preference(x, n) for x in input().split()], n) for i in range(0, n)
        ]
        
        preferences_applicant = [
            check_row([check_preference(x, n) for x in input().split()], n) for i in range(0, n)
        ]
        
        return (n, preferences_hospital, preferences_applicant)
    except ValueError as err:
        print(err)
        return