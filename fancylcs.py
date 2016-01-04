def fancyLCS(S1, S2):
    if S1 == '' or S2 == '':
        return [0, pound(S1), pound(S2)]
    if S1[0] == S2[0]:
        temp = fancyLCS(S1[1:], S2[1:])
        return [temp[0]+1, S1[0]+temp[1], S2[0]+temp[2]]
    t1 = fancyLCS(S1[1:], S2)
    t2 = fancyLCS(S1, S2[1:])
    if t1[0] > t2[0] or t1[0] == t2[0]:
        return [t1[0], '#'+t1[1], t2[1]]
    return [t2[0], t1[1], '#'+t2[1]]

def pound(st):
    return ''.join(['#' for x in xrange(len(st))])

print fancyLCS("human", "chimpanzee")