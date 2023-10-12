from datetime import datetime
from tkinter import *
import time 
from datetime import datetime


def f1():
    sw.deiconify()
    r.withdraw()


r = Tk()
r.title("Digital Clock")
r.config(background="black")
r.geometry("700x300+100+100")
#r.overrideredirect(1)


def get_time():
    timevar = time.strftime("%I:%M:%S %p")
    clock_lab.config(text=timevar)
    clock_lab.after(200,get_time)




clock_lab =  Label(r,font=("Calibri", 90),bg="black",fg="red")
clock_lab.pack()
sw_btn = Button(r,text="StopWatch",font=("Calibri", 90),command=f1)
sw_btn.pack()
get_time()




counter = 66600
running = False
def counter_label(label):
	def count():
		if running:
			global counter			
			if counter==66600:			
				display="Starting..."
			else:
				tt = datetime.fromtimestamp(counter)
				string = tt.strftime("%H:%M:%S")
				display=string
			label["text"]=display 			
			label.after(1000, count)
			counter += 1
	count()	

def Start(label):
	global running
	running=True
	counter_label(label)
	start["state"]="disabled"
	stop["state"]="normal"
	reset["state"]="normal"

def Stop():
	global running
	start["state"]="normal"
	stop["state"]="disabled"
	reset["state"]="normal"
	running = False

def Reset(label):
	global counter
	counter=66600

	if running==False:	
		reset["state"]="disabled"
		label["text"]="Welcome!"

	else:			
		label["text"]="Starting..."

sw = Tk()
sw.title("Stopwatch")

sw.minsize(width=750, height=350)
sw.config(background="black")
label = Label(sw, text="Welcome!", fg="red",bg="black", font="Verdana 30 bold")
label.pack()
f = Frame(sw)
start = Button(f, text="Start", font="Verdana 40 bold",fg="red", command=lambda:Start(label))
stop = Button(f, text="Stop",font="Verdana 40 bold",fg="red",state="disabled", command=Stop)
reset = Button(f, text="Reset",font="Verdana 40 bold",fg="red", state="disabled", command=lambda:Reset(label))
f.pack(anchor = "center",pady=5)
start.pack(side="left", padx=10)
stop.pack(side ="left", padx=10)
reset.pack(side="left", padx=10)
sw.withdraw()

def on_closing():
	
	r.destroy()
	sw.destroy()
r.protocol("WM_DELETE_WINDOW", on_closing)
sw.protocol("WM_DELETE_WINDOW", on_closing)


r.mainloop()