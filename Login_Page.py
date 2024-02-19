import tkinter as tk
from PIL import ImageTk, Image

image_path = "C://Python//Scrap_Management//login_img.jpg"

class Login_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page") 
        self.root.configure(bg="black")

        font_style = ("Helvetica", 15)

        # LEFT FRAME
        self.left_frame = tk.Frame(root, bg="black")
        self.left_frame.grid(row=0, column=0)

        # RIGHT FRAME 
        self.right_frame = tk.Frame(root, bg="black")
        self.right_frame.grid(row=0, column=1)

        # Load Image
        self.load_image(image_path)

        # RIGHT FRAME CONTENT
        self.heading_label = tk.Label(self.right_frame, text="LOGIN", bg="Orange", font=font_style)
        self.heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.email_label = tk.Label(self.right_frame, text="Email", bg="Orange", font=font_style)
        self.email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self.right_frame, font=font_style, borderwidth=4)
        self.email_entry.grid(row=1, column=1)

        self.password_label = tk.Label(self.right_frame, text="Password", bg="Orange", font=font_style)
        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.right_frame, font=font_style, borderwidth=4)
        self.password_entry.grid(row=2, column=1)

        self.login_btn = tk.Button(self.right_frame, text="Login", bg="Orange", width=20, font=font_style)
        self.login_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        font_style2 = ("impact", 12) 
        self.normal_label = tk.Label(self.right_frame, text="Don't have an account?", font=font_style2, foreground="white", bg="black")
        self.normal_label.grid(row=4, column=0, columnspan=2)

        self.normal_button = tk.Button(self.right_frame, text="Register", font=font_style2, foreground="white", bg="blue")
        self.normal_button.grid(row=5, column=0, columnspan=2)

    def load_image(self, path):
        self.image = Image.open(path)
        self.img = ImageTk.PhotoImage(self.image)
        self.img_lbl = tk.Label(self.left_frame, image=self.img)
        self.img_lbl.grid()

if __name__ == '__main__':
    root = tk.Tk()
    app = Login_Page(root)
    root.mainloop()
