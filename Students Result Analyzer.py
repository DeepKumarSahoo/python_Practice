#STUDENTS RESULT ANALYZER!!!!!!(PROJECT)

Name =str(input("Enter student's name!!!!   "))
BEN=int(input("Enter bengali mark!!"))
ENG=int(input("Enter English mark!!"))
PHY=int(input("Enter Physics mark!!"))
CHM=int(input("Enter Chemistry mark!!"))
MATH=int(input("Enter Mathematics mark!!"))
BIO=int(input("Enter  Biology mark!!"))
Marks=[BEN,ENG,PHY,CHM,MATH,BIO]
Marks.sort(reverse=True)
best_Five=Marks[0]+Marks[1]+Marks[2]+Marks[3]+Marks[4]
Total=best_Five
per=Total/5
print("student's Name:",Name)
print("Bengali marks:",BEN)
print("English marks:",ENG)
print("Physics marks:",PHY)
print("Chemistry marks:",CHM)
print("Mathematics marks:",MATH)
print("Biology marks:",BIO)
print("Total marks obtain:",Total)
print("percentage:",per)
if(per>=90):
    print("Grade AA")
elif(per>=80):
    print("Grade A+")
elif(per>=70):
    print("Grade B")
elif(per>=60):
    print("Grade C")
elif(per>=50):
    print("Grade D")    
else:
    print("FAIL!")    
