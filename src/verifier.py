from helper import get_input

# verifier.py outputs:
#   VALID STABLE
#   INVALID: <reason>
#   UNSTABLE: <example blocking pair>
# if both INVALID and UNSTABLE, report INVALID

def verify_validity(n, matching: dict[int, int]) -> tuple[bool, str]:
    if n == 0:
        return True, ""
    
    #hospitals must be 1...n and appear once
    hospital_ids = set(matching.keys())
    needed_hospital_ids = set(range(1, n+1))
    if hospital_ids != needed_hospital_ids:
        missing = sorted(needed_hospital_ids - hospital_ids)
        extra = sorted(hospital_ids - needed_hospital_ids)
        if missing:
            return False, f"INVALID: Missing hospital IDs: {missing}"
        if extra:
            return False, f"INVALID: Extra hospital IDs: {extra}"
        return False, "INVALID: hospitals not exactly 1...n"
    
    #student verification
    students = list(matching.values())
    if any((s < 1 or s > n) for s in students):
        return False, "INVALID: student ID out of range"
    if len(set(students)) != n:
        return False, "INVALID: student assigned to multiple hospitals"
    
    needed_students = set(range(1, n+1))
    if set(students) != needed_students:
        missing = sorted(needed_students - set(students))
        extra = sorted(set(students) - needed_students)
        if missing:
            return False, f"INVALID: Missing student IDs: {missing}"    
        if extra:
            return False, f"INVALID: Extra student IDs: {extra}"
        return False, "INVALID: students not exactly 1...n"
    
    return True, ""

def verify_stability(n: int, hospital: list[list[int]], student: list[list[int]], matching: dict[int, int]) -> tuple[bool, str]:
    if n == 0:
        return True, ""

    #invert matching to get student -> hospital so that looking up is faster
    inv = {s: h for h, s in matching.items()}
    #rank tables
    h_rank = [dict() for _ in range(n)]
    s_rank = [dict() for _ in range(n)]
    for h in range(1, n+1):
        for i, s in enumerate(hospital[h-1]):
            h_rank[h][s] = i
    for s in range(1, n+1):
        for i, h in enumerate(student[s-1]):
            s_rank[s][h] = i
    
    #look for blocking pair (h, s)
    for h in range(1, n+1):
        curr_s = matching[h]
        for s in range(1, n+1):
            if s == curr_s:
                continue
            #check if h prefers s and if s perfers h
            if h_rank[h][s] < h_rank[h][curr_s]:
                curr_h = inv[s]
                if s_rank[s][h] < s_rank[s][curr_h]:
                    return False, f"UNSTABLE: blocking pair ({h}, {s})"
                
    return True, ""