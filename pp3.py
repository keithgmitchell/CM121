def align(X, Y, S, g):  # do not change this line
    """X, Y are two sequences to align, S is substitution score[x][y] and g is the gap penalty"""
    # replace this with your actual calculation
    i = 1
    scores = [[0 for x in range(len(X)+1)] for y in range(len(Y)+1)]  # scores[t][u] = optimal score for aligning first t letters of X, u letters of Y
    moves = [[0 for x in range(len(X)+1)] for y in range(len(Y)+1)]
    while i <= len(X) and i <= len(Y):
        scores[0][i] = i*g
        scores[i][0] = i*g
        moves[0][i] = 'x'
        moves[i][0] = 'y'
        i += 1

    for x in range(1, len(Y) + 1):
        current_x = Y[x-1]
        for y in range(1, len(X) + 1):
            current_y = X[y-1]
            scores[x][y] = max((scores[x-1][y] + g), (scores[x][y-1] + g), (scores[x-1][y-1] + S[current_x][current_y]))
            if scores[x][y]==scores[x-1][y] + g:
                moves[x][y] = 'y'
            elif scores[x][y] == scores[x][y-1] + g:
                moves[x][y] = 'x'
            elif scores[x][y] == scores[x-1][y-1] + S[current_x][current_y]:
                moves[x][y] = 'm'

    path = []

    while x != 0 and y != 0:
        if moves[x][y] == 'm':
            path.append([y-1,x-1])
            x-=1
            y-=1
        if moves[x][y] == 'x':
            # path.append([y-1, x])
            y -= 1
        if moves[x][y] == 'y':
            # path.append([y, x-1])
            x -= 1

    reverse_path = []

    for i in reversed(path):
        reverse_path.append(i)

    # print reverse_path
    return reverse_path