import turtle as t # turtle을 간략하게 t라고 정의함
import random


def screenLeftClick(x, y): # 함수 선언
    tSize = random.randrange(2, 10) # 2이상 10미만의 랜덤한 수를 뽑는 함수
    t.shapesize(tSize) # 사이즈를 2이상 10미만으로 랜덤
    r = random.random()
    g = random.random()
    b = random.random() # rgb = 색상, 색상을 랜덤으로
    t.color((r, g, b)) # 위에서 설정한대로 랜덤한 색상으로 나오게함
    tAngle = random.randrange(0, 360) # 0도에서 360미만의 각도로 랜덤 설정

    t.penup() # stamp() 전까지 거북이를 안찍게함
    t.goto(x, y) #마우스를 누른 위치로 이동시킴
    t.left(tAngle) # 랜덤으로 설정되는 각도만큼 왼쪽으로 회전
    t.stamp() # 거북이 모양 스탬프 찍기

t.shape('turtle') # 모양을 거북이 모양으로 설정

t.onscreenclick(screenLeftClick,1) # 마우스를 클릭하면 screenLeftClick이 실행됨, 1은 마우스 왼쪽클릭을 의미

t.done()