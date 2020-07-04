import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import os
sns.set()

os.chdir(r'C:\Users\Asus\Documents\01_code\03_projects\insurance_retention')
tc_df = pd.read_excel('resulting_sum_of_claims_dist.xlsx', index_col = 0)

fig, ax = plt.subplots()
fig.set_tight_layout(True)

# Query the figure's on-screen size and DPI. Note that when saving the figure to
# a file, we need to provide a DPI for that separately.
print('fig size: {0} DPI, size in inches {1}'.format(
    fig.get_dpi(), fig.get_size_inches()))

h = tc_df.value[1]
line, = ax.plot(tc_df.value[:500], tc_df.ret100000[:500])

plt.xticks(np.arange(0,11)* .5 * 10 ** 6, np.arange(0,5.5, .5))
plt.xlabel('sum of claims (in million Euro)')
plt.yticks(np.arange(0,.02,.0025), [str(format(x,'.2f'))+ "%" for x in np.arange(0,.02,.0025) * 100])
plt.ylabel('probability')

def update(i):
    if i< 10: label = 'Sum of claims distribution density \n under a € {0}00 000 retention'.format(i)
    if i == 10: label = 'Sum of claims distribution density \n under no retention'
    plt.title(label)
    line.set_ydata(tc_df.iloc[:500,i])
    return line, ax

anim = FuncAnimation(fig, update, frames=np.arange(1, 11), interval = 500)
anim.save(r'outputs\total_claim.gif', dpi=80, writer='imagemagick')
plt.show()
