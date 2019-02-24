import os, shutil

srr = 'temp/'
dst = 'train/'
c = 632
for i in os.listdir(srr):
    shutil.move(srr + i, dst + 'train_{}.jpg'.format(c))
    c += 1