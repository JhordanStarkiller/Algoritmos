NZ=int(input("NZ: "))
PE=int(input("PE: "))

if(PE > 5000):
    print("No se puede dar el servicio")
else:
    if(NZ == 1):
     CO = PE * 11
    elif(NZ == 2):
     CO = PE * 10
    elif(NZ == 3):
     CO = PE * 12
    elif(NZ == 4):
     CO = PE * 24
    else:
        CO = PE * 27
print(CO)