print("Enter the XOR Truth Table:")
x1=[]
x2=[]
y=[]

for i in range(0,4):
    i1=input("Enter values of X1:")
    x1.append(i1)

for i in range(0,4):
    i2=input("Enter values of X2:")
    x2.append(i2)


for i in range(0,4):
    i3=input("Enter values of Y:")
    y.append(i3)
    
print ("X1  X2  Y")
i=0
while i <=len(x1):
    
    print(x1[i]," ",x2[i],"  ",y[i])
    i=i+1
    if(i==len(x1)):
        break

print("y1=x1.x2(bar)")
print("New XOR Truth Table:")
y1=[0,0,1,0]
i=0
while i <=len(x1):
    
    print(x1[i]," ",x2[i],"  ",y1[i])
    i=i+1
    if(i==len(x1)):
        break



#c1
print("Assume Both weights are excitory i.e w1=w2=1")

yin1=[]
w1=1
w2=1
i=0
while i <=len(x1):
    add=int(x1[i]*w1)+int(x2[i]*w2)
    yin1.append(add)
    print("yin=",x1[i],"*",w1,"+",x2[i],"*",w2,"=",add)
    i=i+1
    if(i==len(x1)):
        break

print("Maximum from yin1=",max(yin1))

print("assign max to \u03B8 i.e \u03B8=",max(yin1))

print ("We get....")
yyin1=[]
i=0
while i<=len(x1):
    if(yin1[i]>=max(yin1)):
        yyin1.append('1')
    else:
        yyin1.append('0')

    i=i+1
    if(i==len(x1)):
        break

print("y1 y")

i=0
while i <=len(x1):
    
    print(y1[i]," ",yyin1[i])
    i=i+1
    if(i==len(x1)):
        break

print("y1 is not equal to y")
print ("These weights are not suitable")



#c2
print("Assume one weight excitory and other inhibitory i.e w1=1 & w2=-1")

w1=1
w2=-1
yin2=[]
i=0
y=[0,0,1,0]
while i <=len(x1):
    a=int(x2[i])*int(w2)
    add=int(x1[i]*w1)+a
    yin2.append(add)
    print("yin=",x1[i],"*",w1,"+",x2[i],"*",w2,"=",add)
    i=i+1
    if(i==len(x1)):
        break

print("Maximum from yin2=",max(yin2))

print("assign max to \u03B8 i.e \u03B8=",max(yin2))

print ("We get....")
yyin2=[]
i=0
while i<=len(x1):
    if(yin2[i]>=max(yin2)):
        yyin2.append('1')
    else:
        yyin2.append('0')

    i=i+1
    if(i==len(x1)):
        break

print("y1 y")

i=0
while i <=len(x1):
    
    print(y1[i]," ",yyin2[i])
    i=i+1
    if(i==len(x1)):
        break

print("y1 is equal to y")

print ("These weights are suitable and final weights are w1=1 & w2=-1 for y1")


#c3
print("y2=x1(bar).x2")

print("New XOR Truth Table:")
y2=[0,1,0,0]
i=0
while i <=len(x1):
    
    print(x1[i]," ",x2[i],"  ",y2[i])
    i=i+1
    if(i==len(x1)):
        break


print("Assume both weights are excitory i.e w1=w2=1")

w1=1
w2=1
i=0
yin3=[]
y=[0,0,0,1]
while i <=len(x1):
    add=int(x1[i]*w1)+int(x2[i]*w2)
    yin3.append(add)
    print("yin=",x1[i],"*",w1,"+",x2[i],"*",w2,"=",add)
    i=i+1
    if(i==len(x1)):
        break
print("Maximum from yin3=",max(yin3))

print("assign max to \u03B8 i.e \u03B8=",max(yin3))

print ("We get....")
yyin3=[]
i=0
while i<=len(x1):
    if(yin3[i]>=max(yin3)):
        yyin3.append('1')
    else:
        yyin3.append('0')

    i=i+1
    if(i==len(x1)):
        break

print("y2 y")

i=0
while i <=len(x1):
    
    print(y2[i]," ",yyin3[i])
    i=i+1
    if(i==len(x1)):
        break

print("y2 is not equal to y")

print ("These weights are not suitable")


#c4
print("Assume one weight excitory and other inhibitory i.e w1=1 & w2=-1")

w1=1
w2=-1
yin4=[]
i=0
y=[0,0,1,0]
while i <=len(x1):
    a=int(x2[i])*int(w2)
    add=int(x1[i]*w1)+a
    yin4.append(add)
    print("yin=",x1[i],"*",w1,"+",x2[i],"*",w2,"=",add)
    i=i+1
    if(i==len(x1)):
        break

print("Maximum from yin4=",max(yin4))

print("assign max to \u03B8 i.e \u03B8=",max(yin4))

print ("We get....")
yyin4=[]
i=0
while i<=len(x1):
    if(yin2[i]>=max(yin4)):
        yyin4.append('1')
    else:
        yyin4.append('0')

    i=i+1
    if(i==len(x1)):
        break

print("y2 y")

i=0
while i <=len(x1):
    
    print(y2[i]," ",yyin4[i])
    i=i+1
    if(i==len(x1)):
        break

print("y2 is not equal to y")

print ("These weights are not suitable")


#c5

print("Assume one weight inhibitory and other excitory i.e w1=-1 & w2=1")

w1=-1
w2=1
yin5=[]
i=0
while i <=len(x1):
    a=int(x2[i])*int(w2)
    add=(int(x1[i])*int(w1))+a
    yin5.append(add)
    print("yin=",x1[i],"*",w1,"+",x2[i],"*",w2,"=",add)
    i=i+1
    if(i==len(x1)):
        break

print("Maximum from yin5=",max(yin5))

print("assign max to \u03B8 i.e \u03B8=",max(yin5))

print ("We get....")
yyin5=[]
i=0
while i<=len(x1):
    if(yin5[i]>=max(yin5)):
        yyin5.append('1')
    else:
        yyin5.append('0')

    i=i+1
    if(i==len(x1)):
        break

print("y3 y")

i=0
while i <=len(x1):
    
    print(y2[i]," ",yyin5[i])
    i=i+1
    if(i==len(x1)):
        break

print("y3 is equal to y")

print ("These weights are suitable and final weights are w1=-1 & w2=1 for y3")


#c6

print("yin=y1.v1+y2.v2")

print("X1 X2 Y Y1 Y2")

i=0
while i <=len(x1):
    
    print(x1[i]," ",x2[i],"  ",y[i]," ",y1[i]," ",y2[i])
    i=i+1
    if(i==len(x1)):
        break


print ("Assume value of v1 and v2 be excitory")

yin7=[]
v1=1
v2=1
i=0
while i <=len(x1):
    a=int(y2[i])*int(v2)
    add=(int(y1[i])*int(v1))+a
    yin7.append(add)
    print("yin=",y1[i],"*",v1,"+",y2[i],"*",v2,"=",add)
    i=i+1
    if(i==len(x1)):
        break

print("Maximum from yin7=",max(yin7))

print("assign max to \u03B8 i.e \u03B8=",max(yin7))

print ("We get....")
yyin7=[]
i=0
while i<=len(x1):
    if(yin7[i]>=max(yin7)):
        yyin7.append('1')
    else:
        yyin7.append('0')

    i=i+1
    if(i==len(x1)):
        break

print("y  y")
y=[0,1,1,0]
i=0
while i <=len(x1):
    
    print(y[i]," ",yyin7[i])
    i=i+1
    if(i==len(x1)):
        break

print("y is equal to y")

print ("These weights are suitable and final weights are v1=1 & v2=1")

