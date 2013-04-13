# -*- coding: utf-8 -*-
from Tkinter import *
from ttk import *
import os,time
import tkMessageBox
import re,urllib2 
from subprocess import Popen, PIPE

# init and set frame
master = Tk()
master.title('人品大侠人工断线重连换IP器 V0.001')
fm=Frame(master, padding="3 3 9 9")
fm.grid(column=0, row=0, sticky=(N, W, E, S))
fm.columnconfigure(0, weight=1)
fm.rowconfigure(0, weight=1)

#set label
Label(fm, text='宽带名称:',width = 8).grid(row=1,sticky=E)
Label(fm, text='宽带账户:',width = 8).grid(row=2,sticky=E)
Label(fm, text='宽带密码:',width = 8).grid(row=3,sticky=E)

#define var
entyname = StringVar()
account = StringVar()
passport = StringVar()	

#set entry
entry1=Entry(fm ,width = 23,textvariable=entyname)
entry1.grid(row=1,column=1,sticky=W)
entry2=Entry(fm ,width = 23,textvariable=account)
entry2.grid(row=2,column=1,sticky=W)
entry3=Entry(fm ,width = 23,show='*',textvariable=passport)
entry3.grid(row=3,column=1,sticky=W)

#read date
f = file('alist.txt','r')
line = f.readline()
f.close()
if len(line) != 0:
	list1=line.split()
	entyname.set(list1[0])
	account.set(list1[1])
	passport.set(list1[2])
	
def connect2(a,b,c):
	#first disconnect
	os.system('rasdial /Disconnect')	
	i =5
	#call rasdial.exe
	result=os.system('rasdial ' + str(a) + ' ' + str(b) +' ' + str(c))
	#if can't connect,sleep 3s and retry 5 times
	while result !=0 and i !=0:
		time.sleep(3)
		result=os.system('rasdial ' + str(a) + ' ' + str(b) +' ' + str(c))
		i-=1
	#get ip
	try:
		ip_addidas= "连接成功！本机的公网IP是： " + re.search('\d+\.\d+\.\d+\.\d+',urllib2.urlopen("http://www.whereismyip.com").read()).group(0) 
		tkMessageBox.showinfo("",ip_addidas)
	#else show error
	except:
		tkMessageBox.showinfo("","无法连接")
		pass
		
def connect1():
	f = file('alist.txt','r')
	line = f.readline()
	f.close()
	a=entyname.get()
	b=account.get()
	c=passport.get()
	if len(line) == 0:
		write()
		connect2(a,b,c)
	elif line != a+' '+b+' '+c:
		write()
		connect2(a,b,c)
	else:
		connect2(a,b,c)
		
def write():
	f = file('alist.txt','w')
	f.write(entyname.get()+' ')
	f.write(account.get()+ ' ')
	f.write(passport.get())
	f.close()
	
def disconnect():
	os.system('rasdial /Disconnect')
	tkMessageBox.showinfo("","连接中断")

#set button
b=Button(fm, text="连接",command=connect1)
b.grid(column=0, row=5)
Button(fm, text="断开连接", command=disconnect).grid(column=1, row=5,sticky=E)

for child in fm.winfo_children(): child.grid_configure(padx=18, pady=12)
b.focus_force()
b.bind("<Return>", lambda event: b.invoke())
master.mainloop()