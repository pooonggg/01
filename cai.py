A=input("ใส่เลข")
A=int(A)
B=input("ใส่หน่วย เมื่อ1=MM , 2=CM , 3=M , 4=KM")
B=int(B)
if B==1:
    D=A*0.1
    F=(A, "MM")
elif B==2:
    D=A
    F=(A, "CM")
elif B==3:
    D=A*100
    F=(A, "M")
elif B==4:
    D=A*1000
    F=(A, "KM")
D=int(D)
C=input("แปลงหน่วยเป็น เมื่อ1=MM , 2=CM , 3=M , 4=KM")
C=int(C)
if C==1:
    E=D*10
    G=(F ,"เท่ากับ", E ,"MM")
elif C==2:
    E=D
    G=(F ,"เท่ากับ", E ,"CM")
elif C==3:
    E=D*0.01
    G=(F ,"เท่ากับ", E ,"M")
elif C==4:
    E=D*0.001
    G=(F ,"เท่ากับ", E ,"KM")
print(G)
