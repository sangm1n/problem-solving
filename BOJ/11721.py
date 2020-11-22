# 한 줄에 10글자씩 끊어서 출력

string = input()
for i in range(1, len(string)+1):
    print(string[i-1], end='')
    if i%10==0:
        print('')