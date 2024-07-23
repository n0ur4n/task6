englishlist=["one" , "two"  ]

for i in range(len(englishlist)):
    if len(englishlist)==1:
        print(englishlist[i] , end=" ")
    elif i==(len(englishlist)-1):
        print("and",englishlist[i] , end=" ")
    else:
        print(englishlist[i] , "," , end=" ") 
#print(englishlist)