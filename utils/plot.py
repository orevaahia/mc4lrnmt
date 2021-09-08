import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

plt.rcParams['figure.dpi'] = 110
sns.set_context("poster")
plt.rcParams["axes.labelsize"] = 15

def plot_scores(data: pd.DataFrame, x_axis: str, y_axis: str, hue: str, 
                        save_path: str, y_tick_spacing: int, path_to_results: str):

    plot_path = os.path.join(path_to_results, save_path)
    
    f = plt.figure(figsize=(10, 10))
    tick_spacing = 20
    y_tick_spacing = y_tick_spacing
    fig, ax = plt.subplots(1,1)
    
    #colors = ["#697b30", "#c87b7c"]
    
    with sns.axes_style("ticks"): 
        sns.set_palette("cubehelix")
        sns.lineplot(data=data, x=x_axis, y=y_axis, hue=hue, markers=True, style=hue)
        ax.lines[1].set_linestyle(":")
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_spacing))
        sns.despine()
        plt.yticks(np.arange(18, 3, 40), size=14)
        plt.xticks(np.arange(0, 101, 10), size=14)
     
    plt.legend(loc='right', bbox_to_anchor=(1.2, 1));
    plt.legend(fontsize=10, title_fontsize='8')
  
    
    plt.savefig(plot_path)