word = input()
croalp = ['c=','c-','d-','lj','nj','s=','dz=','z='] # 'dz='이 'z='보다 먼저 나와야함
cnt = 0
for i in range(len(croalp)):
    word = word.replace(croalp[i],'T') #word에 croalp가 있으면 그 알파벳은 T로 치환 그리고 길이 반환
print(len(word))
# 이거 푸는데 일주일 걸렸네 씌벌. 그래도 원래는 for문 if문 많이 썻는데 좀 뿌듯하구만. 항상 풀고난후에는 별로 어렵게 안느껴짐