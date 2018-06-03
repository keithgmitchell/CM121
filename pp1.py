from math import *


def calc_snp_log_odds(readData): # do not modify this line
    """readData is a list of (p(read|S), p(read|S'), readID) tuples """
    no_snp = 1
    snp = 1
    for item in readData:
        snp = snp * ((item[0]*0.8) + (item[1]*0.2))
        no_snp = no_snp * (item[0])

    return (log(0.001) + log(snp))-(log(0.999) + log(no_snp))
