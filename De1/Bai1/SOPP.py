def readfile(namefile):
    fileinput = open(namefile,'r',encoding = 'utf-8')
    global x,y;x,y = map(int,fileinput.readline().rstrip().replace('\n','').split())
def filewrite(x,namefile):
    fileout = open(namefile,mode = 'w')
    fileout.write(f'{x}') 
def sumuoc(x):
    a = 0
    for i in range(1,x):
        if x % i == 0: a += i
    else:
        if a > x: return x
        else: return 0
def ktra(x,y):
    global a
    a = []
    for i in range(x,y+1):
        if sumuoc(i): a += [i]
    return len(a)           
i = False
try:
    readfile(input('Nhập name fileinput:'))
    i = True
except FileNotFoundError: print('không tìm thấy file !')
except FileExistsError: print('file bị lỗi')
except: print('Lỗi Đầu Vào')
if i:
    filewrite(ktra(x,y),input('Nhập name fileoutput:'))