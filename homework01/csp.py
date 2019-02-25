from tools.aima.csp import min_conflicts, CSP, parse_neighbors, backtracking_search


def course_scheduling():
    """
    """
    inst = ['adams', 'bailey', 'plantinga', 'schuurman', 'vlinden']
    time = ['mwf900', 'mwf1030', 'mwf1330', 'tth1030', 'tth1800']
    room = ['sb382', 'nh253']
    variables = ['cs108', 'cs112', 'cs212', 'cs342', 'cs374', 'cs344', 'is371']
    domain = {}
    assignment = {'cs108': 'schuurman', 'cs112': 'adams', 'cs212': 'plantinga',
                  'cs374': 'adams', 'cs344': 'vlinden', 'is371': 'bailey',
                  'cs342': 'bailey'}

    # Parsing neighbors: each two courses.
    neighbors = parse_neighbors("""cs108: cs112;
                cs112: cs212; 
                cs212: cs342; 
                cs342: cs374;
                cs374: cs344; 
                cs344: is371;
                is371: cs108""", variables)

    for var in variables:
        for A in var:
            for B in var:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    for var in variables:
        domain[var] = []
        for instructors in inst:
            for time_slot in time:
                for room_num in room:
                    domain[var].append([instructors, time_slot, room_num])

    def course_constraints(A, a, B, b, recurse=0):
        """
        If different courses have the same room, same time, then fails
        If different courses have the same inst, same time, then fails
        If courses have the different inst from assignment, then fails
        A: Variable 1
        B: Variable 2
        a: attribute list of Variable 1
        b: attribute list of Variable 2
        [0]: instructor
        [1]: time
        [2]: room
        """
        # check inst assignments:
        if assignment[A] != a[0] and assignment[B] != b[0]:
            return False

        # check same room and same time
        if a[1] == b[1] and a[2] == b[2]:
            return False

        # check same inst and same time
        if a[1] == b[1] and a[0] == b[0]:
            return False

        return True

    return CSP(variables, domain, neighbors, course_constraints)


p = course_scheduling()
# solution = backtracking_search(p)
solution = min_conflicts(p)
print(solution)