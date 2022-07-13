from tkinter import *

root = Tk()
root.title('Chronometer')
root.config(bg='black')
width, height = 300, 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width / 2 - width / 2
y = screen_height / 2 - height / 2
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
msec = sec = min_ = 0

def start():
	global time, timer, msec, sec, min_
	msec += 1
	if msec == 100:
		msec, sec = 0
		sec += 1
	if sec == 60:
		sec, min_ = 0
		min_ += 1
	timer.config(text=f'{min_}:{sec}:{msec}')
	time = timer.after(200, start)

def stop():
	global time
	timer.after_cancel(time)

def reset():
	global msec, sec, min_
	msec = sec = min_ = 0
	timer.config(text=f'{min_}:{sec}:{msec}')
	timer.after_cancel(time)

def exit():
	root.destroy()

Top = Frame(root, width=400, bg='blue')
Top.pack(side=TOP)
Bottom = Frame(root, width=400, bg='black')
Bottom.pack(side=BOTTOM)
Title = Label(Top, text='Chronometer', font=('arial 24 bold'), fg='gold', bg = 'black')
Title.pack()
timer = Label(Top, font=('times new roman', 30), fg='white', bg='black')
timer.pack(fill=X, expand=NO, pady=10)
timer.config(text=f'{min_}:{sec}:{msec}')
sstart = Button(Bottom, text='START', font=('arial 20 bold'), fg='purple4', width=3, command=start)
sstart.pack(side=LEFT, padx=2, pady=5)
sstop = Button(Bottom, text='STOP', font=('arial 20 bold'), fg='purple4', width=3, command=stop)
sstop.pack(side=LEFT, padx=2, pady=5)
rreset = Button(Bottom, text='RESET', font=('arial 20 bold'), fg='purple4', width=3, command=reset)
rreset.pack(side=LEFT, padx=2, pady=5)
eexit = Button(Bottom, text='EXIT', font=('arial 20 bold'), fg='purple4', width=3, command=exit)
eexit.pack(side=LEFT, padx=2, pady=5)
root.mainloop()