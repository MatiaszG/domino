def execute_algorithm(setup):

    new_setup = []
    if(setup[0] == '|' and setup[1] == '\\'):
        new_setup.append('\\')
    else:
        new_setup.append(setup[0])

    force = 0
    for j in range(1, len(setup)-1):
        new_state = setup[j]
        if(setup[j] == '|'):
            if(setup[j-1] == '/'):
                force += 1
            if(setup[j+1] == '\\'):
                force -= 1
            if(force < 0):
                new_state = '\\'
            elif (force > 0):
                new_state = '/'
            force = 0
        new_setup.append(new_state)

    if(setup[len(setup)-1] == '|' and setup[len(setup)-2] == '/'):
        new_setup.append('/')
    else:
        new_setup.append(setup[len(setup)-1])
    return new_setup


def execute_inverted_algorithm(setup):
    pass
