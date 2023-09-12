i = False
try:
    fileinput = open('KHIEUVU.inp',mode = 'r')
    fileouput = open('KHIEUVU.out',mode = 'w')
    x,y = map(int,(fileinput.readline().rstrip().replace('\n','').split()))
    arrnum = list(map(int,fileinput.readline().split()));arrind = []
    print(len(arrnum))
    i = True
except FileNotFoundError: print('Không tìm thấy file')
except FileExistsError: print('File Đầu Vào Không Hợp Lệ')
except: print('Lỗi file đầu vào')
if (i == True) and (len(arrnum) == x):
    for i in range(len(arrnum)):
        for j in range(len(arrnum)-1,1,-1):
            if (arrnum[i] - arrnum[j] == y) or (arrnum[j] - arrnum[i] == y):
                arrind.append(i+1),arrind.append(j+1)
    fileouput.write('{}'.format(len(arrind)//2))