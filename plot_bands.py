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


def plot_bands_comparative(paths, title=""):
    files_per_band_per_day = []
    for path in paths:
        files_per_band = {}
        files_per_band_per_day.append(files_per_band)
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
        for files_per_band in files_per_band_per_day:
            path = files_per_band[name]
            nw = rf.Network(path, f_unit='mhz')
            nw.plot_s_vswr(ax = ax, label=f'{path}')     
            print(f'{name} M : {nw}')
        
    
    fig.tight_layout()

def plot_all_in_one(paths, title="", legends=None):
    fig = plt.figure(figsize=(15,5))      
    ax = fig.add_subplot(1,1,1)
    ax.set_title(title)
    for idx, path in enumerate(paths):
        nw = rf.Network(os.path.join(path, "All.s1p"), f_unit='mhz')
        label = path if legends is None else legends[idx]
        nw.plot_s_vswr(ax = ax, label=label)
    for band in bands:
        ax.axvline(x = band['low']*1000000, color='black', linestyle='--')
        ax.axvline(x = band['up']*1000000, color='black', linestyle='--')
        
    ax.set_facecolor("darkgray" if len(paths) > 1 else "white")
    fig.tight_layout()
