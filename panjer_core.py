# improvements
# - other claim number distirbutions: nbi, po
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# input
# claim distribution
CLAIM_DF = pd.read_excel("synthetic_claim_size_dist.xlsx", index_col = 0)
# binomial parameter
N_DIST = 'bi'
N = 10000
P = .0016

class Claim_under_retention:
    def __init__(self):
        self.dist_df = CLAIM_DF

    def set_retention(self, retention):
        self.retention = retention
        prob_over_retention = CLAIM_DF.dist[CLAIM_DF.value>= retention].sum()
        self.dist_df = (CLAIM_DF[CLAIM_DF.value < retention]
            .append({'value': retention, 'dist': prob_over_retention},
            ignore_index=True))

def panjer(df = CLAIM_DF):
    # data preperation
    h = df.value[1] - df.value[0]
    min_claim = df.value[0]

    def f(k):
        max_k = len(df) + int(min_claim / h) - 1
        if k <=  max_k and k >= min_claim / h:
            res = df.dist[k - int(min_claim / h )]
        else: res = 0
        return res

    # panjer
    a = P / (P - 1.0)
    b = P * (N + 1.0) / (1.0 - P)
    p0 = (1.0 - P) ** N
    g = np.zeros(1000)
    g[0] = p0
    for k in range(1, 1000):
        inc = 0
        for j in range(1, k + 1):

            inc += (a + b * j / k) * f(j) * g[k - j]
        g[k] = inc
    return(g)

def results():
    h = CLAIM_DF.value[1] - CLAIM_DF.value[0]
    total_claim_df = pd.DataFrame({'value': range(0, 1000 * h, h)})

    retentions = [1 * k * 10 ** 5 for k in range(1,11)]

    for retention in retentions:
        c = Claim_under_retention()
        c.set_retention(retention)
        total_claim_prob_retention = panjer(c.dist_df)
        total_claim_df['ret'+ str(retention)] = total_claim_prob_retention


    total_claim_prob_no_retention = panjer()
    total_claim_df['no ret'] = total_claim_prob_no_retention

    total_claim_df.to_excel("resulting_sum_of_claims_dist.xlsx")
    print(total_claim_df.head())

if __name__ == "__main__":
    results()
