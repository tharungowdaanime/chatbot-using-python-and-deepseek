
import tkinter as tk
from tkinter import messagebox
from chatbot import *
import webbrowser
import random as r



class TantrumApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Tantrum")
        self.root.geometry("1030x600")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        self.app_icon = tk.PhotoImage(file="images/icon.png")
        self.root.iconphoto(False, self.app_icon)
        self.Font =  ("Arial", 18, "bold") #("Garamond", 18, "bold")    
        self.Font2 = ("Palatino", 31) #("Arial", 28, "bold")


        self.user = tk.PhotoImage(file="images/user.png")
        self.ai = tk.PhotoImage(file="images/ai.png")

        self.goku = tk.PhotoImage(file="images/goku_image2.png")
        self.luffy = tk.PhotoImage(file="images/luffy2.png")

        self.naruto = tk.PhotoImage(file="images/naruto3.png")

        self.circle = tk.PhotoImage(file="images/circle.png")  

        self.me_img = tk.PhotoImage(file="images/me.png")

        self.thanks_img = tk.PhotoImage(file="images/thanks.png")




        self.text_feild = tk.PhotoImage(file="images/text2.png")



      
        self.bottom_frame = tk.Frame(
            self.root,
            width=1100,
            height=130,
            bg="#212120").pack(side=tk.BOTTOM)


        self.text_area = tk.Label(
            self.bottom_frame,
            image=self.text_feild,
            bg="#000000")
        self.text_area.place(x=70, y=480)




        self.send_btn_image = tk.PhotoImage(file="images/send.png")


        self.send_btn = tk.Button(
            self.bottom_frame,
            image=self.send_btn_image,
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            bg="#000000",
            highlightthickness=0,
            activebackground="#212120", 
            takefocus=False,
            command=self.send_message
        )
        self.send_btn.place(x=540, y=480)

        self.open_router_image = tk.PhotoImage(file="images/api.png")
        self.open_router_btn = tk.Button(
            self.bottom_frame,
            image=self.open_router_image,
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            bg="#212120",
            highlightthickness=0,
            activebackground="#000000",  
            takefocus=False,
            command=self.thanks_open_router
        )

        self.open_router_btn.place(x=720,y=480)

        random_anime = r.randint(1,3)

        if random_anime == 1:
            self.goku_btn = tk.Button(
            self.bottom_frame,
            image=self.goku,
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            bg="#212120",
            highlightthickness=0,
            activebackground="#000000",  
            takefocus=False,
            command=self.about_me
            )

            self.goku_btn.place(x=890,y=480)
        elif random_anime == 2:
            self.luffy_btn = tk.Button(
            self.bottom_frame,
            image=self.luffy,
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            bg="#212120",
            highlightthickness=0,
            activebackground="#000000",  
            takefocus=False,
            command=self.about_me
            )

            self.luffy_btn.place(x=890,y=480)
        else:
            self.naruto_btn = tk.Button(
            self.bottom_frame,
            image=self.naruto,
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            bg="#212120",
            highlightthickness=0,
            activebackground="#000000",  
            takefocus=False,
            command=self.about_me
            )

            self.naruto_btn.place(x=890,y=480)
    

        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(
            self.root,
            width=100,
            height=30,
            font=self.Font,
            relief="flat",
            bg="#F8F8FF",#ffffff",
            state="disabled",
            takefocus=0,
            yscrollcommand=self.scrollbar.set,
            selectbackground="#e8ff00",
            selectforeground="#000000"
            )
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.message = tk.Entry(
            self.bottom_frame,
            bg="#ffffff",
            font= self.Font2,
            takefocus = 1,
            width=17,
            borderwidth=0,        
            highlightthickness=0

        )

        self.message.place(x=85,y=510)
        self.message.focus()
        self.message.bind("<Return>",self.send_message)

    def send_message(self, event=None):

        user_message = self.message.get().strip()
        if user_message: 
            self.text.config(state="normal")

            self.text.insert(tk.END, "\n")

            self.text.image_create(tk.END, image=self.user)

        
            self.text.insert(tk.END, f" {user_message}\n")

            self.text.config(state="disabled") 
            self.text.yview(tk.END)
            self.message.delete(0, tk.END)  

            self.fetch_api_response(user_message)


    def fetch_api_response(self, user_message):
        try:
        
            ai_get_msg = TantrumBot(user_message)
            ai_response = ai_get_msg.response_ai()

        except Exception as e:
            messagebox.showinfo("Server Busy","The servers are busy, Please Try Again Later")
            ai_response = "I didn't quite understand that could you repeat?"

        self.display_bot_response(ai_response)

    def display_bot_response(self,ai_response):

        self.text.config(state="normal")
        self.text.insert(tk.END, "\n")
        self.text.image_create(tk.END, image=self.ai)
        self.text.insert(tk.END, " ")
        #self.text.insert(tk.END, f" {ai_response}\n")
        #self.text.config(state="disabled")
        wrapped_response = "\n".join(ai_response.splitlines())  
        self.text.insert(tk.END, wrapped_response + "\n")
        self.text.yview(tk.END)
        self.message.config(state="normal")
        self.message.focus()
        
    def thanks_open_router(self):
        webbrowser.open("https://openrouter.ai/deepseek/deepseek-r1:free")
    
    def about_me(self):


        window = tk.Toplevel()
        window.title("About Me")
        window.geometry("950x700")
        window.config(bg="#ffffff")
        window.iconphoto(False,self.app_icon)
        window.resizable(False, False)
        window.circle = tk.PhotoImage(file="images/circle.png")
        window.me_img = tk.PhotoImage(file="images/me.png")
        window.thanks_img = tk.PhotoImage(file="images/thanks.png")
       
        about_text = " Hi , i am I P Tharun Gowda i build this as a fun project. \
as i was bored and i recently saw a news about a new model called Deepseek\
and i also  saw a YouTube Video which showed about free api of Deepseek\
at OpenRouter website.\
So i thought to myself why not use this as i was simply sitting on home \
and i can also submit this a s my school project .\
So that's why i built this model\
and sorry about those anime buttons , i simply placed them as i like anime alot\
alot means alot"


        

        circle_label = tk.Label(window,image= window.circle,bg="white")
        circle_label.place(x=300, y=5)  # Adjust the position as needed

