#-*-coding: utf-8-*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math

class Mainapp:
	
	def __init__(self, master):
		# Main Frame setting
		self.master = master
		master.title('Calculator')
		self.main = ttk.Frame(master, padding="8 4")
		self.main.grid(column=0, row=0, sticky=(N, W, E, S))
		self.main.columnconfigure(0, weight=1)
		self.main.rowconfigure(0, weight=1)
		self.category = {'metal':['llg','lls'],
		'energy':['oil','oil2000','gas'], 
		'fx':['eurusd','eurjpy','usdjpy','audusd','gbpusd','eurgbp','usdcny','nzdusd','usdcad','usdswd'],
		'index':['d300','sp500','a50','f100','j225','g30'],
		'stock':['apple','ali']}
		self.labels_widget()
		self.entries_widget()
		self.combos_widget()
		self.outputs_widget()
		self.buttons_widget()
	
	def labels_widget(self):
		# Labels setting
		self.category_label = ttk.Label(self.main, text="Category：")
		self.category_label.grid(column=1, row=1, sticky=W)
		self.buy_label = ttk.Label(self.main, text="Direction：")
		self.buy_label.grid(column=1, row=2, sticky=W)
		self.open_label = ttk.Label(self.main, text="Open：")
		self.open_label.grid(column=1, row=3, sticky=W)
		self.close_label = ttk.Label(self.main, text="Close：")
		self.close_label.grid(column=1, row=4, sticky=W)
		self.vol_label = ttk.Label(self.main, text="Volume：")
		self.vol_label.grid(column=1, row=5, sticky=W)
		self.duration_label = ttk.Label(self.main, text="Duration：")
		self.duration_label.grid(column=1, row=6, sticky=W)
		self.bal_label = ttk.Label(self.main, text="Balance：")
		self.bal_label.grid(column=1, row=7, sticky=W)
		self.item_label = ttk.Label(self.main, text="Item：")
		self.item_label.grid(column=3, row=1, sticky=E)
		self.margin_label = ttk.Label(self.main, text="Margin：")
		self.margin_label.grid(column=3, row=3, sticky=E)
		self.swap_label = ttk.Label(self.main, text="Swap：")
		self.swap_label.grid(column=3, row=4, sticky=E)
		self.pl_label = ttk.Label(self.main, text="P&L：")
		self.pl_label.grid(column=3, row=5, sticky=E)
		self.aff_label = ttk.Label(self.main, text="Affordable Rate：")
		self.aff_label.grid(column=3, row=6, sticky=E)
	
	def entries_widget(self):
		#Entries setting
		vcmd = (self.main.register(vfunc), '%d', '%P', '%S')
		self.open = StringVar()
		self.open_entry = ttk.Entry(self.main, width=12, textvariable=self.open, validate='key', validatecommand=(vcmd))
		self.open_entry.grid(column=2, row=3, sticky=(W, E))
		self.close = StringVar()
		self.close_entry = ttk.Entry(self.main, width=12, textvariable=self.close, validate='key', validatecommand=(vcmd))
		self.close_entry.grid(column=2, row=4, sticky=(W, E))
		self.lot = StringVar()
		self.lot_entry = ttk.Entry(self.main, width=12, textvariable=self.lot, validate='key', validatecommand=(vcmd))
		self.lot_entry.grid(column=2, row=5, sticky=(W, E))
		self.duration = StringVar()
		self.duration_entry = ttk.Entry(self.main, width=12, textvariable=self.duration, validate='key', validatecommand=(vcmd))
		self.duration_entry.grid(column=2, row=6, sticky=(W, E))
		self.balance = StringVar()
		self.balance_entry = ttk.Entry(self.main, width=12, textvariable=self.balance, validate='key', validatecommand=(vcmd))
		self.balance_entry.grid(column=2, row=7, sticky=(W, E))
	
	def combos_widget(self):
		# combo setting
		self.categorycombo = ttk.Combobox(self.main, width=12, values=list(self.category.keys()))
		self.categorycombo.grid(column=2, row=1)
		self.itemcombo = ttk.Combobox(self.main, width=12)
		self.itemcombo.grid(column=4, row=1)
		self.inoutcombo = ttk.Combobox(self.main, width=12, values=['buy','sell'])
		self.inoutcombo.grid(column=2, row=2)
		self.categorycombo.bind('<<ComboboxSelected>>', self.eventfunction)
	
	def eventfunction(self, *args, **kwargs):
		#combo interaction
		self.itemcombo['values'] = self.category[self.categorycombo.get()]
	
	def outputs_widget(self):
		#outputs setting
		self.margin_o = StringVar()
		self.interest_o = StringVar()
		self.net_o = StringVar()
		self.aford_o = StringVar()
		self.margin_l = ttk.Label(self.main, textvariable=self.margin_o)
		self.margin_l.grid(column=4, row=3, sticky=(W, E))
		self.interest_l = ttk.Label(self.main, textvariable=self.interest_o)
		self.interest_l.grid(column=4, row=4, sticky=(W, E))
		self.net_l = ttk.Label(self.main, textvariable=self.net_o)
		self.net_l.grid(column=4, row=5, sticky=(W, E))
		self.aford_l = ttk.Label(self.main, textvariable=self.aford_o)
		self.aford_l.grid(column=4, row=6, sticky=(W, E))
	
	def buttons_widget(self):
		#buttons setting
		self.reset_button = ttk.Button(self.main, text='reset', command=self.reset)
		self.reset_button.grid(column=2, row=8)
		self.run_button = ttk.Button(self.main, text='run', command=self.pressreturn)
		self.run_button.grid(column=1, row=8)
	
	def reset(self, *args, **kwargs):
		self.open_entry.delete(0,END)
		self.close_entry.delete(0,END)
		self.lot_entry.delete(0,END)
		self.duration_entry.delete(0,END)
		self.balance_entry.delete(0,END)
		self.categorycombo.set('')
		self.itemcombo.set('')
		self.inoutcombo.set('')
		self.margin_o.set('')
		self.interest_o.set('')
		self.net_o.set('')
		self.aford_o.set('')
	
	def pressreturn(self, *args, **kwargs):
		count = 0
		entry_list = [child for child in self.main.winfo_children() if isinstance(child, Entry)]
		for entry in entry_list:
			if not entry.get():
				messagebox.showinfo(title='Warning', message = 'Entry all values')
				return False
				break
			else: count+=1
		if count>=8:
			self.runbutton()
	
	def runbutton(self):
		vopen = float(self.open.get())
		vclose = float(self.close.get())
		vlot = float(self.lot.get())
		vduration = int(self.duration.get())
		vbalance = float(self.balance.get())
		direction = self.inoutcombo.get()
		item = self.itemcombo.get()
		prod = product(item)
		margin, interest, net, aford = calculator(prod, direction, vopen, vclose, vlot, vduration, vbalance)
		self.margin_o.set(margin)
		self.interest_o.set(interest)
		self.net_o.set(net)
		self.aford_o.set(aford)

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

def main():
	root = Tk()
	app = Mainapp(root)
	for child in app.main.winfo_children(): child.grid_configure(padx=5, pady=5)
	root.bind('<Return>', app.pressreturn)
	root.mainloop()

# Start the application
if __name__ == '__main__':
	main()