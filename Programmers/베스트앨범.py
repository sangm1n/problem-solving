"""
author : Lee Sang Min
github : https://github.com/sangm1n
e-mail : dltkd96als@naver.com

title : 베스트앨범
description : Hash
"""

from collections import defaultdict


def solution(genres, plays):
    count_dic = defaultdict(int)
    list_dic = defaultdict(list)

    for i in range(len(genres)):
        count_dic[genres[i]] += plays[i]
        list_dic[genres[i]].append((plays[i], i))

    best_genre = sorted(count_dic.items(), key=lambda x: -x[1])

    result = []
    for genre, count in best_genre:
        now_genre = list_dic[genre]
        now_genre.sort(key=lambda x: (-x[0], x[1]))
        for i in range(2):
            if i < len(now_genre):
                result.append(now_genre[i][1])

    return result


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]

    result = solution(genres, plays)
    print(result)
