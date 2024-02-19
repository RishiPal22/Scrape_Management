import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import aboutUs
import Homepage
from Homepage import *

class servicepage:
    def __init__(self, win, image_path=""):
        self.win = win
        self.win.title("Service Page")
        self.win.geometry("180x370")
        font_style = ("Helvetica", 10)

        def submit():
            conn = sqlite3.connect('scrap_management.db')
            cur = conn.cursor()

            # cur.execute("""CREATE TABLE services(
            #             contact INTEGER,
            #             email TEXT,
            #             address TEXT,
            #             notes TEXT
            #             )""")
            
            cur.execute("INSERT INTO services VALUES (:con_entry, :e_entry, :add_entry, :notes_entry)",
                        {
                            'con_entry':self.con_entry.get(),
                            'e_entry' : self.e_entry.get(),
                            'add_entry':self.add_entry.get(),
                            'notes_entry': self.notes_entry.get()
                        })

            conn.commit()
            conn.close()

            self.con_entry.delete(0, tk.END)
            self.e_entry.delete(0, tk.END)
            self.add_entry.delete(0, tk.END)
            self.notes_entry.delete(0, tk.END)


        def display():
            conn = sqlite3.connect('scrap_management.db')
            cur = conn.cursor()

            cur.execute("SELECT * FROM services")
            
            print(cur.fetchall())

            conn.commit()
            conn.close()

    # Nav Frame
        self.nav_frame = tk.Frame(win)
        self.nav_frame.grid(row=0, column=0)

    # Frame in our Window
        self.frame = tk.Frame(win)
        self.frame.configure(bg='black')
        self.frame.place(relx=0.5,rely=0.5,anchor="center")
        self.frame.grid(row=1,column=0,sticky="nsew")
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)

    # Nav Bar Content
        
        self.home_label = tk.Label(self.nav_frame, text="Home", font=font_style)
        self.home_label.grid(row=0, column=0, padx=5, pady=5)
        self.home_label.bind("<Button-1>", lambda event: self.redirect_to_homepage())


        self.aboutus_label = tk.Label(self.nav_frame, text="About Us", font=font_style)
        self.aboutus_label.grid(row=0, column=1, padx=5, pady=5)
        self.aboutus_label.bind("<Button-1>", lambda event: self.redirect_to_aboutUs())



        self.services_label = tk.Label(self.nav_frame, text="Services", font=font_style)
        self.services_label.grid(row=0, column=2, padx=5, pady=5)
        


    # Frame content
        

        self.main_label = tk.Label(self.frame, text = 'Our Services' , bg='orange',font=font_style)
        self.main_label.grid(row=0, column=0,columnspan=2,padx=5,pady=5)
       
        self.con_label = tk.Label(self.frame , text = 'Contact No' ,font=font_style, bg='orange' )
        self.con_label.grid(row=1,column=0,columnspan=1,padx=5,pady=5)

        self.con_entry = tk.Entry(self.frame , borderwidth=4,font=font_style)
        self.con_entry.grid(row=2,column=0,columnspan=1,padx=5,pady=5 )

        self.e_label = tk.Label (self.frame, text = 'Email ID',font=font_style, bg='orange')
        self.e_label.grid(row=3,column=0,columnspan=1,padx=5,pady=5)

        self.e_entry = tk.Entry(self.frame, borderwidth=4,font=font_style)
        self.e_entry.grid(row = 4,column=0, columnspan=1,padx=5,pady=5)

        self.add_label = tk.Label(self.frame , text = 'Address' ,font=font_style, bg='orange')
        self.add_label.grid(row=5,column=0, columnspan=1,padx=5,pady=5)

        self.add_entry = tk.Entry(self.frame, borderwidth=4,font=font_style)
        self.add_entry.grid(row=6,column=0,columnspan=1,padx=5,pady=5)

        self.notes_label = tk.Label(self.frame , text = 'Notes',font=font_style, bg='orange')
        self.notes_label.grid(row=7,column=0,columnspan=1,padx=5,pady=5)

        self.notes_entry = tk.Entry(self.frame, borderwidth=4,font=font_style)
        self.notes_entry.grid(row=8,column=0,columnspan=1,padx=5,pady=5)

        self.button = tk.Button(self.frame ,text='Submit', bg='green',font=font_style, command=submit)
        self.button.grid(row=9,column=0,columnspan=2,padx=5,pady=5)

        self.button_dis = tk.Button(self.frame ,text='Display', bg='green',font=font_style, command=display)
        self.button_dis.grid(row=10,column=0,columnspan=2,padx=5,pady=5)

    def redirect_to_aboutUs(self):
        self.win.destroy()  # Destroy current window
        win = tk.Tk()        # Create a new Tkinter window
        app = aboutUs.aboutUs(win,image_path)  # Display the service page
        win.mainloop()

    def redirect_to_homepage(self):
        self.win.destroy()  # Destroy current window
        win = tk.Tk()        # Create a new Tkinter window
        app = Homepage.homepage(win,image_path)  # Display the homepage
        win.mainloop()




# Object Instantiation
if __name__ == '__main__':
    image_path = r"C://Python//Scrap_Management//login_img.jpg"
    win = tk.Tk()
    app = servicepage(win)
    win.mainloop()