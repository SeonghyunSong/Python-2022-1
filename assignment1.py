import turtle as t # turtle을 간략하게 t라고 정의함

t.width(20) # 선의 폭이 20
t.shape("turtle") # 모양을 거북이 모양으로
t.color("cyan") # 색 지정
t.circle(100) # 반지름이 100만큼인 원 생성
t.up() # down 전까지 거북이가 선을 그리지 않게함

t.color("black")
t.forward(180) # 앞으로 180만큼 이동 (오륜기를 그리기 위한 위치)
t.down() # 이제 선을 그림
t.circle(100)
t.up()
t.color("red")
t.forward(180)
t.down()
t.circle(100)
t.up()
t.color("green")
t.left(120)
t.forward(50)
t.left(60)
t.forward(50)   # 오륜기를 그리기 위해 4개의 과정만큼 up한채로 이동
t.down()
t.circle(100)
t.up()
t.color("yellow")
t.forward(200)
t.down()
t.circle(100)