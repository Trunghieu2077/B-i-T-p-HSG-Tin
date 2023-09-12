def sumuoc(x):
    a = 0
    for i in range(1,x):
        if x % i == 0: a += i
    else:
        if a > x: return x
        else: return 0
def ktra(x,y):
    a = []
    for i in range(x,y+1): if sumuoc(i): a += [i]
    return len(a)
spacedone = False
try: 
    spacedone = True
    fileinput = open('SOPP.inp',mode = 'r',encoding = 'utf-8')
    x,y = map(int,fileinput.readline().rstrip().replace('\n','').split())
except FileNotFoundError: print('Không tìm thấy file')
except FileExistsError: print('File Đầu Vào Bị Lỗi !!')
except: print('Lỗi Đầu Vào')
if spacedone:
    fileout = open('SOPP.out',mode = 'w')
    fileout.write('{}'.format(ktra(x,y)))
