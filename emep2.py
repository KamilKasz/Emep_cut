"""
This script goes through downloaded EMEP data in .txt format and then chooses only those that contain data for chosen countries. Then it creates new folder with this data  
Author: Kamil Kaszowski
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*
from subprocess import Popen, PIPE
import os 
import shutil #importing modules


pathts= input("Path to directory with source files") or "/home/kamil/EMEP2019/"
pathts2=input("Path to directory with end files") or "/home/kamil/emep_cut/" #choosing directory with base data and name of the directory where results will be placed
zb=input("Name countries of interest (two or three letters shortcut for each country)") or ["PL","CZ","SK"] #choosing countries 


otw=Popen(["find",pathts,"-type","f","-size","+0","-name","*txt*"],stdout=PIPE)
otwa=otw.communicate()[0].decode().split("\n")
otwa2=otwa
otwa2.sort() #creating lists with paths and names of the files 

otwa2.remove("")
def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))] #defining function that will copy only paths of files
shutil.copytree(pathts,
                pathts2,
                ignore=ignore_files) #copying directory tree
                


                
for j in range(0,len(otwa2)):
    with open(otwa2[j]) as file: 
      read1=file.readlines() 
	
	
    for i in range(0,len(read1)):
        if read1[i][0:2] in zb:
          with open(pathts2+otwa2[j][len(pathts):]+"_cut.txt","a") as file2:
             file2.write(read1[i]) #creating files

	 



