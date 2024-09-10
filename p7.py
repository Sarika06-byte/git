
def sign_in(nm,pswd,email):
     print("_________________________________________")
     print("_________________________________________")
     print("\nNOW U HAVE ENTERED IN THE SIG IN PAGE")
     print("\nENTER THE FOLLOWING DETAILS : ")
     nm=input("ENTER  NAME                 : ")
     email=input("ENTER  EMAIL_ID             : ")
     pswd=input("ENTER  PASSWORD             : ")
     pswd1=input("ENTER  CONFIRM PASSWORD    : ")
     if(pswd1==pswd):
            print("\n\nSUCCESSFULLY SIGNED IN")
            print("_________________________________________")
     else:
            pswd1=input("\nPASSWORD DON'T MATCH ....  TRY AGAIN   :  ")
            print("_________________________________________")
            if(pswd1==pswd):
               print("\n\nSUCCESSFULLY LOG IN")

            else:
                print("\nWRONG PASSWORD")
                print("\nNOT  SIGNED IN")
                ans1=input("DO U WANT TO SIGN IN AGAIN (y/n)" )
                if(ans1=="y"):
                  sign_in(nm,pswd,email)
                else:
                 print("\n\n_________________________________________")
                print("THANKS FOR VISITING")
                print("_________________________________________")

def login(nm,pswd,email):
    print("\n\n\t\t_________________________________________")
    print("\t\t\tWELCOME TO THE WEBSITE ")
    print("\t\t_________________________________________")
    print("\n\n______________________________________________")
    ans=input("DO U HAVE ANY PASSWORD(y/n) : ")
    print("______________________________________________")
    if(ans=="y"):
        psd=input("\nENTER THE PASSWORD : ")
        print("______________________________________________")
    else :
        print("\nGO AHEAD>>>>")  
        print("______________________________________________")
    a=input("\nENTER(y) TO DIRECTLY  >> GO TO LOGIN PAGE  >> ELSE ENTER(n): ")
    print("_________________________________________")
    if(a=="n"):
      ans=input("DO U HAVE A ACCOUNT(y/n) : ")
      print("_________________________________________")
      if(ans=="n"):
          ans=input("\nDO U WANT TO CREATE AN ACCOUNT OR NOT(y/n): ")
          print("_________________________________________")
          if(ans=="y"):
             sign_in(nm,pswd,email)
          else:
            ans=input("\nDO U WANT TO LOGIN OR NOT(y/n): ")
            print("_________________________________________")
            if(ans=="y"):
             login(nm,pswd,email)
             
            else:
                print("\n\n_________________________________________")
                print("THANKS FOR VISITING")
                print("_________________________________________")
    
      else:
         ans=input("\nDO U WANT TO LOGIN OR NOT(y/n): ")
         print("_________________________________________")
         if(ans=="y"):
             login(nm,pswd,email)
        
         else:
            print("\n\n_________________________________________")
            print("THANKS FOR VISITING")
            print("_________________________________________")

    else:
         print("_________________________________________")
         print("\nNOW U HAVE ENTERED IN THE LOGIN PAGE")
         print("_________________________________________")
         print("\nENTER THE FOLLOWING DETAILS : ")
         print("_________________________________________")
         nm=input("ENTER  NAME             : ")
         email=input("ENTER  EMAIL_ID         : ")
         pswd=input("ENTER  PASSWORD         : ")
         if(pswd==psd):
            print("\n\nSUCCESSFULLY LOG IN")
            print("_________________________________________")
         else:
            pswd=input("\nWRONG PASSWORD ....  TRY AGAIN   :  ")
            print("_________________________________________")
            if(pswd==psd):
               print("\n\nSUCCESSFULLY LOG IN")

            else:
                print("\nWRONG PASSWORD")
                print("\n\n_________________________________________")
         print("\nTHANKS FOR VISITING\n")
         print("_________________________________________")
         print("_________________________________________")

nm,pswd,email=0,0,0
login(nm,pswd,email)