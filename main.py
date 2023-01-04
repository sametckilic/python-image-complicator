import tkinter
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os
import logging

from tkinter import filedialog

class IMG_Stegno:
    output_image_size = 0

    def main(self, root):
            root.title('Python Image Complicator')
            root.resizable(width=False, height=False)
            frame = Frame(root)
            frame.config(pady=150)
            frame.grid(row=0,column=2,sticky="nsew")

            title = Label(frame, text='Image Complicator')
            title.config(font=('Arial', 25, 'bold'))
            title.grid(pady=20)
            title.grid(row=0,column=1)

            encode = Button(frame, text="Crypter", command=lambda: self.encode_frame1(frame), padx=20,pady=20,)
            encode.config(font=('Arial', 14, 'italic'),padx=50)
            encode.grid(row=1,column=0)
            decode = Button(frame, text="Decrypter", command=lambda: self.decode_frame1(frame), padx=20,pady=20,)
            decode.config(font=('Arial', 14, 'italic'), padx=50)
            decode.grid(row=1,column=2)



            root.grid_rowconfigure(1, weight=1)
            root.grid_rowconfigure(2, weight=0)

    def back(self, frame):
            frame.destroy()
            self.main(root)

            
    def encode_frame1(self, F):
            F.destroy()
            F2 = Frame(root)
            F2.config(pady=150,padx=0)
            label1 = Label(F2, text='     Choose image you want to complicate     \n\n    Choose image:     \n\n')
            label1.config(font=('Arial', 25, 'bold'))
            label1.grid()

            button_bws = Button(F2, text='Choose Image', command=lambda: self.encode_frame2(F2))
            button_bws.config(font=('Arial', 18))
            button_bws.grid()
            button_back = Button(F2, text='Cancel', command=lambda: IMG_Stegno.back(self, F2))
            button_back.config(font=('Arial', 18))
            button_back.grid(pady=15)
            button_back.grid()
            F2.grid()

    def encode_frame2(self, e_F2):
            e_pg = Frame(root)
            myfile = tkinter.filedialog.askopenfilename(
                filetypes=([ ('jpg', '*.jpg'), ('jpeg', '*.jpeg'),('png', '*.png') , ('All Files', '*.*')]))
            if not myfile:
                messagebox.showerror("Error", "You didn't selecet anything!")
            else:
                my_img = Image.open(myfile)
                new_image = my_img.resize((300, 200))
                img = ImageTk.PhotoImage(new_image)
                label3 = Label(e_pg, text='Selected image')
                label3.config(font=('Arial', 14, 'bold'))
                label3.grid()
                board = Label(e_pg, image=img)
                board.image = img
                self.output_image_size = os.stat(myfile)
                self.o_image_w, self.o_image_h = my_img.size
                board.grid()
                encode_button = Button(e_pg, text='İptal', command=lambda: IMG_Stegno.back(self, e_pg))
                encode_button.config(font=('Arial', 14))
                button_back = Button(e_pg, text='Complicate',command=lambda: [self.enc_fun(my_img), IMG_Stegno.back(self, e_pg)])
                button_back.config(font=('Arial', 14))
                button_back.grid(pady=15)
                encode_button.grid()
                e_pg.grid(row=1)
                e_F2.destroy()

    def enc_fun(self, input_image):
        pixel_map = input_image.load()

        width, height = input_image.size


        for x in range(0, width):
            for y in range(0, height):
                r,g,b = input_image.getpixel((x,y))
                red = ((x*y)%256 + r)%256
                green= ((x*y)%256 + g)%256
                blue = ((x*y)%256 + b)%256
                pixel_map[x,y] = (red,green,blue)
        messagebox.showinfo("Complicated", "Image complication is done\n")
        input_image.show()
        newImg = input_image.copy()
        my_file = BytesIO()
        temp = os.path.splitext(os.path.basename(input_image.filename))[0]
        newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=([('png', '*.png')]),defaultextension=".png"))
        self.d_image_size = my_file.tell()
        self.d_image_w, self.d_image_h = newImg.size

    def decode_frame1(self, F):
            F.destroy()
            F2 = Frame(root)
            F2.config(pady=150,padx=0)
            label1 = Label(F2, text='     Choose image you want to decomplicate     \n\n    Choose image:     \n\n')
            label1.config(font=('Arial', 25, 'bold'))
            label1.grid()

            button_bws = Button(F2, text='Choose Image', command=lambda: self.decode_frame2(F2))
            button_bws.config(font=('Arial', 18))
            button_bws.grid()
            button_back = Button(F2, text='Cancel', command=lambda: IMG_Stegno.back(self, F2))
            button_back.config(font=('Arial', 18))
            button_back.grid(pady=15)
            button_back.grid()
            F2.grid()

    def decode_frame2(self, e_F2):
            e_pg = Frame(root)
            myfile = tkinter.filedialog.askopenfilename(
                filetypes=([ ('png', '*.png') ,('jpg', '*.jpg'), ('jpeg', '*.jpeg'), ('All Files', '*.*')]))
            if not myfile:
                messagebox.showerror("Error", "You didn't selecet anything!")
            else:
                my_img = Image.open(myfile)
                new_image = my_img.resize((300, 200))
                img = ImageTk.PhotoImage(new_image)
                label3 = Label(e_pg, text='Selected image')
                label3.config(font=('Arial', 14, 'bold'))
                label3.grid()
                board = Label(e_pg, image=img)
                board.image = img
                self.output_image_size = os.stat(myfile)
                self.o_image_w, self.o_image_h = my_img.size
                board.grid()
                encode_button = Button(e_pg, text='Cancel', command=lambda: IMG_Stegno.back(self, e_pg))
                encode_button.config(font=('Arial', 14))
                button_back = Button(e_pg, text='Decomplicate',command=lambda: [self.dec_fun(my_img), IMG_Stegno.back(self, e_pg)])
                button_back.config(font=('Arial', 14))
                button_back.grid(pady=15)
                encode_button.grid()
                e_pg.grid(row=1)
                e_F2.destroy()      

    def dec_fun(self, input_image):
        pixel_map = input_image.load()

        width, height = input_image.size


        for x in range(0, width):
            for y in range(0, height):
                r,g,b = input_image.getpixel((x,y))
                red = r - (x*y)%256 if r - (x*y)%256 >= 0 else r - (x*y)%256 + 256
                green = g - (x*y)%256 if g - (x*y)%256 >= 0 else g - (x*y)%256 + 256
                blue = b - (x*y)%256 if b - (x*y)%256 >= 0 else b - (x*y)%256 + 256
                pixel_map[x,y] = (red,green,blue)
        messagebox.showinfo("Decomplicated", "Image decomplication is done\n")
        input_image.show()
        newImg = input_image.copy()
        my_file = BytesIO()
        temp = os.path.splitext(os.path.basename(input_image.filename))[0]
        newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=([('png', '*.png')]),defaultextension=".png"))
        self.d_image_size = my_file.tell()
        self.d_image_w, self.d_image_h = newImg.size


root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()
