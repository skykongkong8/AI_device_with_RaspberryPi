from random import randint
def rap():
    rap_num = randint(1,3)
    if rap_num == 1:
        rap = ['유튜버 과나님의 랩을 한 번 해보겠습니다. 흐응','부자 마음대로 추움','춘다아','아무리 출출하아','더라도 내 세끼를 참아아', '내 새끼를 굶길 수는 없으니까 차마아', '어때요 멋지죠?']
        #6
    elif rap_num == 2:
        rap = ['북치기','박치기','북치기','박치기','북치기박치기북치기박치기','북치기박치기북치기박치기']
    elif rap_num == 3:
        rap = ["Yo His palms are sweaty, knees weak, arms are heavy,\
        There's vomit on his sweater already, mom's spaghetti\
He's nervous, but on the surface he looks calm and ready\
To drop bombs, but he keeps on forgetting\
What he wrote down, the whole crowd goes so loud\
He opens his mouth, but the words won't come out\
He's choking, how, everybody's joking now\
The clocks run out, times up, over, blaow"]
    return [rap_num, rap]
