# write a program to generate multiplication for 14
numb = int(input("Enter number whose table your want: "))
fh = open("9_multablereal.txt","w")
for i in range(1,11):
    fh.write(str(numb))
    fh.write(" X ")
    fh.write(str(i))
    fh.write(" = ")
    fh.write(str(numb*i))
    fh.write("\n")
    # print(numb,"X",i,"=",numb*i)
fh.close()