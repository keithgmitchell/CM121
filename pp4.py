def calc_fb(liks, ptrans, prior): # don't change this line
    '''liks is list of (p(roll|F), p(roll|L)); ptrans is p[from][to];
    prior is (p(F), p(L))'''

    forward = [(1., 1.)]
    backward = [(0, 0)]  # replace this with your calculation
    ppost = [(0, 0)]
    pobs = [1.]

    forward[0] = [prior[0]*liks[0][0], prior[1]*liks[0][1]]

    for x in range(1, len(liks)):
        forward.append([(liks[x][0] * ptrans[0][0] * forward[x - 1][0] +
                         liks[x][0] * ptrans[1][0] * forward[x - 1][1]),
                        (liks[x][1] * ptrans[1][1] * forward[x - 1][1] +
                         liks[x][1] * ptrans[0][1] * forward[x - 1][0])])
        backward.append([0, 0])

    backward[x] = [1.0, 1.0]
    x -= 1

    while not(x < 0):
        backward[x] = ([(ptrans[0][0] * liks[x + 1][0] * backward[x + 1][0] +
                         ptrans[0][1] * liks[x + 1][1] * backward[x + 1][1]),
                        (ptrans[1][0]) * liks[x + 1][0] * backward[x + 1][0] +
                        ptrans[1][1] * liks[x + 1][1] * backward[x + 1][1]])
        x -= 1

    for x in range(0, len(liks)):
        if x == 0:
            pobs[x] = (forward[x][0] * backward[x][0] + forward[x][1] * backward[x][1])
            ppost[x] = [((forward[x][0] * backward[x][0]) / pobs[x]),((forward[x][1] * backward[x][1]) / pobs[x])]
        else:
            pobs.append(forward[x][0] * backward[x][0] + forward[x][1] * backward[x][1])
            ppost.append([((forward[x][0] * backward[x][0]) / pobs[x]), ((forward[x][1] * backward[x][1]) / pobs[x])])

    return forward, backward, pobs, ppost
