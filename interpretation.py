import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
sns.set()

os.chdir(r'C:\Users\Asus\Documents\01_code\03_projects\insurance_retention')
tc_df = pd.read_excel(r'resulting_sum_of_claims_dist.xlsx', index_col = 0)

print(tc_df.shape)

q0 = .995

def safety(i = 1, q = q0):
    h = 10000
    q_sum = 0
    k = 0
    while q_sum < .995:
        q_sum += tc_df.iloc[k, i]
        k += 1
    return k * h

ret_mean = [sum(tc_df.iloc[:, 1] * tc_df.value)]
ret_sd = [(sum(tc_df.iloc[:, 1] * (tc_df.value ** 2)) - sum(tc_df.iloc[:, 1] * tc_df.value) ** 2) ** .5]
ret_safety = [safety()]
for x in range(2,len(tc_df.columns)):
    ret_mean.append(sum(tc_df.iloc[:, x] * tc_df.value))
    ret_sd.append((sum(tc_df.iloc[:, x] * (tc_df.value ** 2)) - sum(tc_df.iloc[:, x] * tc_df.value) ** 2) ** .5)
    ret_safety.append(safety(i = x))

ret_summary_df = pd.DataFrame({'mean': ret_mean,
                               'sd': ret_sd,
                               str(q0 * 100)+'% safety': ret_safety}, index = tc_df.columns[1:])


print(ret_summary_df)
ret_summary_df.to_excel("summary.xlsx")

# 99.5% safety capital
plt.bar(range(1,12), [x / 10 ** 6 for x in ret_safety], label = str(q0 * 100)+'% safety capital')
plt.bar(range(1,12), [x / 10 ** 6 for x in ret_mean], label = 'expected sum of claims')
plt.legend()
plt.xticks(range(1,12),[str(x / 10.0) for x in range(1, 11)] + ['no'])
plt.title('Needed capital by retention')
plt.xlabel("retention (in million Euro)")
plt.ylabel("sum of claims (in million Euro)")
plt.savefig('outputs\SafetyCapital.png')
plt.show()
