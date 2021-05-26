import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Randomplot
import nearestplot
import learningplot
import communicationplot
sns.set_theme(style="darkgrid")



data_preproc = pd.DataFrame({
    'Times': Randomplot.random_times[:27350],  #27350
    'Random': Randomplot.random_times_total[:27350],
    'Nearest': nearestplot.nearest_times_total[:27350],
    'Learning': learningplot.learning_times_total[:27350],
    'Communicating': communicationplot.communication_times_total[:27350]
    })


sns.lineplot(x='Times', y='value', hue='variable', data=pd.melt(data_preproc, ['Times'])).set_title("Time that Clients wait for a ride")


plt.show()