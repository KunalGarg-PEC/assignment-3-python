grade = int(input("enter gardes of student: "))

Report="Your grade is <!grade!> and <!performance!> performance"

if grade==4:
    Report=Report.replace("<!grade!>","D")
    Report=Report.replace("<!performance!>","Poor")
    print(Report)

elif grade==5:
    Report=Report.replace("<!grade!>","C")
    Report=Report.replace("<!performance!>","Below average")
    print(Report)  

elif grade==6:
    Report=Report.replace("<!grade!>","C+")
    Report=Report.replace("<!performance!>","average")
    print(Report) 

elif grade==7:
    Report=Report.replace("<!grade!>","B")
    Report=Report.replace("<!performance!>","good")
    print(Report)    

elif grade==8:
    Report=Report.replace("<!grade!>","B+")
    Report=Report.replace("<!performance!>","Very good")
    print(Report)     

elif grade==9:
    Report=Report.replace("<!grade!>","A")
    Report=Report.replace("<!performance!>","Excellent")
    print(Report)  

elif grade==10:
    Report=Report.replace("<!grade!>","A+")
    Report=Report.replace("<!performance!>","Outstanding")
    print(Report)        

else :
    print("error")    