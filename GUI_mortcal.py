# -*-coding: utf-8 -*-
# GUI mortgage calculator

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Main Frame
class MainApplication:
	
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		parent.title('Mortgage Calculator')
		self.main = ttk.Frame(parent, padding="5 4")
		self.main.grid(column=0, row=0, sticky=(N, W, E, S))
		self.main.columnconfigure(0, weight=1)
		self.main.rowconfigure(0, weight=1)
		#labels
		self.prinlabel = ttk.Label(self.main, text='Principal: ')
		self.prinlabel.grid(column=1, row=1, sticky=W)
		self.ratelabel = ttk.Label(self.main, text='Interest: ')
		self.ratelabel.grid(column=1, row=2, sticky=W)
		self.duralabel = ttk.Label(self.main, text='Duration: ')
		self.duralabel.grid(column=1, row=3, sticky=W)
		self.monthlabel = ttk.Label(self.main, text='Monthly Cost: ')
		self.monthlabel.grid(column=3, row=1, sticky=E)
		self.totallabel = ttk.Label(self.main, text='Total Cost: ')
		self.totallabel.grid(column=3, row=2, sticky=E)
		self.inparlabel = ttk.Label(self.main, text='Interest Cost: ')
		self.inparlabel.grid(column=3, row=3, sticky=E)
		self.pmonthlabel = ttk.Label(self.main, text='Pressure Monthly Cost: ')
		self.pmonthlabel.grid(column=3, row=4, sticky=E)
		self.incomlabel = ttk.Label(self.main, text='Required Income: ')
		self.incomlabel.grid(column=3, row=5, sticky=E)
		# inputs
		vcmd = (self.main.register(vfunc), '%d', '%P', '%S')
		self.principal = StringVar()
		self.principal_entry = ttk.Entry(self.main, width=12, textvariable=self.principal, validate='key', validatecommand=(vcmd))
		self.principal_entry.grid(column=2, row=1, sticky=(W, E))
		self.interest = StringVar()
		self.interest_entry = ttk.Entry(self.main, width=12, textvariable=self.interest, validate='key', validatecommand=(vcmd))
		self.interest_entry.grid(column=2, row=2, sticky=(W, E))
		self.duration = StringVar()
		self.duration_entry = ttk.Entry(self.main, width=12, textvariable=self.duration, validate='key', validatecommand=(vcmd))
		self.duration_entry.grid(column=2, row=3, sticky=(W, E))
		# outputs
		self.monthly = StringVar()
		self.total = StringVar()
		self.ratepart = StringVar()
		self.pmonthly = StringVar()
		self.income = StringVar()
		self.monthly_l = ttk.Label(self.main, width=15, textvariable=self.monthly)
		self.monthly_l.grid(column=4, row=1, sticky=W)
		self.total_l = ttk.Label(self.main, width=15, textvariable=self.total)
		self.total_l.grid(column=4, row=2, sticky=W)
		self.rate_l = ttk.Label(self.main, width=15, textvariable=self.ratepart)
		self.rate_l.grid(column=4, row=3, sticky=W)
		self.pm_l = ttk.Label(self.main, width=15, textvariable=self.pmonthly)
		self.pm_l.grid(column=4, row=4, sticky=W)
		self.income_l = ttk.Label(self.main, width=15, textvariable=self.income)
		self.income_l.grid(column=4, row=5, sticky=W)
		#buttons
		self.runbutton = ttk.Button(self.main, text='run', command=self.pressreturn)
		self.runbutton.grid(column=1, row=4)
		self.resetbutton = ttk.Button(self.main, text='reset', command=self.reset)
		self.resetbutton.grid(column=1, row=5)
		self.main.pack()
	
	def pressreturn(self, *args, **kwargs):
		entry_list = [self.principal, self.interest, self.duration]
#		for entry in entry_list: print(entry.get())
		count = 0
		for entry in entry_list:
			if not entry.get():
				messagebox.showinfo(title='Warning', message = 'Entry all values')
				return False
				break
			else: count+=1
#		print(count)
		if count>=3:
			self.core_run()
	
	def core_run(self):
		p = float(self.principal.get())
		yr = float(self.interest.get())
		r = yr*0.01/12
		pr = r+0.0025
		d = int(self.duration.get())
		out = float(calculator(p, r, d))
		p_out = float(calculator(p, pr, d))
		rqi = p_out/0.6
		total_debt = out*d
		inpart = total_debt - p
		out = round(out,4)
		p_out = round(p_out,4)
		rqi = round(rqi,4)
		total_debt = round(total_debt,4)
		inpart = round(inpart,4)
		self.monthly.set(out)
		self.total.set(total_debt)
		self.ratepart.set(inpart)
		self.pmonthly.set(p_out)
		self.income.set(rqi)
	
	def reset(self, *args, **kwargs):
		self.principal_entry.delete(0, END)
		self.interest_entry.delete(0, END)
		self.duration_entry.delete(0, END)
		self.monthly.set('')
		self.total.set('')
		self.ratepart.set('')
		self.pmonthly.set('')
		self.income.set('')

def calculator(p, r, d):
	nr = 1+r
	R = nr**d
	output = p*(r*R)/(R-1)
	return output


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
	app = MainApplication(root)
	root.bind('<Return>', app.pressreturn)
	root.mainloop()

if __name__ == '__main__':
	main()