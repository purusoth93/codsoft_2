from tkinter import *
from tkinter import ttk

class calculator(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("500x400")
        self.title("Simple calculator")
        self.configure(pady=50,bg="pink")
        self.create_widget()
        
    def create_widget(self):
        #head label
        self.head=Label(text="CALCULATOR",font=("bold",10),bg="pink")
        self.head.pack(padx=20)
        
        #creating text box
        self.text_entry=Entry(self,width=40)
        self.text_entry.pack(pady=25,padx=25)
        
        #creating frame for inserting button
        self.butn_frame=Frame(self,bg="pink")
        self.butn_frame.pack(pady=10)
        
        #creating number buttons
        self.butn_one=Button(self.butn_frame,text="1",width=3,command=lambda t="1":self.entry(t))
        self.butn_one.grid(row=0,column=0,padx=5,pady=5)
        
        self.butn_two=Button(self.butn_frame,text="2",width=3,command=lambda t="2":self.entry(t))
        self.butn_two.grid(row=0,column=1,padx=5,pady=5)
        
        self.butn_three=Button(self.butn_frame,text="3",width=3,command=lambda t="3":self.entry(t))
        self.butn_three.grid(row=0,column=2,padx=5,pady=5)
        
        self.butn_four=Button(self.butn_frame,text="4",width=3,command=lambda t="4":self.entry(t))
        self.butn_four.grid(row=1,column=0,padx=5,pady=5)
        
        self.butn_five=Button(self.butn_frame,text="5",width=3,command=lambda t="5":self.entry(t))
        self.butn_five.grid(row=1,column=1,padx=5,pady=5)
        
        self.butn_six=Button(self.butn_frame,text="6",width=3,command=lambda t="6":self.entry(t))
        self.butn_six.grid(row=1,column=2,padx=5,pady=5)
        
        self.butn_seven=Button(self.butn_frame,text="7",width=3,command=lambda t="7":self.entry(t))
        self.butn_seven.grid(row=2,column=0,padx=5,pady=5)
        
        self.butn_eight=Button(self.butn_frame,text="8",width=3,command=lambda t="8":self.entry(t))
        self.butn_eight.grid(row=2,column=1,padx=5,pady=5)
        
        self.butn_nine=Button(self.butn_frame,text="9",width=3,command=lambda t="9":self.entry(t))
        self.butn_nine.grid(row=2,column=2,padx=5,pady=5)
        
        self.butn_zero=Button(self.butn_frame,text="0",width=3,command=lambda t="0":self.entry(t))
        self.butn_zero.grid(row=3,column=1,padx=5,pady=5)
        
        #creating symbol buttons
        
        self.butn_plus=Button(self.butn_frame,text="+",width=3,command=lambda t="+":self.entry(t))
        self.butn_plus.grid(row=0,column=3,padx=5,pady=5)
        
        self.butn_minus=Button(self.butn_frame,text="-",width=3,command=lambda t="-":self.entry(t))
        self.butn_minus.grid(row=1,column=3,padx=5,pady=5)
        
        self.butn_mul=Button(self.butn_frame,text="*",width=3,command=lambda t="*":self.entry(t))
        self.butn_mul.grid(row=2,column=3,padx=5,pady=5)
        
        self.butn_div=Button(self.butn_frame,text="/",width=3,command=lambda t="/":self.entry(t))
        self.butn_div.grid(row=3,column=3,padx=5,pady=5)
        
        self.butn_equal=Button(self.butn_frame,text="=",width=3,command=self.evaluate)
        self.butn_equal.grid(row=3,column=2,padx=5,pady=5)
        
        self.butn_clr=Button(self.butn_frame,text="clr",width=3,command=self.clear)
        self.butn_clr.grid(row=3,column=0,padx=5,pady=5)
        
    def entry(self,s):
        self.text_entry.insert(END,s)
        
    def evaluate(self):
        task=self.text_entry.get()
        if task:
            result=eval(task)
            self.text_entry.delete(0,END)
            self.text_entry.insert(0,result)
    
            
    def clear(self):
        self.text_entry.delete(0,END)
        
app=calculator()
app.mainloop()
        