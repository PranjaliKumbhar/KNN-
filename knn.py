#To predict whether person is default or not default
#x1 is loan_amount(Independant variable)
#x2 is age(Independant variable)
#y is default or not default(dependant variable)

import math as m

#dataset
dataset=[[25000,20,"ND"],[40000,25,"ND"],
 [18000,53,"ND"],[60000,35,"ND"],
 [60000,40,"D"],[80000,45,"ND"],
 [90000,25,"D"],[100000,60,"D"],
 [150000,35,"ND"],[125000,37,"D"],
 [225000,47,"D"]
 ]

#finding deafult or not default value for x1=140000 and x2=48 then y=?

xi=140000
xj=48
len_dataset=len(dataset)

#print(len_dataset)

dist_list=[]
i=0


#calculate the euclidean distance
while(i<=len_dataset):
 d1=[ind for ind in dataset]
 #print(d1[0][0])
 dist=m.pow((d1[i][0]-xi),2)+m.pow((d1[i][1]-xj),2)
 dist_final=int(m.sqrt(dist))

 dist_list.append([dist_final,d1[i][2]])
 i=i+1

 if(i==len_dataset):
     break

#print(dist_list)
#Sorting of distances
dist_list.sort()

#print(dist_list)
#Ranking the distances
i=1

for x in dist_list:
 x.append(i)
 i=i+1

print("Distance with rank and given Category values:",end="")
print (dist_list)
#value of k=3
k=3

#Taking 3 nearest values
print("3 nearest neighbours",end="")
print(dist_list[0:k])


#Categorizing the y values
i=0
cnt_nd=0
cnt_d=0

while(i<=k):
 print(dist_list[i][1])
 if(dist_list[i][1]=="ND"):
     cnt_nd +=1
 else:
     cnt_d +=1
     
 i=i+1
 if(i==k):
     break

print("Final output",end="")
if(cnt_nd > cnt_d):
 print("For",xi,"",xj,"","Output is","ND")
else:
 print("For",xi,"",xj,"","Output is","D")
    


 
