import tkinter as tk

class GUI:
    def create_root(self):
        """Set up the window features for tkinter window"""
        root = tk.Tk()
        root.title('Review Sentiment Analyzer')
        root.geometry('700x630+350+50') # widthXheight topx+topy
        root.resizable(False, False)
        self.root = root
        return root
        # self.algo_choice = tk.IntVar(root,value=1)



if __name__ == "__main__":
    window = GUI()
    root = window.create_root()
    #Mainloop
    root.mainloop()