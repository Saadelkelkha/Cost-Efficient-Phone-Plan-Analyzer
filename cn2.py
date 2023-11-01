d=[]
def tel (t) :
    pt=[]
    if t>2 :
      p=100+(t-2)*0.5*60
    else :
      p=100
    pt.append(p)
    if t>1 :
      p=50+(t-1)*60
    else :
      p=50
    pt.append(p)
    if t>0.5 :
      p=20+(t-0.5)*1.5*60
    else :
      p=20
    pt.append(p)
    p=t*2*60
    pt.append(p)
    return pt
n=int(input("Type communication time in minute :"))
t=n/60
d=tel(t)
print("The monthly cost list per offer is ",d,"DH")
for i in range (0,len(d)) :
   min=d[0]
   o=2
   if min > d[i] :
     min=d[i]
     o=i+2
if min>200 :
   print ("The most interesting offer is offer 1.")
else :
   print("The most interesting offer is offer ",o,".")