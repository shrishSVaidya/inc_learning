import os
from collections import Counter

def get_classes(path):
    path = os.path.join(os.getcwd(), 'data', path, 'labels')
    classes = []
    nums={}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt') and file != 'classes.txt':
                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        classes.append(line.split()[0])
    nums=dict(Counter(classes))                
    classes = list(set(classes))
    return classes, nums

print('classes in train:', get_classes('train')[0])
print('classes in val:', get_classes('val')[0])
# print('classes in test:', get_classes('test')[0])

print('number of classes in train:', get_classes('train')[1])
print('number of classes in valid:', get_classes('val')[1])



# for file in os.listdir('data/val'):
#     if file.endswith('.txt'):
#         os.replace('data/val/'+file, 'data/val/labels/'+file)
# for file in os.listdir('data/val/labels'):
#     try:
#         classes=[]
#         if file.endswith('.txt'):
#             with open(os.path.join('data/val/labels', file), 'r') as f:
#                         for line in f:
#                             classes.append(line.split()[0])
#             if '13' in classes:
#                 os.replace('data/val/images/'+ file.split('.')[0]+'.png', 'data/extra/images/'+file.split('.')[0]+'.png')
#                 os.replace('data/val/labels/'+file, 'data/extra/labels/'+file)
#     except Exception as e:
#          print(e)

# im = list(os.listdir('data/train/images'))
# lab = list(os.listdir('data/train/labels'))

# for i in lab:
#     with open(os.path.join('data/train/labels', i), 'r') as f:
#                     for line in f:
#                         if line.split()[0]=='13':
#                              print(i)

# lab_m = [i.split('.')[0] for i in lab]
# im_m = [i.split('.')[0] for i in im]
# print(len(im), len(lab))
# for i in lab_m:
#     if i not in im_m:
#         print(i)
#         os.remove('data/val/labels/'+i+'.txt')