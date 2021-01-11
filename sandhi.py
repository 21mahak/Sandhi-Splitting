list_index=[]
with open('index_txt.txt') as reader:
    for line in reader.readlines():
      t=line.split(" ")
      l=t[0].split("_")
      for i in l:
        list_index.append(i)
#print(list_index)

list_noun=[]
with open('idxnoun_txt.txt') as reader:
    for line in reader.readlines():
      #  print(line)
      t=line.split(" ")
      l=t[0].split("_")
      for i in l:
        list_noun.append(i)
#print(list_noun)

list_adverb=[]
with open('idxadverb_txt.txt') as reader:
    for line in reader.readlines():
      #print(line)
      t=line.split(" ")
      l=t[0].split("_")
      for i in l:
        list_adverb.append(i)
#print(list_adverb)

list_adjective=[]
with open('idxadjective_txt.txt') as reader:
    for line in reader.readlines():
      #print(line)
      t=line.split(" ")
      l=t[0].split("_")
      for i in l:
        list_adjective.append(i)
#print(list_adjective)

#list1=[]
#with open('SuffixandPrefix.txt') as reader:
#    for line in reader.readlines():
#        #print(line)
#        line=line.rstrip("\n")
#        #print(line)
#        list1.append(line)
#len(list1)

#master_list=list1
master_list=list_noun
master_list.append(list_index)
master_list.append(list_adjective)
master_list.append(list_adverb)
#len(master_list)

sandhi_dict={}
sandhi_dict['ा']=[['','अ'],['','आ'],['ा','अ'],['ा','आ']]
sandhi_dict['ी']=[['ि','इ'],['ि','ई'],['ी','इ'],['ी','ई'],['ि'+'ः','']]
sandhi_dict['ू']=[['ु','उ'],['ु','ऊ'],['ू','उ'],['ू','ऊ'],['ु'+'ः','']]
sandhi_dict['ृ']=[['ृ','ऋ']]
sandhi_dict['े']=[['','इ'],['','ई'],['ा','इ'],['ा','ई']]
sandhi_dict['ो']=[['','उ'],['','ऊ'],['ा','उ'],['ा','ऊ'],['ः','']]
sandhi_dict['र'+'्']=[['','ऋ'],['ा','ऋ']]
sandhi_dict['ै']=[['','ए'],['','ऐ'],['ा','ए'],['ा','ऐ']]
sandhi_dict['ौ']=[['','ओ'],['','औ'],['ा','ओ'],['ा','औ']]
sandhi_dict['य']=[['ि','अ'],['ी','अ'],['े','अ'],['े','इ'],['े','उ']]
sandhi_dict['या']=[['ि','आ'],['ी','आ']]
sandhi_dict['यु']=[['ि','उ'],['ी','उ']]
sandhi_dict['यू']=[['ि','ऊ'],['ी','ऊ']]
sandhi_dict['व']=[['ू','अ'],['ु','अ'],['ो','अ'],['ो','इ'],['ो','उ']]
sandhi_dict['वा']=[['ू','आ'],['ु','आ']]
sandhi_dict['वो']=[['ू','ओ'],['ु','ओ']]
sandhi_dict['वौ']=[['ू','औ'],['ु','औ']]
sandhi_dict['वि']=[['ू','इ'],['ु','इ']]
sandhi_dict['वी']=[['ू','ई'],['ु','ई']]
sandhi_dict['वे']=[['ू','ए'],['ु','ए']]
sandhi_dict['वै']=[['ू','ऐ'],['ु','ऐ']]
sandhi_dict['ा'+'य']=[['ै','अ'],['ै','इ'],['ै','उ']]
sandhi_dict['ा'+'व']=[['ौ','अ'],['ौ','इ'],['ौ','उ']]
sandhi_dict['ल्ल']=[['त'+'्','ल']]
sandhi_dict['च्च']=[['त'+'्','च']]
sandhi_dict['च्छ']=[['त'+'्','छ']]
sandhi_dict['ज्ज']=[['त'+'्','ज']]
sandhi_dict['द्ध']=[['त'+'्','ह']]
sandhi_dict['ड्']=[['च'+'्','']]
sandhi_dict['ण'+'्']=[['ट्','']]
sandhi_dict['न'+'्']=[['त्','']]
sandhi_dict['म'+'्']=[['प्','']]
sandhi_dict['ं']=[['म'+'्','']]
sandhi_dict['ि'+'ष'+'्']=[['ि'+'ः','']]
sandhi_dict['ु'+'ष'+'्']=[['ु'+'ः','']]
sandhi_dict['ः']=[['ः','']]
sandhi_dict['र्']=[['ः','']]
sandhi_dict['ष्']=[['ः','']]
sandhi_dict['स्']=[['ः','']]
sandhi_dict['श्']=[['ः','']]
#print(sandhi_dict)

