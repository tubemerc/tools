# -*- coding: utf-8 -*-
import glob
import os

"""
拡張子を指定して......
a : ファイル名を全て数字に変換
f : ファイル名の先頭に数字を追加
e : ファイル名の末尾に数字を追加
"""

if __name__ == '__main__':
    _path = ""
    
    input_fe = input("拡張子>> ")
    path = _path + "*." + input_fe
    filelist = glob.glob(path)
    
    if filelist:
        print("before:", filelist)
        
        input_switch = input("switch>> ")        
        if input_switch == "a":
            i = 1
            for file in filelist:
                os.rename(file, _path + str(i) + "." + input_fe)
                i += 1
        elif input_switch == "f":
            i = 1
            for file in filelist:
                _file = file.rsplit("\\", 1)
                _file = _file[1].rsplit(".", 1)
                print(_file[0])
                os.rename(file, _path + str(i) + _file[0] + "." + input_fe)
                i += 1
        elif input_switch == "e":
            i = 1
            for file in filelist:
                _file = file.rsplit("\\", 1)
                _file = _file[1].rsplit(".", 1)
                print(_file[0])
                os.rename(file, _path + _file[0] + str(i) + "." + input_fe)
                i += 1
        else:
            print("[ERROR] wrong input_switch.")
            
        filelist = glob.glob(path)
        print("after:", filelist)
    else:
        print("[ERROR] could not find any files.")