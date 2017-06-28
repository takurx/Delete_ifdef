# coding: cp932

import sys

f = open(sys.argv[1])
data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()

w = open(sys.argv[1] + "temp", 'w')

lines1 = data1.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)

output_flag = 1
ifdef_flag = 0
else_flag = 0
ifdef_count = 0
correspond_ifdef_count = 0
for line in lines1:
    if line.find("#ifdef") >= 0 or line.find("#ifndef") >= 0 or line.find("#if") >= 0:
        ifdef_count = ifdef_count + 1;
    
    if line.find("#ifdef _ML6X00") >= 0:
        if line.find("_MULTI") == -1 and line.find("TEST") == -1 and line.find("_MULTI2") == -1:
            output_flag = 0 #iifdefの行を消す
            ifdef_flag = 1 #iifdef部分の始まり
            else_flag = 0 #初期化
            correspond_ifdef_count = ifdef_count #iifdef番号を保持
        
    
    if ifdef_flag == 1:
        if line.find("#endif") >= 0:
            if ifdef_count == correspond_ifdef_count:
                output_flag = 0 #iendifの行は消す
                ifdef_flag = 0 #iifdef部分は終わり
                else_flag = 0 #ielse部分は終わり
            
        
    
    if ifdef_flag == 1:
        if line.find("#elif") >= 0:
            if ifdef_count == correspond_ifdef_count:
                output_flag = 0 #ielifの行は消す
                else_flag = 1 #ielse部分の始まり
            
        
    
    if ifdef_flag == 1:
        if line.find("#else") >= 0:
            if ifdef_count == correspond_ifdef_count:
                output_flag = 0 #ielseの行は消す
                else_flag = 1 #ielse部分の始まり
            
        
    
    if line.find("#endif") >= 0:
        ifdef_count = ifdef_count - 1;
    
    if output_flag == 1:
        w.write(eval(repr(line)) + "\n")
    
    if output_flag == 0:
        output_flag = 1
        
    
    if ifdef_flag == 1:
        if else_flag == 1:
            output_flag = 0
        
    

w.close()

