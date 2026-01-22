from helper import get_input, get_output

def match(n, hospital: list[list], applicant: list[list]):
    # Contains sets indexed by hospital ID
    free_hospitals: list = [i+1 for i in range(0, n)]
    free_applicants: list = [i+1 for i in range(0, n)]
    # Matching storing hospital -> applicant
    matching: dict = {};
    while len(free_hospitals) != 0 and len(hospital[free_hospitals[0]-1]) != 0:
        # Choose a hospital h
        h = free_hospitals[0]
        # Choose first applicant on h's list to whom h has not been matched
        a = hospital[h-1].pop(0)
        # Find h_prime
        h_prime_list = [hos for hos, app in matching.items() if app == a]
        h_prime = h_prime_list[0] if len(h_prime_list) > 0 else None
        if a in free_applicants:
            # a is free
            matching[h] = a
            free_hospitals.remove(h)
            free_applicants.remove(a)
        elif applicant[a-1].index(h) < applicant[a-1].index(h_prime):
            # a prefers h to current assingment
            matching[h] = a
            free_hospitals.append(h_prime)
        else:
            # a rejects h
            pass
    return matching


if __name__ == "__main__":
    data = get_input()
    if data is not None:
        matching = match(data[0], data[1], data[2])
        print(get_output(matching))