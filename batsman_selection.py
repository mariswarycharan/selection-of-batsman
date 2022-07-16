



# from calculator import square


# from statistics import variance


from cProfile import label
from itertools import count
from matplotlib import markers
from numpy import count_nonzero
import matplotlib.pyplot as plt 

# import matplotlib.pyplot as sample


rahul = [10,0,100,20,20,9,7]
ajay = [40,30,40,30,40,30,4]



mean_rahul = sum(rahul)/len(rahul)
mean_ajay = sum(ajay)/len(ajay)

print("mean of rahul is",round(mean_rahul))
print("mean of ajay is ",round(mean_ajay))

if len(rahul)%2 != 0:
    rahul.sort()
    
    d =round(len(rahul)/2 -0.5)
    
    m1 = rahul[d]
    print("madium of rahul is ",m1)

if len(rahul)%2 == 0:
    rahul.sort()
    
    d = round(len(rahul)/2) 
    r = d - 1
    
    m1 = rahul[d]
    m2 = rahul[r]
    sum = m1   + m2 
    div = sum / 2
    print("madium of rahul is ",div)
    
    
if len(ajay)%2 != 0:
    ajay.sort()
    
    d =round(len(ajay)/2 -0.5)
    
    m1 = ajay[d]
    print("madium of ajay is ",m1)

if len(ajay)%2 == 0:
    ajay.sort()
    
    d = round(len(ajay)/2) 
    r = d +1
    m1 = ajay[d]
    m2 = ajay[r]
    sum = m1   + m2 
    div = sum / 2 
    print("madium of ajay is ",div)
    
    
"----------------------variance-------------------------------------"

stardard_deviation_rahul = []

for i in rahul:
    deviation = mean_rahul - i
    stardard_deviation_rahul.append(round(deviation))
    
# print(stardard_deviation)

squared_list_rahul = []

for i in stardard_deviation_rahul:
    squ = i**2
    squared_list_rahul.append(squ)
    
    
# print(squared_list)

list_sum  = sum(squared_list_rahul) 

# print(list_sum)

number = len(squared_list_rahul) - 1
variance_rahul = list_sum / number

print("variance of rahul is ",round(variance_rahul))        
    

"-------------------------------------------------------------------------------------------------------------------------------------"


stardard_deviation_ajay = []

for i in ajay:
    deviation_a = mean_ajay - i
    stardard_deviation_ajay.append(round(deviation_a))
    
# print(stardard_deviation)

squared_list_ajay = []

for i in stardard_deviation_ajay:
    squ_a = i**2
    squared_list_ajay.append(squ_a)
    
    
# print(squared_list)

list_sum_a  = sum(squared_list_ajay) 

# print(list_sum)

number_a = len(squared_list_ajay) - 1
variance_ajay = list_sum_a / number_a

print("variance of ajay is ",round(variance_ajay))
print("stardard_deviation of rahul",squared_list_rahul)
print("stardard_deviation of ajay", squared_list_ajay)        
    

count_rahul = []
list_r = []
l2 = []
n1 = 0



for i in rahul:
    
    z= rahul.count(i)
    count_rahul.append(z)
    list_r.append(z)
    list_r.append(i)
        
v_r= max(count_rahul)

if v_r == 1:
    print("rahul has no mode")
    
    
if v_r > 1:

    for j in list_r:
        if j == v_r:
            id_r = list_r.index(j,n1)
            n1 = id_r +1
            l2.append(list_r[id_r + 1])
            

            
    print("mode of rahul is",list(set(l2)))


"------------------------------------------------------------------------------------------------------------------------"


count_ajay = []
list_a = []
l1 = []
n = 0



for i in ajay:
    
    z= ajay.count(i)
    count_ajay.append(z)
    list_a.append(z)
    list_a.append(i)
        
v = max(count_ajay)

if v == 1:
    print("ajay has no mode")
    
    
if v > 1:

    for j in list_a:
        if j == v:
            id = list_a.index(j,n)
            n = id +1
            l1.append(list_a[id + 1])
            

            
    print("mode of ajay is",list(set(l1)))
          
    
    
    





if v > 1:
    f=count_ajay.index(v)
    h = ajay[f]
    print("mode of ajay is ",h)
      
rahulx = [10,0,100,20,50]
ajayy = [40,30,40,30,40]        
z = [1,2,3,4,5]
plt.xlabel("no of matches")
plt.ylabel("runs scored by rahul and ajay")
plt.title("selection of batsman")

plt.plot(z,rahulx,label = "rahul",marker = "o",markerfacecolor = "red")
plt.plot(z,ajayy,label = "ajay",marker ="o",markerfacecolor = "black")

plt.legend()
plt.show()              
            
            
          
            
    



        
    