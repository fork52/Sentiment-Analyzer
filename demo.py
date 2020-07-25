import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font

class GUI:
    '''Main class for GUI class'''
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

        self.sc = ScrolledText(
            master = self.root,
            font=self.hv16,bg='#c0effc',
            padx = 20 , pady=20
        )

        self.top_margin = 60
        self.left_margin = 50
        self.txt_width = 600
        self.txt_height = 200
        self.sc.place(   
            x = self.left_margin ,
            y = self.top_margin ,
            width= self.txt_width , height = self.txt_height
        )

    def add_buttons(self):
        '''Adds buttons to the GUI'''
        clearBtn = tk.Button(self.root , text = 'Clear',command = self.scrollText_command)      
        clearBtn.place(
                        x =  self.left_margin + self.txt_width-120 ,
                        y = self.top_margin + self.txt_height+20,
                        width = 100  , height = 50,
        )

        
        pass

    def submit_command(self):
        self.sentence = self.sc.get('1.0', tk.END)
        print(self.sentence)

    def scrollText_command(self):
        # Note that sc.get() returns a \n at the end of the string.
        self.sc.delete(1.0,tk.END)

if __name__ == "__main__":
    window = GUI()
    root = window.create_root()
    window.add_textbox()
    window.add_buttons()
    root.mainloop()