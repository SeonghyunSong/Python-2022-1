import turtle as t

t.shape('turtle')

h = int(input())
w = int(input())

for i in range(4):
    if i % 2 == 0:
        t.forward(h)
        t.left(90)
    else:
        t.forward(w)
        t.left(90)

t.done()
