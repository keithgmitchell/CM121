from scipy import stats


def get_sorted_hits(geneData): # do not modify this line
    """geneData is list of (size, k, gene) tuples"""
    hits = []
    count = 0
    sum_all = 0
    sum_k = 0
    for gene in geneData:
        sum_all += gene[0]
        sum_k += gene[1]
    #alpha = (1.0/sum_k)
    alpha = 0.0025
    for gene in geneData:
        hit = []
        x = stats.poisson.pmf(gene[1], sum_k*(gene[0]/sum_all), loc=0) + \
            stats.poisson.sf(gene[1], sum_k*(gene[0]/sum_all), loc=0)
        hit.append([x, count])
        count += 1
        hits.append(hit)

    hits = sorted(hits, key=lambda tup: tup[0])
    # hits = list(hits)
    # print hits[0], alpha
    return hits[0], alpha
