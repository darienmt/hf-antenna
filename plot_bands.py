import os
import skrf as rf
import matplotlib.pyplot as plt
from constants import bands

def plot_bands(path, title=""):
    files_per_band = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.s1p'):
                band = file[:2]
                files_per_band[band] = os.path.join(root, file)

    
    fig = plt.figure(figsize=(12,20))
    fig.suptitle(title, fontsize=16)
    for idx, band in enumerate(bands):
        ax = fig.add_subplot(8,2, idx + 1)
        name = band["name"]
        ax.set_title(f'{name} M')
        path = files_per_band[name]
        nw = rf.Network(path, f_unit='mhz')
        nw.plot_s_vswr(ax = ax)        
        ax.get_legend().remove()
        print(f'{name} M : {nw}')
    
    fig.tight_layout()