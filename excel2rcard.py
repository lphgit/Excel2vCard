import xlrd


import sys, getopt



opts, args = getopt.getopt(sys.argv[1:], "hi:o:")

input_file=""

output_file=""
initflag = 0;

for op, value in opts:

    if op == "-i":
        initflag = 1;

        input_file = value

    elif op == "-o":
        initflag = 1;

        output_file = value

    elif op == "-h":

        print("-i inputfile  -o outputfile")

        sys.exit()
        
if initflag == 0 :
    print("-i inputfile  -o outputfile")
    sys.exit()


        
data = xlrd.open_workbook(input_file);

table = data.sheets()[0];

nrows = table.nrows

ncols = table.ncols

print("nrows", nrows);
startdatarow = (int)(input("通信录数据起始行（始于0）: "))
enddatarow = (int)(input("通信录数据结束行（始于0）: "))
namecol = (int)(input("名字所在列（始于0）: "))
cellcol = (int)(input("电话所在列（始于0）:"))

f = open(output_file, 'w')

for i in range(startdatarow , enddatarow):
  ctype = table.cell(i, cellcol).ctype
  cell  = table.cell(i, cellcol).value
  if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
       cell = int(cell)  # 浮点转成整型
       cell = str(cell)  # 转成整型后再转成字符串，如果想要整型就去掉该行
  f.write("BEGIN:VCARD\n");
  f.write("VERSION:3.0\n");
  f.write("FN:CHARSET=gb2132:" + table.cell(i,namecol).value + "\n");
  f.write("TEL;TYPE=CELL:" + cell + "\n");
  f.write("ORG;CHARSET=gb2132:南京能云电力\n");
  f.write("END:VCARD\n");
f.close();