import re

count=0
total=0
with open('text_input.txt') as reader:
    for line in reader.readlines():
      m=line.split(",")
      text_input=m[0]
      f=m[1]
      s=m[2]
      final_answer=[]
      for char in sandhi_dict.keys():
        temp=re.split(char,text_input)
        if(len(temp)>1):
          temp_list=sandhi_dict[char]
          for x in temp_list:
            for d in range(len(temp)-1):
              t_f=""
              t_s=""
              j=0
              while j<=d:
                  t_f=t_f+temp[j]+char
                  j=j+1
              j=d+1
              while j<=len(temp)-1:
                  t_s=t_s+temp[j]+char
                  j=j+1
              if(m[3]=='1\n'):
                t_f=t_f[:-1]
              else:
                t_f=re.sub(char,'',t_f)
              first=t_f+x[0]
              second=x[1]+t_s
              if(m[3]=='1\n'):
                second=second[:-1]
              else:
                second=re.sub(char,'',second)
              if((first in master_list) and (second in master_list)):
                if(char=='ड्' or char=='ण'+'्' or char=='न'+'्' or char=='म'+'्'):
                  if((temp[1][0]=='म' or temp[1][0]=='न')):
                    final_answer.append([first,second])
                elif(char=='ो'):
                  if(temp[1][0]=='य' or temp[1][0]=='र' or temp[1][0]=='ल' or temp[1][0]=='व' or temp[1][0]=='ह'):
                    final_answer.append([first,second])
                elif(char=='ि'+'ः' or char=='ु'+'ष'+'्' or char=='ः'):
                  if(temp[1][0]=='क' or temp[1][0]=='ख' or temp[1][0]=='प' or temp[1][0]=='फ'):
                    final_answer.append([first,second])
                elif(char=='श्'):
                  if(temp[1][0]=='च' or temp[1][0]=='छ' or temp[1][0]=='श'):
                    final_answer.append([first,second])
                elif(char=='ष्'):
                  if(temp[1][0]=='ट' or temp[1][0]=='ठ' or temp[1][0]=='ष'):
                    final_answer.append([first,second])
                elif(char=='स्'):
                  if(temp[1][0]=='त' or temp[1][0]=='थ' or temp[1][0]=='स'):
                    final_answer.append([first,second])
                else:
                    final_answer.append([first,second])
              if(char=='य' or char=='या' or char=='यु' or char=='यू' or char=='व' or char=='वा' or char=='वो' or char=='वौ' or char=='वि' or char=='वी' or char=='वे' or char=='वै'):
                t_f=re.sub('्','',t_f)
                first=t_f+x[0]
                second=x[1]+t_s
                if((first in master_list) and (second in master_list)):
                  final_answer.append([first,second])
      #print(text_input,f,s,final_answer)
      total+=1
      for ans in final_answer:
        if(f==ans[0] and s==ans[1]):
          count+=1
          break
        else:
          continue
#print(count/total*100)
