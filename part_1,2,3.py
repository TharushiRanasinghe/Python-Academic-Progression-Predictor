#Author- Tharushi Ranasinghe
# Date: 11th November 2022

#Part 1-Main Version
#Part 2–List(extension)
#Part 3-Text File(extension)

datas=[]
Pr_count=0
tr_count=0
re_count=0
Ex_count=0
def range_Integer_Error(credit_name):
    while True:
        try:
            global credit
            global x
            credit_str=input(f"Enter your total {credit_name} credits: ")
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
            datas.append(['Progress',pass_1,defer_1,fail_1])
            Pr_count=Pr_count+1
    elif(pass_1==100):
            print("Progress(module trailer)")
            datas.append(['Progress(module trailer)',pass_1,defer_1,fail_1])
            tr_count=tr_count+1
    elif(fail_1<=60):
            print("Module retriever")
            datas.append(['Module retriever',pass_1,defer_1,fail_1])
            re_count=re_count+1
    elif(fail_1>=80):
            print("Exclude")
            datas.append(['Exclude',pass_1,defer_1,fail_1])
            Ex_count=Ex_count+1
    print()
    qy=input("""Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results : """)
    print()
    if qy.lower()=='q':
        break
    elif qy.lower()=='y':
        continue

print('Histogram')
total_count=Pr_count+tr_count+re_count+Ex_count            
print("Progress",Pr_count," :",end="")
for i in range(Pr_count):
    print('*',end="")

print("\n"+"trailer",tr_count,"  :",end="")
for i in range(tr_count):
    print('*',end="")
print("\n"+"retriever",re_count,":",end="")
for i in range(re_count):
    print('*',end="")
print("\n"+"Exclude",Ex_count,"  :",end="")
for i in range(Ex_count):
    print('*',end="")
print()
    
print(f"\n{total_count} outcomes in total.\n")

#part 2

for data in datas:
    print(data[0]+ ' - ' + str(data[1])+',' , str(data[2]),',' , str(data[3]))

#
print()  # Add an empty line 
#

#part 3

print('Part 3: ')

with open("textfile.txt", "w") as f:
    for data in datas:
        f.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")

with open("textfile.txt", "r") as f:
    print(f.read())


