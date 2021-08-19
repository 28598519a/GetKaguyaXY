import csv
import os
import pathlib

# 取得目標資料夾
while True:
	Root = input('Write your target folder path : ').replace("'","").replace('"',"")
	if os.path.exists(Root):
		break
	else:
		print("Path not exist")

# 資料夾路徑結尾若為 "\" 則去掉
if not os.path.basename(Root):
	Root = Root[:-1]

# 取得所有 "*.alp" 附檔名的檔案
Alp = pathlib.Path(Root).glob("**\*.alp")

# 取得XY座標
xylist = ""
for i in Alp:
	position = []
	
	with open(i, "rb") as f:
		f.seek(4)
		position.append(int.from_bytes(f.read(2), byteorder="little"))
		f.seek(8)
		position.append(int.from_bytes(f.read(2), byteorder="little"))
	
	xylist = xylist + str(i).replace(f"{Root}\\","").replace("\\","/") + f" : {str(position[0])}, {str(position[1])}\n"

# 存座標表為txt
with open("AlpXY_Offset.txt", "w") as txt:
	txt.write(xylist)

