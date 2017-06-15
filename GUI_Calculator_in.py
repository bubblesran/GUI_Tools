#-*-coding: utf-8-*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math

root = Tk()
root.title('Calculator')

# Main Frame setting
mainframe = ttk.Frame(root, padding="8 4")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Label setting
ttk.Label(mainframe, text="Category：").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Item：").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="Direction：").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Open：").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Close：").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Volume：").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Duration：").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Balance：").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Margin：").grid(column=3, row=3, sticky=E)
ttk.Label(mainframe, text="Swap：").grid(column=3, row=4, sticky=E)
ttk.Label(mainframe, text="P&L：").grid(column=3, row=5, sticky=E)
ttk.Label(mainframe, text="Affordable Rate：").grid(column=3, row=6, sticky=E)

# Text Entries setting
def vfunc(action, value_if_allowed, text):
	if action == '1':
		if text in '0123456789.-':
			try: 
				float(value_if_allowed)
				return True
			except ValueError:
				return False
		else: return False
	else: return True
vcmd = (mainframe.register(vfunc), '%d', '%P', '%S')

open = StringVar()
open_entry = ttk.Entry(mainframe, width=12, textvariable=open, validate='key', validatecommand=(vcmd))
open_entry.grid(column=2, row=3, sticky=(W, E))
close = StringVar()
close_entry = ttk.Entry(mainframe, width=12, textvariable=close, validate='key', validatecommand=(vcmd))
close_entry.grid(column=2, row=4, sticky=(W, E))
lot = StringVar()
lot_entry = ttk.Entry(mainframe, width=12, textvariable=lot, validate='key', validatecommand=(vcmd))
lot_entry.grid(column=2, row=5, sticky=(W, E))
duration = StringVar()
duration_entry = ttk.Entry(mainframe, width=12, textvariable=duration, validate='key', validatecommand=(vcmd))
duration_entry.grid(column=2, row=6, sticky=(W, E))
balance = StringVar()
balance_entry = ttk.Entry(mainframe, width=12, textvariable=balance, validate='key', validatecommand=(vcmd))
balance_entry.grid(column=2, row=7, sticky=(W, E))

# combo setting
category = {'metal':['llg','lls'],
'energy':['oil','oil2000','gas'], 
'fx':['eurusd','eurjpy','usdjpy','audusd','gbpusd','eurgbp','usdcny','nzdusd','usdcad','usdswd'],
'index':['d300','sp500','a50','f100','j225','g30'],
'stock':['apple','ali']}

categorycombo = ttk.Combobox(mainframe, width=12, values=list(category.keys()))
categorycombo.grid(column=2, row=1)
itemcombo = ttk.Combobox(mainframe, width=12)
itemcombo.grid(column=4, row=1)

def eventfunction(event):
	itemcombo['values'] = category[categorycombo.get()]

categorycombo.bind('<<ComboboxSelected>>', eventfunction)

inoutcombo = ttk.Combobox(mainframe, width=12, values=['buy','sell'])
inoutcombo.grid(column=2, row=2)

# product class
class product():

	def __init__(self, name):
		self.name = name
	
	def margin(self):
		if self.name == 'lls': return 650
		elif self.name in ['eurusd','eurjpy','eurgbp']:return 600
		elif self.name in ['usdjpy','audusd','nzdusd','usdcad']:return 200
		elif self.name == 'd300':return 5000
		else: return 1000
	
	def rate_in(self):
		if self.name == 'a50':return 0.03
		elif self.name == 'sp500':return 0.025
		elif self.name in ['llg','lls']:return 0.01
		elif self.name in ['d300','apple','ali']:return 0.05
		else: return 0
	
	def rate_out(self):
		if self.name == 'a50':return 0.03
		elif self.name == 'sp500':return 0.025
		elif self.name in ['llg','lls']:return 0.005
		elif self.name in ['d300','apple','ali']:return 0.05
		else: return 0
	
	def unit(self):
		if self.name in ['j225','a50']:return 5
		elif self.name in ['f100','g30']:return 10
		elif self.name == 'd300':return 50
		elif self.name in ['llg','sp500']:return 100
		elif self.name in ['apple','ali']:return 200
		elif self.name in ['oil','oil2000']:return 1000
		elif self.name == 'lls':return 5000
		elif self.name == 'gas':return 10000
		else: return 100000

# calculating function
def calculator(item, direction, open, close, lot, duration, balance):
	if direction == 'buy':
		margin = item.margin()*lot
		interest = open*lot*item.unit()*item.rate_in()/360*duration
		net = (close-open)*lot*item.unit()-interest
		aford = (balance - lot*margin*0.3)/(lot*item.unit())
	else:
		margin = item.margin()*lot
		interest = open*lot*item.unit()*item.rate_out()/360*duration
		net = (open-close)*lot*item.unit()-interest
		aford = (balance - lot*margin*0.3)/(lot*item.unit())
	return margin, interest, net, aford

# output setting
def runbutton(*args):
	vopen = float(open.get())
	vclose = float(close.get())
	vlot = float(lot.get())
	vduration = int(duration.get())
	vbalance = float(balance.get())
	direction = inoutcombo.get()
	item = itemcombo.get()
	prod = product(item)
	margin, interest, net, aford = calculator(prod, direction, vopen, vclose, vlot, vduration, vbalance)
	margin_o.set(margin)
	interest_o.set(interest)
	net_o.set(net)
	aford_o.set(aford)

margin_o = StringVar()
interest_o = StringVar()
net_o = StringVar()
aford_o = StringVar()

margin_l = ttk.Label(mainframe, textvariable=margin_o)
margin_l.grid(column=4, row=3, sticky=(W, E))
interest_l = ttk.Label(mainframe, textvariable=interest_o)
interest_l.grid(column=4, row=4, sticky=(W, E))
net_l = ttk.Label(mainframe, textvariable=net_o)
net_l.grid(column=4, row=5, sticky=(W, E))
aford_l = ttk.Label(mainframe, textvariable=aford_o)
aford_l.grid(column=4, row=6, sticky=(W, E))

ttk.Button(mainframe, text='run', command=runbutton).grid(column=1, row=8)

# Reset function
def reset(*args):
	open_entry.delete(0,END)
	close_entry.delete(0,END)
	lot_entry.delete(0,END)
	duration_entry.delete(0,END)
	balance_entry.delete(0,END)
	categorycombo.set('')
	itemcombo.set('')
	inoutcombo.set('')
	margin_o.set('')
	interest_o.set('')
	net_o.set('')
	aford_o.set('')

ttk.Button(mainframe, text='reset', command=reset).grid(column=2, row=8)

# Enter Button setting
entry_list = [child for child in mainframe.winfo_children() if isinstance(child, Entry)]
def pressreturn(*args):
	count = 0
	for entry in entry_list:
		if not entry.get():
			 messagebox.showinfo(title='Warning', message = 'Entry all values')
			 break
		else: count+=1
	if count>=8:
		runbutton()
root.bind('<Return>', pressreturn)

# Start the application
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()