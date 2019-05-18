# -*- coding: utf-8 -*-
"""Created on Sun May 19 00:10:08 2019 @author: kgh001"""
#Comment: import needful libraries for the programme
import re
#Comment1: Create a handle 'fname' providing path to open and load the text file
#Can be used to get the userdefined filename and path
fname = input("Enter the path of file:\n" )           ## e.g.>> C:\Users\kgh001\Desktop\File_Manipulation\Fsf.txt
#fname = 'C:\\Users\\kgh001\\Desktop\\SEAssignment2\\Fsf.txt'
#Comment2: Create an empty list to store all the lines from text file
lines = []
#Comment3: Read the text file using 'with' context providing filehandler and read command
with open (fname, 'r') as fname:
#Comment4: Setting iterations of 'For loop' to extract all the lines in object 'line'
    for line in fname:        
#comment5: store each line into the earlier created empty list
#          using 'append' method
        lines.append(line)
#Comment6: Remove/delete the lines that need to be skipped from list
#          (i.e. line 1,2,10,20,23) using 'del' method 
del lines[0:2]
del lines[7]
del lines[16]
del lines[18]
#Comment7: create an empty list to add the give values in the text flie
valList = []
#Comment8: Get the numerical parameters using regular expression 
regex1 = r'^[0-9]*\.?[0-9]+'
#Comment9: Setting a for loop to search in each line and save it into the list
for l in lines:
    val = re.findall(regex1,l)
    for v in val:
        valList.append(v)
#Comment10: Get the string parameters/ file names with extensions using regular expression 
#           and Setting another for loop to search in each line and save it into the list
regex2 = r'^[a-zA-Z]+\.*[a-zA-Z]+'
for l in lines:
    valstr = re.findall(regex2,l)
    if (valstr == []):
        continue
    valList.append(valstr[0])
#Comment11: Get the specific parameter with using regular expression 
#           and Setting another for loop to search in each line and save it into the list
regex3 = r'^[qQhH]'
for line in lines:
    keystr = re.findall(regex3,line)
    for l in keystr:
        valList.append(l)
#Comment12: Getting userdefined variable names to save each value 
#           stored in the list 'valList' by parsing them in  int or float
#           whereever necessary and append variables into a new list 'keylist'
keylist =[]
print("Enter variable name for 'Space Dicretization' value (i.e. dx):\t")
v = input()
keylist.append(v)
locals()[v] = int(valList[(0)])
print("Enter variable name for 'Time Step' value (i.e. dt):")
v = input()
keylist.append(v)
locals()[v] = int(valList[(1)])
print("Enter variable name for 'Maximum Iterations' value (i.e. nmaxits):")
v = input()
keylist.append(v)
locals()[v] = int(valList[(2)])
print("Enter variable name for 'Maximum Model Time Run' value (i.e. tmax):")
v = input()
keylist.append(v)
locals()[v] = int(valList[(3)])
print("Enter variable name for 'Time Coefficient, Preissmann' value (i.e. theta):")
v = input()
keylist.append(v)
locals()[v] = float(valList[(4)])
print("Enter variable name for 'Space Coefficient, Preissmann' value (i.e. psi):")
v = input()
keylist.append(v)
locals()[v] = float(valList[(5)])
print("Enter variable name for 'Boussinesq Coefficient' value (i.e. beta):")
v = input()
keylist.append(v)
locals()[v] = float(valList[(6)])
print("Enter variable name for 'Storage Width' value (i.e. bs):")
v = input()
keylist.append(v)
locals()[v] = int(valList[(7)])
print("Enter variable name for 'Chezy Coefficient' value (i.e. c):")
v = input()
keylist.append(v)
locals()[v] = int(valList[(8)])
print("Enter variable name for 'gravity' value (i.e. g):")
v = input()
keylist.append(v)
locals()[v] = float(valList[(9)])
print("Enter variable name for 'Bed Slope' value (i.e. ib):")
v = input()
keylist.append(v)
locals()[v] = int(valList[(10)])
print("Enter variable name for 'Length of Channel' value (i.e. l):")
v = input()
keylist.append(v)
locals()[v]  = int(valList[(11)])
print("Enter variable name for 'Upstream Value' (i.e. uv):")
v = input()
keylist.append(v)
locals()[v] = int(valList[(12)])
print("Enter variable name for 'Downstream Value' (i.e. dv):")
v = input()
keylist.append(v)
locals()[v] = int(valList[(13)])
print("Enter variable name for 'Depth input Data Files' (i.e. d_in):")
v = input()
keylist.append(v)
locals()[v] = valList[(14)]
print("Enter variable name for 'Discharge input Data File' (i.e. q_in):")
v = input()
keylist.append(v)
locals()[v] = valList[(15)]
print("Enter variable name for 'Water depth Output file' (i.e. d_out):")
v = input()
keylist.append(v)
locals()[v] = valList[(16)]
print("Enter variable name for 'Discharge Output file' (i.e. q_out):")
v = input()
keylist.append(v)
locals()[v] = valList[(17)]
print("Enter variable name for 'Upstream Condition' (i.e. uc):")
v = input()
keylist.append(v)
locals()[v] = valList[(18)]
print("Enter variable name for 'Downstream Condition' (i.e. dc):")
v = input()
keylist.append(v)
locals()[v] = valList[(19)]
print ("File processing Successful!!!\n")
#Comment13: print the userdefined variables with their values using for loop
print ("----------------------------------------------------------------------\n")
print ("Following is the list of variable with their values:")
for i in range(20):
    print("{}: {}".format(keylist[i],locals()[keylist[i]]))