from pathlib import Path
filename = "file1.txt"
mode = 'r'
#Case 1
print("")
f = open (filename, mode)
#f.read will read and return the whold contents of the files.
data = f.read()
print(data)
data1 = f.read()
print("========")
print(data1)
f.close()

#another case
outfilename = "outfile.txt"
with open(outfilename, 'w') as fout:
    fout.write("this is a newly created file. The following \
lines will be copied from the input file. \n")
    with open (filename, mode) as fin:
        for line in fin:
            fout.write(line)

#more stuff
outfilename = "outfile.txt"
my_file = Path(outfilename)
if my_file.exists() and my_file.is_file():
    print ("Warning!!!! {} already exists. Opening it will overwrite it".format(outfilename))
with open ("outfile.txt", 'w') as fout:
    fout.write("{} already exists. \
It was opened with mode of 'w' and thus overwritten.\
\n The following lines were copied from the input file. \n \n".format(outfilename))

    with open (filename, mode) as fin:
        for line in fin:
            fout.write(line)

print ("Case 7: opening a text file with mode 'a' will append at the end of it")
outfilename = "outfile.txt"
my_file = Path(outfilename)
if my_file.exists() and my_file.is_file():
    print ("Warning!!!! {} already exists. Opening with mode 'a' will append it at the end".format(outfilename))
with open ("outfile.txt", 'a') as fout:
    fout.write("\n \n{} already exists. \
It was opened with mode of 'a'.\
\n The following lines were copied from the input file. \n \n".format(outfilename))

    with open (filename, mode) as fin:
        for line in fin:
            fout.write(line)