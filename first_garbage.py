import tkinter as tk
import subprocess
import os
from pathlib import Path



class Ezbutton():
    # def __init__(self, ):
    root = tk.Tk()
    root.title('森林判識小工具')
    root.geometry('400x200')


        # button.config(width=w, height=h)
    def gen_button(self, ):

        mybutton1 = tk.Button(self.root, text='圖片前處理')
        mybutton1.configure(command=lambda:self.preprosossing())
        mybutton2 = tk.Button(self.root, text='AI判斷')
        mybutton2.configure(command=lambda:self.predict())
        mybutton3 = tk.Button(self.root, text='產出shp')
        mybutton3.configure(command=lambda:self.gen_shp())
        mybutton1.place(relx = 0.4, rely = 0.3)
        mybutton2.place(relx = 0.4, rely = 0.5)
        mybutton3.place(relx = 0.4, rely = 0.7)


    def preprosossing(self, ):
        fp = Path.cwd() / Path("split.exe pause")
        os.startfile(fp)
        # rs = subprocess.call(['split.exe'])
        # get 0 when done
    def predict(self, ):
        # rs = subprocess.call(['model.bat'])
        fp = Path.cwd() / Path("model.bat")
        os.startfile(fp)
    def gen_shp(self, ):
        # rs = subprocess.call(['combine.exe'])
        fp = Path.cwd() / Path("combine.exe")
        os.startfile(fp)
    def run(self, ):
        self.gen_button()
        self.root.mainloop()

if __name__=='__main__':
    ezbt = Ezbutton()
    ezbt.run()
