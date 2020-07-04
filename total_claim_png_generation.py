import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import os
sns.set()

os.chdir(r'C:\Users\Asus\Documents\01_code\03_projects\insurance_retention')
tc_df = pd.read_excel('resulting_sum_of_claims_dist.xlsx', index_col = 0)
tc_df = tc_df[:500]

k = 1
for key in tc_df.keys()[1:11]:
    if k < 10: lab = f'retention: € {k}00 000'
    if k == 10: lab = 'no retention'
    k += 1
    plt.plot('value', key, data = tc_df, label = lab)

plt.legend()
plt.title('Sum of claims distribution density under various retentions')
plt.xticks(np.arange(0,11) * .5 * 10 ** 6, np.arange(0,5.5,.5))
plt.xlabel('Sum of claims (in million Euro)')
plt.yticks(np.arange(0,.02,.005), [str(round(x,2))+ "%" for x in np.arange(0,.02,.005) * 100])
plt.ylabel('probability')
plt.savefig(r'outputs\total_claim.png')
plt.show()
