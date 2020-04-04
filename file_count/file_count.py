# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import docx2txt
import re

"""
フォルダ毎のファイル数をカウント->表示
フォルダに含まれる.docxファイルの文字数もカウント(空白文字"\s"は除外)
"""

if __name__ == '__main__':
    allfiles = os.walk("target")
    if allfiles:
        filelist = {}
        wordnum = {}
        for dirs, subdirs, files in allfiles:
            filelist[dirs] = [subdirs, files]
            wordnum[dirs] = 0
            for file in files:
                if ".docx" in file:
                    wordnum[dirs] +=\
                        len(re.sub("\s", "", docx2txt.process(dirs+"/"+file)))
        # グラフ描写
        fig = plt.figure(figsize = (5, 5), dpi = 100)   
        ax1 = fig.add_subplot(211,
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
        
        ax2 = fig.add_subplot(212,
                              title = "word_num",
                              xlabel = "directory_path",
                              ylabel = "word_num")
        x2_label = wordnum.keys()
        x2 = range(len(wordnum))
        y2 = [wordnum[key] for key in x2_label]
        ax2.bar(x2, y2)
        ax2.set_xticks(x2)
        ax2.set_xticklabels(list(x2_label), rotation = 90)
        ax2.yaxis.set_major_locator(ticker.MaxNLocator(integer = True))
        ax2.grid(axis = "y", color = "black", ls = "--")
        fig.show()
    else:
        print("[ERROR] could not find files.")