import tkinter as tk
from PIL import Image, ImageTk
import servicepage
import Homepage
from Homepage import *


class aboutUs:
    def __init__(self, win, image_path):
        self.win = win
        self.win.title("About Us")
        self.win.geometry("1000x400")

        font_style = ("Helvetica", 15)

        # Nav Frame
        self.nav_frame = tk.Frame(win, relief="solid")
        self.nav_frame.grid(row=0, column=0)

        self.home_label = tk.Label(self.nav_frame, text="Home", font=font_style)
        self.home_label.grid(row=0, column=0, padx=5, pady=5)
        self.home_label.bind("<Button-1>", lambda event: self.redirect_to_homepage())


        self.aboutus_label = tk.Label(self.nav_frame, text="About Us", font=font_style)
        self.aboutus_label.grid(row=0, column=1, padx=5, pady=5)



        self.services_label = tk.Label(self.nav_frame, text="Services", font=font_style)
        self.services_label.grid(row=0, column=2, padx=5, pady=5)
        self.services_label.bind("<Button-1>", lambda event: self.redirect_to_servicepage())


        # Image Frame
        self.img_frame = tk.Frame(win,relief="solid")

        
        self.img_frame.grid(row=1, column=0)

        self.load_image(image_path)

        # Content Frame
        self.con_frame = tk.Frame(win,relief="solid")
        self.con_frame.grid(row=1, column=1)

        # Content Frame Content
        self.con_label = tk.Label(self.con_frame, text="Welcome!  where shopping becomes an experience our journey began with a simple vision: to create a retail haven that goes beyond transactions and embraces connections. For years, we have been curating a collection of different craps that reflects our commitment to quality, style, and value. Our journey is marked by a passion for providing customers with not just products but memories.", 
                                  font=font_style, wraplength=500,justify="left")
        self.con_label.grid(row=0,column=0,padx=5,pady=5)

        #footer frame
        self.footer_frame = tk.Frame(win,relief="solid")
        self.footer_frame.grid(row=3, column=0)

        #footer frame content
        self.contact_label = tk.Label(self.footer_frame, text="Contact Number: 8456798567", font=font_style)
        self.contact_label.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        # self.contact_label.rowconfigure(0, weight=1)                                      # Make the row expandable
        # self.contact_label.columnconfigure(0, weight=1)     

        self.email_label = tk.Label(self.footer_frame, text="Email Address: abc@gmail.com", font=font_style)
        self.email_label.grid(row=1, column=0,padx=5,pady=5) 

        self.address_label = tk.Label(self.footer_frame, text="Address: Maple Street New York NY", font=font_style)
        self.address_label.grid(row=2, column=0,padx=5,pady=5)       



    def load_image(self, path):
        try:
            self.image = Image.open(path)
            self.img_resizem = self.image.resize((350,200))
            self.img = ImageTk.PhotoImage(self.img_resizem)
            self.img_lbl = tk.Label(self.img_frame, image=self.img)
            self.img_lbl.grid(row=0, column=0)
        except Exception as e:
            print("Error loading image:", e)

    def redirect_to_homepage(self):
        self.win.destroy()  # Destroy current window
        win = tk.Tk()        # Create a new Tkinter window
        app = Homepage.homepage(win,image_path)  # Display the homepage
        win.mainloop()
    
    def redirect_to_servicepage(self):
        self.win.destroy()  # Destroy current window
        win = tk.Tk()        # Create a new Tkinter window
        app = servicepage.servicepage(win,image_path)  # Display the service page
        win.mainloop()
                                                                                                                                                                                                                                
if __name__ == "__main__":
    image_path = r"C://Python//Scrap_Management//login_img.jpg"
    win = tk.Tk()
    app = aboutUs(win, image_path=image_path)  # Provide the image path here
    win.mainloop()

