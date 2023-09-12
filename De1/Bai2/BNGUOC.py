is_spacedone = False
try: 
    fileinput = open('BNGUOC.inp',mode = 'r')
    fileouput = open('BNGUOC.out',mode = 'w')
    x,y = map(str,(fileinput.readline().rstrip().split()))
    DNa,DNb = int(str(x[::-1])),int(str(y[::-1]))
    is_spacedone = True
except: print('File Đầu Vào Bị Lỗi')
if is_spacedone:
    if DNa > DNb: fileouput.write(f'{x}')
    else: fileouput.write(f'{y}')
