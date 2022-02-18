from PIL import Image, ImageDraw


def draw_by_points(way):
    first_floor = Image.open('Images/Prototype_First_Floor.png')

    second_floor = Image.open('Images/Prototype_Second_Floor.png')

    privius_point = ''

    for i in way:

        if privius_point == '':
            privius_point = i
            continue

        if i[0] == 'f':
            if privius_point == 's':
                privius_point = i
                continue
            draw = ImageDraw.Draw(first_floor)

        if i[0] == 's':
            if privius_point == 'f':
                privius_point = i
                continue
            draw = ImageDraw.Draw(second_floor)

        draw.line((coordinats[privius_point][0], coordinats[privius_point][1], coordinats[i][0], coordinats[i][1]), fill=128, width=3)


        privius_point = i

    first_floor_name = "Test/Prototype_First_Floor.png"
    second_floor_name = "Test/Prototype_Second_Floor.png"

    first_floor.save(first_floor_name)
    second_floor.save(second_floor_name)


# points



coordinats = {

    # first floor

    'f1': [630, 300],
    'f2': [710, 275],
    'f3': [630, 270],
    'f4': [680, 230],
    'f5': [620, 190],
    'f6': [695, 170],
    'f7': [695, 130],
    'f8': [580, 130],
    'f9': [580, 270],
    'f10': [520, 270],
    'f11': [470, 290],
    'f12': [520, 180],
    'f13': [400, 180],
    'f14': [420, 130],
    'f15': [500, 100],
    'f20': [380, 180],
    'f16': [370, 200],
    'f17': [200, 180],
    'f18': [110, 180],
    'f19': [110, 220],

    # second floor

    's1': [110, 220],
    's2': [120, 180],
    's3': [200, 180],
    's4': [200, 200],
    's5': [350, 180],
    's6': [350, 200],
    's8': [350, 160],
    's9': [410, 180],
    's10': [400, 200],
    's12': [415, 160],
    's13': [640, 180],
    's14': [640, 90],
    's15': [540, 90],
    's16': [640, 200],
    's17': [790, 180],
    's18': [790, 200],
    's19': [1070, 180],
    's20': [1070, 160],
    's21': [1170, 180],
    's22': [1170, 200],
}



# --------------------------------------------

way = ['f1', 'f3', 'f4', 'f6', 'f7', 'f8', 's15', 's14', 's13', 's9', 's5', 's3', 's2', 's1', 'f19', 'f18', 'f17']

#draw_by_points(way)

#for i in way:
#    print(f' {i} --> ', end='')

# from tkinter import *
# from tkinter import messagebox
#
# def on_closing():
#     if messagebox.askokcancel("Exit?", "Do you want?"):
#         tk.destroy()
#
# tk = Tk()
# tk.protocol('WM_DELETE_WINDOW', on_closing)
# tk.title("Application")
# tk.resizable(0, 0)
# #tk.wm_attributes("-topmost", 1)
# canvas = Canvas(tk, width=900, height=600, bd=0, highlightthickness=0)
#
#
# ground_floor_image = PhotoImage(file = 'Images/Prototype_Ground_Floor.png')
# ground_floor_image = ground_floor_image.subsample(2, 2)
# ground_floor_lable = Label(tk)
# ground_floor_lable.image = ground_floor_image
# ground_floor_lable['image'] = ground_floor_lable.image
# ground_floor_lable.place(x = 0, y = 0)
#
# first_floor_image = PhotoImage(file = 'Images/Prototype_First_Floor.png')
# first_floor_image = first_floor_image.subsample(2, 2)
# first_floor_lable = Label(tk)
# first_floor_lable.image = first_floor_image
# first_floor_lable['image'] = first_floor_lable.image
# first_floor_lable.place(x = 0, y = 160)
#
# canvas.create_line(50, 50, 1000, 50)
# canvas.pack()
# tk.mainloop()