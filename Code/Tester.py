
import subprocess

#Runs a command in the shell to start NamesSorter
subprocess.run(["python3", "NamesSorter.py"])

f1 = open("Output.txt" , "r")
f2 = open("Sorted Text.txt", "r")

i = 0
for line1 in f1:
    i += 1
      
    for line2 in f2:
        if not (line1 == line2):
            print("Line ", i, ":")
            print("\tReported:", line1, end='')
            print("\tCorrect:", line2, end='')
        break
  
#Close files
f1.close()                                       
f2.close()


#Reversed Tests
subprocess.run(["python3", "NamesSorter.py", "-r"])

f1 = open("Output.txt" , "r")
f2 = open("Sorted Text - Reversed.txt", "r")

i = 0
for line1 in f1:
    i += 1
      
    for line2 in f2:
        if not (line1 == line2):
            print("Reversed, Line ", i, ":")
            print("\tReported:", line1, end='')
            print("\tCorrect:", line2, end='')
        break
  
#Close files
f1.close()                                       
f2.close()

print("Tests Complete.")
