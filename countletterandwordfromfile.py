isop=True
def countwandlfromfile():
    global noofw, noofl
    filename=input("Write name of file with it's extension to count words and letters: ")
    file=open(filename,'r')
    for i in file:
        noofw,noofl=0,0
        noofw=len(i.split())
        noofl=len(i)
    print(f'Number of words {noofw}, Number of letters {noofl}')
while isop:
    countwandlfromfile()
    wannaexit=input("Write y to exit")
    if wannaexit=="y":
        isop=False