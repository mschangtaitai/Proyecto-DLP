
def move(states, sign, trans):
    response = []
    for i in trans:
        if((i[2] not in response) and (i[1] == sign) and (i[0] in states)):
            response.append(i[2])
    return response

def eClosure(states, trans):
    response = states.copy()
    added = True
    while (added):
        added = False
        for i in trans:
            if((i[2] not in response) and (i[1] == "E") and (i[0] in response)):
                response.append(i[2])
                added = True
    return response

class AF:
    def __init__(self, states, sigma, trans, start, finals):
        self.states = states
        self.sigma = sigma
        self.trans = trans
        self.start = start
        self.finals = finals
        