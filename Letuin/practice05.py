"""
볼링 점수 계산하기

FSM으로 상태 관리
"""

STATUS_FRAME_FIRST_PITCH = 1
STATUS_FRAME_SECOND_PITCH = 2
STATUS_TEN_FRAME_STRIKE_FIRST_BONUS = 3
STATUS_TEN_FRAME_STRIKE_SECOND_BONUS = 4
STATUS_TEN_FRAME_STRIKE_SPARE = 5

bowling = list(map(int, input().split()))

idx, frame = 0, 0
score = 0
result = []
while idx < len(bowling):
    if frame == 11:
        result.append(score)
        score = 0
        frame = 0
        continue

    if bowling[idx] == 10:
        score += bowling[idx]
        if idx+2 < len(bowling) and bowling[idx+2]:
            score += bowling[idx+1] + bowling[idx+2]
        idx += 1
    elif idx+1 < len(bowling) and bowling[idx] + bowling[idx+1] == 10:
        score += bowling[idx] + bowling[idx+1]
        if idx+2 < len(bowling) and bowling[idx+2]:
            score += bowling[idx+2]
        idx += 2
    else:
        score += bowling[idx] + bowling[idx+1]
        idx += 2
    frame += 1

print(score)
print(result)
