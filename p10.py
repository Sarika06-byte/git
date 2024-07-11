import array as a
i1=1 
i2=1
print(f"{i1}.....ARRAY OF UNSIGNED BOOLEAN( CHAR ) ELEMENETS..... ")
ary=a.array("B",[True,False])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
i2=1
print("_________________________________________________")
print(f"{i1+1}.....ARRAY OF SIGNED BOOLEAN( CHAR ) ELEMENETS..... ")
ary=a.array("b",[True,-False,9])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
print("_________________________________________________")
i2=1
print(f"{i1+2}.....ARRAY OF UNSIGNED INT( SHORT ) ELEMENETS..... ")
ary=a.array("H",[3463,5464])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
i2=1
print("_________________________________________________")
print(f"{i1+3}.....ARRAY OF SIGNED INT( SHORT ) ELEMENETS..... ")
ary=a.array("h",[1,343])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
print("_________________________________________________")
i2=1
print(f"{i1}.....ARRAY OF UNSIGNED INT( LONG ) ELEMENETS..... ")
ary=a.array("L",[3564645,464576])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
i2=1
print("_________________________________________________")
print(f"{i1+1}.....ARRAY OF SIGNED INT( LONG ) ELEMENETS..... ")
ary=a.array("l",[45645,45778])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
print("_________________________________________________")
i2=1
print(f"{i1+2}.....ARRAY OF UNSIGNED INT ELEMENETS..... ")
ary=a.array("I",[3463,5464])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
i2=1
print("_________________________________________________")
print(f"{i1+3}.....ARRAY OF SIGNED INT ELEMENETS..... ")
ary=a.array("i",[1,343])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
print("_________________________________________________")
i2=1
print(f"{i1}.....ARRAY OF UNSIGNED INT( LONG LONG ) ELEMENETS..... ")
ary=a.array("Q",[3564645,464576])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
i2=1
print("_________________________________________________")
print(f"{i1+1}.....ARRAY OF SIGNED INT( LONG LONG ) ELEMENETS..... ")
ary=a.array("q",[45645,45778])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
print("_________________________________________________")
i2=1
print(f"{i1+2}.....ARRAY OF FLOAT ELEMENETS..... ")
ary=a.array("f",[3463.35,5464])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
i2=1
print("_________________________________________________")
print(f"{i1+3}.....ARRAY OF DOUBLE ELEMENETS..... ")
ary=a.array("d",[343464564.464,45646.577])
for i in range(0,len(ary)):
    print(f"\t\t>>>{ i2 } element of array : {ary[i]}")
    i2=i2+1
print("_________________________________________________")