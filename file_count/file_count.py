# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

"""
フォルダ毎のファイル数をカウント->表示
"""

if __name__ == '__main__':
    allfiles = os.walk("target")
    if allfiles:
        filelist = {}
        for dirs, subdirs, files in allfiles:
            filelist[dirs] = [subdirs, files]
        
        fig = plt.figure(figsize = (5, 3),
                         dpi = 100)
        ax1 = fig.add_subplot(1, 1, 1,
                              title = "file_count",
                              xlabel = "directory_path",
                              ylabel = "file_num")
        x1_label = filelist.keys()
        x1 = range(len(filelist))
        y1 = [len(filelist[key][1]) for key in x1_label]
        ax1.bar(x1, y1)
        ax1.set_xticks(x1)
        ax1.set_xticklabels(list(x1_label), rotation = 90)
        ax1.yaxis.set_major_locator(ticker.MaxNLocator(integer = True))
        ax1.grid(axis = "y", color = "black", ls = "--")
        fig.show()
    else:
        print("[ERROR] could not find any files.")