# "Me" Image (Below Circle)
        me_label = tk.Label(window, image=window.me_img, bg="white")
        me_label.place(x=0, y=120) 
        about_txt = tk.Label(
            window,
            text= about_text,
            font=("Arial", 14, "bold"),
            bg="white",
            fg="black",
            wraplength=900,  # Ensures text wraps properly
            justify="left",  # Aligns text in center
        )
        about_txt.place(x=0, y=250) 
    

        thanks_text2 = (
            "*I want to thank OpenRouter for the API\n\
*I want to thank Canva, which I used to build all graphics\n\
*I also want to thank those people who put Luffy, Goku, and Naruto's images.Sorry,I forgot the sites as these images were in my laptop for like 8 months\n\
*Lastly and leastly, Thank you Everyone!"
        )

        thanks_label = tk.Label(
            window,
            text=thanks_text2,
            font=("Arial", 14, "bold"),
            bg="white",
            fg="black",
            wraplength=900,  # Ensures text wraps properly
            justify="left",  # Aligns text in center
        )
        thanks_label.place(x=0, y=545) 

# "Thanks" Image (Below "Me")
        thanks_label2 = tk.Label(window, image=window.thanks_img, bg="white")
        thanks_label2.place(x=0, y=450)  # Adjust position accordingly

        window.mainloop()

        
if __name__ == "__main__":
    root = tk.Tk()
    app = TantrumApp(root)
    root.mainloop()
