import turtle
import random

turtle.bgcolor("black")
seurat = turtle.Turtle()

width = 5
height = 7

dot_distance = 25

seurat.setpos(-250, 250)
seurat.penup()

List=['white','yellow','red','blue','orange','green','pink']


def spiral(m, n):
    k = 0
    l = 0
    f = 0
    seurat.color("white")
    '''
    k= index of the starting row
    l= index of starting column
    '''

    while (k < m and l < n):
        if (f == 1):
            seurat.right(90)

        col=random.randint(0,6)
        seurat.color(List[col])
        for i in range(k, m):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[k][i],end=" ")
        k += 1
        f = 1

        seurat.right(90)
        col = random.randint(0, 6)
        seurat.color(List[col])
        for i in range(k, m):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[i][n-1],end=" ")
        n -= 1
        seurat.right(90)

        if (k < m):
            col = random.randint(0, 6)
            seurat.color(List[col])
            for i in range(n - 1, l - 1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
                # print(a[m-1][i],end=" ")
            m -= 1

        seurat.right(90)
        if (l < n):
            col = random.randint(0, 6)
            seurat.color(List[col])
            for i in range(m - 1, k - 1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
                # print(a[i][l],end=" ")
            l += 1


spiral(20, 20)

turtle.done()
