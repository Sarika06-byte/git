print("____________________________________________________")
print("____________________________________________________")
s=s="hello"
i=1
s1=lambda s: s[0:4]
s2=s1(s)
print(f"\n{i}\tSLICING[2:4] : [  hello  ] --> [{s2}]")
print("____________________________________________________")
s="  c++   "
s1=lambda s: s.strip()
s2=s1(s)
print(f"\n{i+1}.\tSTRIP : [  c++  ] --> [{s2}]")
print("____________________________________________________")
s1=lambda s: s.lstrip()
s2=s1(s)
print(f"\n{i+2}.\tLSTRIP : [  c++  ] --> [{s2}]")
print("____________________________________________________")
s1=lambda s: s.rstrip()
s2=s1(s)
print(f"\n{i+3}.\tRSTRIP : [  c++  ] --> [{s2}]")
print("____________________________________________________")
s="hello"
s1=lambda s: s.removeprefix("h")
s2=s1(s)
print(f"\n{i+4}.\tREMOVEPREFIX : [ hello ] --> [ {s2} ]")
print("____________________________________________________")
s1=lambda s: s.removesuffix("o")
s2=s1(s)
print(f"\n{i+5}.\tREMOVESUFFIX : [ hello ] --> [ {s2} ]")
print("____________________________________________________")
s1=lambda s: s.replace("hello","bye")
s2=s1(s)
print(f"\n{i+6}.\tREPLACE : [ hello ] --> [ {s2} ]")
print("____________________________________________________")
import re
s="hi world"
s1=lambda s: re.sub("\s","--",s)
s2=s1(s)
print(f"\n{i+7}.\tRE.SUB(\s to '-') : [ hi world ] --> [ {s2} ]")
print("____________________________________________________")
s="hi world"
s1=lambda s: s.split()
s2=s1(s)
print(f"\n{i+8}.\tSPLIT : [ hi world ] -->  {s2} ")
print("____________________________________________________")
s="hi good morning"
s1=lambda s: s.rsplit(maxsplit=1)
s2=s1(s)
print(f"\n{i+9}.\tRSPLIT : [ hi good morning ] -->  {s2} ")
print("____________________________________________________")
s=["p","y","t","h","o","n"]
s1=lambda s: "".join(s)
s2=s1(s)
print(f"\n{i+10}.\tJOIN : [ p,y,t,h,o,n ] --> [ {s2} ]")
print("____________________________________________________")
s="java"
s1=lambda s: s.upper()
s2=s1(s)
print(f"\n{i+11}.\tUPPER : [ java ] --> [ {s2} ]")
print("____________________________________________________")
s="jAVA"
s1=lambda s: s.capitalize()
s2=s1(s)
print(f"\n{i+12}.\tCAPTIALISE : [ jAVA ] -->  [ {s2} ]")
print("____________________________________________________")
s="JAVA"
s1=lambda s: s.lower()
s2=s1(s)
print(f"\n{i+13}.\tLOWER : [ JAVA ] --> [ {s2} ]")
print("____________________________________________________")
s="JAVA"
s1=lambda s: s.islower()
s2=s1(s)
print(f"\n{i+14}.\tISLOWER : [ JAVA ] --> [ {s2} ]")
print("____________________________________________________")
s1=lambda s: s.isupper()
s2=s1(s)
print(f"\n{i+15}.\tISUPPER : [ JAVA ] --> [ {s2} ]")
print("____________________________________________________")
s="java"
s1=lambda s: s.isalpha()
s2=s1(s)
print(f"\n{i+16}.\tISAPLHA : [ java ] --> [ {s2} ]")
print("____________________________________________________")
s="java"
s1=lambda s: s.isnumeric()
s2=s1(s)
print(f"\n{i+17}.\tISNUM : [ java ] --> [ {s2} ]")
print("____________________________________________________")
s="java123"
s1=lambda s: s.isalnum()
s2=s1(s)
print(f"\n{i+18}.\tISAPNUM : [ java123 ] --> [ {s2} ]")
print("____________________________________________________")
s=['h','t','t','p']
s1=lambda s: s.count('t')
s2=s1(s)
print(f"\n{i+19}.\tCOUNT('t') : [ h,t,t,p ] --> [ {s2} ]")
print("____________________________________________________")
s="java123"
s1=lambda s: s.find('a')
s2=s1(s)
print(f"\n{i+20}.\tFIND('a') : [ java123 ] --> [ {s2} ]")
print("____________________________________________________")
s="core_java"
s1=lambda s: s.startswith('j')
s2=s1(s)
print(f"\n{i+21}.\tSTARTSWITH('j') : [ core_java ] --> [ {s2} ]")
print("____________________________________________________")
s1=lambda s: s.endswith('a')
s2=s1(s)
print(f"\n{i+22}.\tENDSWITH('a') : [ core_java ] --> [ {s2} ]")
print("____________________________________________________")
s="8 bit is  byte"
s1=lambda s: s.partition("is")
s2=s1(s)
print(f"\n{i+23}.\tPARTITION('is') : [ 8 bit is byte ] --> [ {s2} ]")
print("______________________________________________________")
s="html"
s1=lambda s: s.center(10,"-")
s2=s1(s)
print(f"\n{i+24}.\tCENTER : [ html ] --> [ {s2} ]")
print("____________________________________________________")
s1=lambda s: s.ljust(10,"-")
s2=s1(s)
print(f"\n{i+26}.\tLJUST : [ html ] --> [ {s2} ]")
print("____________________________________________________")
s1=lambda s: s.rjust(10,"-")
s2=s1(s)
print(f"\n{i+27}.\tRJUST : [ html ] --> [ {s2} ]")
print("____________________________________________________")
s=" HI world"
s1=lambda s: s.swapcase()
s2=s1(s)
print(f"\n{i+29}.\tSWAPCASE : [ hi world ] --> [ {s2} ]")
print("____________________________________________________")
s='A'
s1=lambda s: s.zfill(6)
s2=s1(s)
print(f"\n{i+30}.\tZFILL : [ A ] --> [ {s2} ]")
print("____________________________________________________")
s='A'
s1=lambda s: s.encode()
s2=s1(s)
print(f"\n{i+31}.\tENCODE : [ A ] --> [ {s2} ]")
print("____________________________________________________")
s1=lambda s=21 : print(f"\n{i+32}.\tF_STRING : value of s = {s}")
s1()
print("____________________________________________________")
s=b's'
s1=lambda s: s.decode()
s2=s1(s)
print(f"\n{i+33}.\tDECODE : [ b's' ] --> [ {s2} ]")
print("____________________________________________________")
s="dict"
b={1:111,2:222}
s1=lambda s: s.maketrans(b)
s2=s1(s)
print(f"\n{i+34}.\tMAKETRANS : [ dict ] --> [ {s2} ]")
print("____________________________________________________")


