import random
import os

path = "E:/github_ide/Yolo-for-k210/Yolo-for-k210/Train_Image/MyImage"

jpegdir = os.path.join(f'{path}/Annotations')
rootdir = os.path.join(f'{path}/JPEGImages')
with open(f'{path}/ImageSets/Main/pscalvoc.txt', 'w') as write_path:
    for (dirpath,dirnames,filenames) in os.walk(rootdir):
        for filename in filenames:    
            it = 0  #在JPEGImages寻找对应的图片，找到图片后标记为1
            for (dirpath1,dirnames1,filenames1) in os.walk(jpegdir):
                for filename1 in filenames1:
                    if (
                        os.path.splitext(filename1)[1] == '.xml'
                        and os.path.splitext(filename)[1] == '.jpg'
                        and os.path.splitext(filename)[0]
                        == os.path.splitext(filename1)[0]
                    ):
                        write_path.write(os.path.splitext(filename)[0]+'\n')
                        it = 1
                        break
            if it==0:
                print("删除以下多于文件")
                print(f'{path}/JPEGImages{os.path.splitext(filename)[0]}.jpg')
                os.remove(f'{path}/JPEGImages/{os.path.splitext(filename)[0]}.jpg')

    for (dirpath,dirnames,filenames) in os.walk(jpegdir):
        for filename in filenames:    
            it = 0  #在JPEGImages寻找对应的图片，找到图片后标记为1
            for (dirpath1,dirnames1,filenames1) in os.walk(rootdir):
                for filename1 in filenames1:
                    if (
                        os.path.splitext(filename1)[1] == '.jpg'
                        and os.path.splitext(filename)[1] == '.xml'
                        and os.path.splitext(filename)[0]
                        == os.path.splitext(filename1)[0]
                    ):
                        # write_path.write(os.path.splitext(filename)[0]+'\n')
                        it = 1
                        break
            if it==0:
                print("删除以下多于文件")
                print(f'{path}/Annotations{os.path.splitext(filename)[0]}.xml')
                os.remove(f'{path}/Annotations/{os.path.splitext(filename)[0]}.xml')

annotation_path = f"{path}/ImageSets/Main/pscalvoc.txt"
train_path = f"{path}/ImageSets/Main/train.txt"
val_path = f"{path}/ImageSets/Main/val.txt"
test_path = f"{path}/ImageSets/Main/test.txt"

train_file = open(train_path,"w")
val_file = open(val_path,"w")
test_file = open(test_path,"w")
anno = open(annotation_path, 'r')
result = []
my_dict = {}
cnt = 0
for line in anno:
   my_dict[cnt]=line
   cnt+=1
totalnum = cnt
train_num = int(totalnum * 0.7)
val_num = int(totalnum * 0.2)
test_num = totalnum-train_num-val_num

test_set = set()
val_set = set()
train_set = set()

while(len(test_set) < test_num):
     x = random.randint(0,totalnum)
     if x not in test_set :
        test_set.add(x)

while(len(val_set) < val_num):
     x = random.randint(0,totalnum)
     if x in test_set :
        continue
     if x not in val_set :
        val_set.add(x)

for x in range(totalnum):
     if x in test_set or x in val_set:
        continue
     else:
        train_set.add(x)

for i in range(cnt):
    strs = my_dict[i]
    if i in train_set:
       train_file.write(strs)
    elif i in val_set:
       val_file.write(strs)
    else:
       test_file.write(strs)
train_file.close
val_file.close
test_file.close