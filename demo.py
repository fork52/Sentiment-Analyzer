import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font

class GUI:
    def create_root(self):
        """Set up the window features for tkinter window"""
        root = tk.Tk()
        root.title('Review Sentiment Analyzer')
        root.geometry('700x630+350+50') # widthXheight topx+topy
        root.resizable(False, False)
        root.configure(background='black')
        self.root = root
        return root
        # self.algo_choice = tk.IntVar(root,value=1)
    
    def add_textbox(self):
        self.hv16 = Font(family="Helvetica", size=16)
        sc = ScrolledText(root,font=self.hv16,bg='#c0effc')
        sc.place(   
             x = 50 ,y = 60 ,
            width=600 , height = 200
        )




if __name__ == "__main__":
    window = GUI()
    root = window.create_root()
    window.add_textbox()
    root.mainloop()