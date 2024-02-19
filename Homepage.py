import tkinter as tk
from PIL import Image, ImageTk
import servicepage
import aboutUs


class homepage:
    def __init__(self, win, image_path=""):
        self.win = win
        self.win.title("Home Page")
        self.win.geometry("1240x650")

    

        font_style = ("Helvetica", 10)

        # Nav Frame
        self.nav_frame = tk.Frame(win)
        self.nav_frame.grid(row=0, column=0)

        # Metal Frame
        self.metal_frame = tk.Frame(win, bd=3, relief="solid")
        self.metal_frame.grid(row=1, column=0,padx=10,pady=10)

        # Plastic Frame
        self.plastic_frame = tk.Frame(win, bd=3, relief="solid")
        self.plastic_frame.grid(row=1, column=1,padx=10,pady=10)

        # Paper Frame
        self.paper_frame = tk.Frame(win, bd=3, relief="solid")
        self.paper_frame.grid(row=1, column=2,padx=10,pady=10)

        # E-waste Frame
        self.ewaste_frame = tk.Frame(win, bd=3, relief="solid")
        self.ewaste_frame.grid(row=2, column=0,padx=12,pady=12)

        # unknown Frame
        self.unidentified_frame = tk.Frame(win, bd=3, relief="solid")
        self.unidentified_frame.grid(row=2, column=1,padx=12,pady=12)

        # Load Image
        self.load_plimage(image_path)
        self.load_unimage(image_path)
        self.load_image(image_path)
        self.load_paimage(image_path)
        self.load_ewimage(image_path)

        

        # Nav Bar Content
        self.home_label = tk.Label(self.nav_frame, text="Home", font=font_style)
        self.home_label.grid(row=0, column=0, padx=5, pady=5)

        self.aboutus_label = tk.Label(self.nav_frame, text="About Us", font=font_style)
        self.aboutus_label.grid(row=0, column=1, padx=5, pady=5)
        self.aboutus_label.bind("<Button-1>", lambda event: self.redirect_to_aboutUs())


        self.services_label = tk.Label(self.nav_frame, text="Services", font=font_style)
        self.services_label.grid(row=0, column=2, padx=5, pady=5)
        self.services_label.bind("<Button-1>", lambda event: self.redirect_to_servicepage())

        # Metal Frame Content
        self.metal_label = tk.Label(self.metal_frame, text="METALS", font=font_style)
        self.metal_label.grid(row=4, column=5, padx=5, pady=5)
        self.description_mlabel = tk.Label(self.metal_frame, text="The price of 1kg metal is Rs15", font=font_style)
        self.description_mlabel.grid(row=6,column=5)

        # Plastic Frame Content
        self.plastic_label = tk.Label(self.plastic_frame, text="PLASTICS", font=font_style)
        self.plastic_label.grid(row=4, column=5, padx=5, pady=5)
        self.description_pllabel = tk.Label(self.plastic_frame, text="The price of 1kg Plastic is Rs15", font=font_style)
        self.description_pllabel.grid(row=6,column=5)

        # Paper Frame Content
        self.paper_label = tk.Label(self.paper_frame, text="PAPER", font=font_style)
        self.paper_label.grid(row=0, column=5, padx=5, pady=5)
        self.description_palabel = tk.Label(self.paper_frame, text="The price of 1kg Paper is Rs8", font=font_style)
        self.description_palabel.grid(row=6,column=5)

        # E-waste Frame Content
        self.ewaste_label = tk.Label(self.ewaste_frame, text="E-WASTE", font=font_style)
        self.ewaste_label.grid(row=0, column=5, padx=5, pady=5)
        self.description_ewlabel = tk.Label(self.ewaste_frame, text="Depending upon the condition you will be awarded a reasonable Price", font=font_style)
        self.description_ewlabel.grid(row=6,column=5)


        # Unidentified Frame Content
        self.unidentified_label = tk.Label(self.unidentified_frame, text="UNIDENTIFIED", font=font_style)
        self.unidentified_label.grid(row=0, column=5, padx=5, pady=5)
        self.description_unlabel = tk.Label(self.unidentified_frame, text="Depending upon the scrap you will be awarded a reasonable Price", font=font_style)
        self.description_unlabel.grid(row=6,column=5)

    def load_image(self, path):
        self.image = Image.open(path)
        self.img_resizem = self.image.resize((350,200))
        self.img = ImageTk.PhotoImage(self.img_resizem)
        self.img_lbl = tk.Label(self.metal_frame, image=self.img)
        self.img_lbl.grid(row=5, column=5)

    def load_plimage(self, path1):
        self.image1 = Image.open(path1)
        self.img_resizepl = self.image1.resize((350,200))
        self.img1 = ImageTk.PhotoImage(self.img_resizepl)
        self.img_lbl1 = tk.Label(self.plastic_frame, image=self.img1)
        self.img_lbl1.grid(row=5, column=5)

    def load_paimage(self, path2):
        self.imagepa = Image.open(path2)
        self.img_resizepa = self.imagepa.resize((350,200))
        self.imgpa = ImageTk.PhotoImage(self.img_resizepa)
        self.img_lblpa = tk.Label(self.paper_frame, image=self.imgpa)
        self.img_lblpa.grid(row=5, column=5)
        
    def load_ewimage(self, path3):
        self.imageew = Image.open(path3)
        self.img_resize = self.imageew.resize((350,200))
        self.imgew = ImageTk.PhotoImage(self.img_resize)
        self.img_lblew = tk.Label(self.ewaste_frame, image=self.imgew)
        self.img_lblew.grid(row=5, column=5)

    def load_unimage(self, path4):
        self.imageun = Image.open(path4)
        self.img_resizeun = self.imageun.resize((350,200))
        self.imgun = ImageTk.PhotoImage(self.img_resizeun)
        self.img_lblun = tk.Label(self.unidentified_frame, image=self.imgun)
        self.img_lblun.grid(row=5, column=5)

    def redirect_to_servicepage(self):
        self.win.destroy()  # Destroy current window
        win = tk.Tk()        # Create a new Tkinter window
        app = servicepage.servicepage(win,image_path)  # Display the service page
        win.mainloop()

    def redirect_to_aboutUs(self):
        self.win.destroy()  # Destroy current window
        win = tk.Tk()        # Create a new Tkinter window
        app = aboutUs.aboutUs(win,image_path)  # Display the service page
        win.mainloop()



if __name__ == "__main__":
    image_path = r"C://Python//Scrap_Management//login_img.jpg"
    image_plpath = r"C://Python//Scrap_Management//login_img.jpg"
    image_papath = r"C://Python//Scrap_Management//login_img.jpg"
    image_ewpath = r"C://Python//Scrap_Management//login_img.jpg"
    image_unpath = r"C://Python//Scrap_Management//login_img.jpg"
    image_path2 = r"C://Python//Scrap_Management//download.jpg"
    win = tk.Tk()
    app = homepage(win, image_path)
    win.mainloop()


