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
        '''Add and configure the main textbox for input'''
        self.hv16 = Font(family="Helvetica", size=16)

        sc = ScrolledText(
            master = self.root,
            font=self.hv16,bg='#c0effc',
            padx = 20 , pady=20
        )

        self.top_margin = 60
        self.left_margin = 50
        self.txt_width = 600
        self.txt_height = 200
        sc.place(   
            x = self.left_margin ,
            y = self.top_margin ,
            width= self.txt_width , height = self.txt_height
        )


    def add_buttons(self):
        '''Adds buttons to the GUI'''
        pass

if __name__ == "__main__":
    window = GUI()
    root = window.create_root()
    window.add_textbox()
    root.mainloop()