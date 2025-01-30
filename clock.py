import tkinter as tk
import time
import math

width = 400
height = 400

root = tk.Tk()
root.title("Analog Clock")
canvas = tk.Canvas(root, width=width, height=height, bg="purple")
canvas.pack()

def update_clock():
    canvas.delete("all")
    



    canvas.create_oval(2, 2, width, height, outline="black", width=2)





    for i in range(12):
        angle = i * math.pi / 6 - math.pi / 2
        x = width / 2 + 0.7 * width / 2 * math.cos(angle)
        y = height / 2 + 0.7 * height / 2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y, text=str(i+12), font=("Verdana", 16, "bold"))
        else:
            canvas.create_text(x, y, text=str(i), font=("Verdana", 16, "bold"))






    for i in range(60):
        angle = i * math.pi / 30 - math.pi / 2
        x1 = width / 2 + 0.85 * width / 2 * math.cos(angle)
        y1 = height / 2 + 0.85 * height / 2 * math.sin(angle)
        x2 = width / 2 + 0.95 * width / 2 * math.cos(angle)
        y2 = height / 2 + 0.95 * height / 2 * math.sin(angle)
        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="gray", width=1)





    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec





    hour_angle = (hour + minute / 60) * math.pi / 6 - math.pi / 2
    draw_hand(0.5, hour_angle, "black", 5)
    minute_angle = (minute + second / 60) * math.pi / 30 - math.pi / 2
    draw_hand(0.7, minute_angle, "black", 3)
    second_angle = second * math.pi / 30 - math.pi / 2
    draw_hand(0.8, second_angle, "red", 1)






    canvas.after(1000, update_clock)

def draw_hand(length, angle, color, line_width):
    x = width / 2 + length * width / 2 * math.cos(angle)
    y = height / 2 + length * height / 2 * math.sin(angle)
    canvas.create_line(width / 2, height / 2, x, y, fill=color, width=line_width)

# Start the clock
update_clock()
root.mainloop()