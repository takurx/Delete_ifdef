# coding: cp932

import sys

f = open(sys.argv[1])
data1 = f.read()  # �t�@�C���I�[�܂őS�ēǂ񂾃f�[�^��Ԃ�
f.close()

w = open(sys.argv[1] + "temp", 'w')

lines1 = data1.split('\n') # ���s�ŋ�؂�(���s�������̂��͖̂߂�l�̃f�[�^�ɂ͊܂܂�Ȃ�)

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
            output_flag = 0 #iifdef�̍s������
            ifdef_flag = 1 #iifdef�����̎n�܂�
            else_flag = 0 #������
            correspond_ifdef_count = ifdef_count #iifdef�ԍ���ێ�
        
    
    if ifdef_flag == 1:
        if line.find("#endif") >= 0:
            if ifdef_count == correspond_ifdef_count:
                output_flag = 0 #iendif�̍s�͏���
                ifdef_flag = 0 #iifdef�����͏I���
                else_flag = 0 #ielse�����͏I���
            
        
    
    if ifdef_flag == 1:
        if line.find("#elif") >= 0:
            if ifdef_count == correspond_ifdef_count:
                output_flag = 0 #ielif�̍s�͏���
                else_flag = 1 #ielse�����̎n�܂�
            
        
    
    if ifdef_flag == 1:
        if line.find("#else") >= 0:
            if ifdef_count == correspond_ifdef_count:
                output_flag = 0 #ielse�̍s�͏���
                else_flag = 1 #ielse�����̎n�܂�
            
        
    
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

