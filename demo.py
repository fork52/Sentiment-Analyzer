import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font
from PIL import Image,ImageTk
from model_utils import FullyConnected_NN,GRU

class GUI:
    '''Main class for GUI class'''
    def __init__(self):
        self.model_mapper = {
            1: FullyConnected_NN,
            2: 'RNN',
            3: GRU
        }

        self.models = {
            FullyConnected_NN : False,
            'RNN' : False,
            GRU : False
        }
        pass

    def create_root(self):
        """Set up the window features for tkinter window"""
        root = tk.Tk()
        root.title('Review Sentiment Analyzer')
        root.geometry('700x550+350+50') # widthXheight topx+topy
        root.resizable(False, False)
        root.configure(background='black')
        self.root = root
        self.model_choice = tk.IntVar(root,value=1)
        return root
    
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

        submitBtn = tk.Button(self.root , text = 'Submit',command = self.submit_command)      
        submitBtn.place(
                        x =  self.left_margin + self.txt_width-260 ,
                        y = self.top_margin + self.txt_height+20,
                        width = 100  , height = 50,
        )
        
    def add_radio_buttons(self):
        #Create label for the algorithms

        self.verdana16 = Font(self.root ,family = 'Verdana',size=14)
        model_label = tk.Label(
            self.root, text = 'Choose Model :-',
            padx = 20 , pady = 8,font = self.verdana16
        )
        self.radio_label = (self.left_margin + 30,self.top_margin + self.txt_height+20 )
        model_label.place(
                x = self.radio_label[0] ,
                y = self.radio_label[1]  
        )

        #Option one
        FullyConnected = tk.Radiobutton( self.root, 
                  text= 'FullyConnected NN',
                  variable=self.model_choice, 
                  value = 1 ,
                  width = 20,padx=5,pady=3,
                  justify='left'

                  )
        FullyConnected.place(x = self.radio_label[0], y=self.radio_label[1]+ 60)

        #Option two
        RNN = tk.Radiobutton( self.root, 
            text= 'Recurrent Neural Network',
            variable=self.model_choice, 
            value = 2,
            width = 20,padx=5,pady=3,
            justify='left'
            )
        RNN.place(x = self.radio_label[0], y=self.radio_label[1]+ 100)

        #Option three
        LSTM = tk.Radiobutton( self.root, 
            text= 'LSTM network',
            variable=self.model_choice, 
            value = 3,
            width = 20,padx=5,pady=3,
            justify='left'
            )
        LSTM.place(x = self.radio_label[0], y=self.radio_label[1]+ 140)

    def submit_command(self):
        self.sentence = self.sc.get('1.0', tk.END)[:-1]
        self.add_rating_image(self.sentence)

    def scrollText_command(self):
        # Note that sc.get() returns a \n at the end of the string.
        self.sc.delete(1.0,tk.END)

    def add_rating_image(self,sentence):
        #Load the model class's 
        model_type = self.model_mapper[self.model_choice.get()]
        
        model_obj = self.models.get(model_type,False)
        if not model_obj:
            model_obj = self.models[model_type] =  model_type()
    
        # print(model_obj.model.summary())
        current_rating = model_obj.get_rating(self.sentence)

        #Adding Label for rating
        self.verdana1 = Font(self.root ,family = 'Verdana',size=14)
        self.rating_label = tk.Label(
            self.root, text = 'Rating Prediction:',
            padx = 40 , pady = 8,font = self.verdana16
        )
        self.rating_label.place(
            x=self.left_margin+self.txt_width-280,
            y = self.top_margin + self.txt_height + 100
        )

        # Adding image to model
        img_name = f'images/{current_rating}star.jpg'
        img = Image.open(img_name)
        img  = img.resize( (200,40) ,Image.ANTIALIAS)
        rating_img  = ImageTk.PhotoImage(img)
        img_label = tk.Label(self.root, image=rating_img)
        img_label.image = rating_img
        img_label.place(
            x=self.left_margin+self.txt_width-250,
            y = self.top_margin + self.txt_height + 160
        )

    

if __name__ == "__main__":
    window = GUI()
    root = window.create_root()
    window.add_textbox()
    window.add_buttons()
    window.add_radio_buttons()
    # window.add_rating_image()
    root.mainloop()