import tkinter as tk

class user_registration:
    def __init__(self,win):
        self.win = win
        win.configure(bg='black')
        self.win.title("Registration Page")
        win.columnconfigure(0, weight=1)
        win.rowconfigure(0, weight=1)

        font_style=("Helvetica" , 15)

        # Frame in our Window
        self.frame = tk.Frame(win,background='black')
        self.frame.place(relx=0.5,rely=0.5,anchor="center")
        self.frame.grid(row=0,column=0,sticky="nsew")
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
                    
        # Creating registration page
        self.main_label = tk.Label(self.frame, text = 'Register' , bg='orange',font=font_style)
        self.main_label.grid(row=0, column=0,columnspan=2,padx=5,pady=5)
        self.fname_label = tk.Label(self.frame , text = 'First Name' ,font=font_style, bg='orange' )
        self.fname_label.grid(row=1,column=0,columnspan=1,padx=5,pady=5)

        self.fname_entry = tk.Entry(self.frame , borderwidth=4,font=font_style)
        self.fname_entry.grid(row=2,column=0,columnspan=1,padx=5,pady=5 )

        self.lname_label = tk.Label (self.frame, text = 'Last Name',font=font_style, bg='orange')
        self.lname_label.grid(row=3,column=0,columnspan=1,padx=5,pady=5)

        self.lname_entry = tk.Entry(self.frame, borderwidth=4,font=font_style)
        self.lname_entry.grid(row = 4,column=0, columnspan=1,padx=5,pady=5)

        self.email_label = tk.Label(self.frame , text = 'Email' ,font=font_style, bg='orange')
        self.email_label.grid(row=5,column=0, columnspan=1,padx=5,pady=5)

        self.email_entry = tk.Entry(self.frame, borderwidth=4,font=font_style)
        self.email_entry.grid(row=6,column=0,columnspan=1,padx=5,pady=5)

        self.password_label = tk.Label(self.frame , text = 'Password',font=font_style, bg='orange')
        self.password_label.grid(row=7,column=0,columnspan=1,padx=5,pady=5)

        self.password_entry = tk.Entry(self.frame, borderwidth=4,font=font_style)
        self.password_entry.grid(row=8,column=0,columnspan=1,padx=5,pady=5)
        
        self.button = tk.Button(text='Submit', bg='green',font=font_style)
        self.button.grid(row=12,column=0,columnspan=1,padx=5,pady=5)

        font_style2 = ("impact", 12) 

        self.regist_label = tk.Label(text='If already registered',font=font_style2,bg='blue',fg='white')
        self.regist_label.grid(row=13,column=0,columnspan=2,padx=5,pady=5)
 
        self.button = tk.Button(text='Login', bg='green',font=font_style)
        self.button.grid(row=14,column=0,columnspan=2,padx=5,pady=5)

        

# Object Initialization
if __name__ == '__main__':
    win = tk.Tk()
    app = user_registration(win)
    win.mainloop()
