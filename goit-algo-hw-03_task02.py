
import turtle

def koch_line(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_line(t, length, level - 1)
        t.left(60)
        koch_line(t, length, level - 1)
        t.right(120)
        koch_line(t, length, level - 1)
        t.left(60)
        koch_line(t, length, level - 1)

def draw_snowflake(level):
    t = turtle.Turtle()
    t.speed(0)

    for _ in range(3):
        koch_line(t, 300, level)
        t.right(120)

    turtle.done()

def main():
    print("= Сніжинка коха =")
    level = int(input("Введіть рівень рекурсії (наприклад 3 чи 4): "))
    draw_snowflake(level)



if __name__ == "__main__":
    main()
