#Author- Tharushi Ranasinghe
# Date: 11th November 2022

#Part 4-Dictionary(separate program)


datas={}
Pr_count=0
tr_count=0
re_count=0
Ex_count=0
def range_Integer_Error(credit_name):
    while True:
        try:
            global credit
            global x
            credit_str=input(f"Enter your total {credit_name} credits:")
            credit=int(credit_str)
            if(credit%20 or credit>120):
                print('Out of Range')
            else:
                x=None
                break
        except:
           
            
            if credit_str.lower()=="q":
                x="q"
                break
            else:
                print("interger requird")
                x=None
                continue

while True:
    index=input('Enter the studnet index number : ')
    range_Integer_Error("PASS")
    if x:
        break
    pass_1=credit
    range_Integer_Error("DEFER")
    if x:
        break
    defer_1=credit
    range_Integer_Error("FAIL")
    if x:
        break
    fail_1=credit

    if(pass_1+defer_1+fail_1!=120):
        print("total incorrect")


    elif(pass_1==120):
        print("Progress")
        datas[index]={'progression Outcome':
'Progress','passCredit':pass_1,'deferCredit':defer_1,'failCredit':fail_1}                          
        Pr_count=Pr_count+1
    elif(pass_1==100):
        print("Progress-module trailer")
        datas[index]={'progression Outcome':
'Progress(module trailer)','passCredit':pass_1,'deferCredit':defer_1,'failCredit':fail_1}
        tr_count=tr_count+1
    elif(fail_1<=60):
        print("DO not Progress-module retriever")
        datas[index]={'progression Outcome':
'Module retriever','passCredit':pass_1,'deferCredit':defer_1,'failCredit':fail_1}
        re_count=re_count+1
    elif(fail_1>=80):
        print("Excluded")
        datas[index]={'progression Outcome':     
'Excluded','passCredit':pass_1,'deferCredit':defer_1,'failCredit':fail_1}
        Ex_count=Ex_count+1
        print()
    qy=input("""Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results : """)
    print()
    if qy.lower()=='q':
        break
    elif qy.lower()=='y':
        continue

Tot_count=Pr_count+tr_count+re_count+Ex_count
s='-'
print(s*100)
print ('Histogram')
print("Progress ",Pr_count," :",end="")
for i in range(Pr_count):
    print('*',end="")

print("\n"+"Trailer  ",tr_count," :",end="")
for i in range(tr_count):
    print('*',end="")
print("\n"+"Retriever",re_count," :",end="")
for i in range(re_count):
    print('*',end="")
print("\n"+"Excluded ",Ex_count," :",end="")
for i in range(Ex_count):
    print('*',end="")
print()
                    
    
print("\n "+str(Tot_count) +" outcomes in total.\n")
print(s*100)
    
                  
for data in datas:
    print(str(data) + ':'+datas[data]['progression Outcome']+' - '+ str(datas[data]['passCredit'])+',' +str(datas[data]['deferCredit'])+','+str( datas[data]['failCredit']))

        
