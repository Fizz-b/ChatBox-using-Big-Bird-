from tkinter import *
#from bigbirdmodel import get_response, bot_name

BG_GRAY = "#2986cc"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 16"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Covid-19 question answering")
        self.window.resizable(width=False, height=True)
        self.window.configure(width=470, height=300, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg="#6fa8dc", fg="#ffffff",
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.02)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg="white", fg="black",
                                font=FONT, padx=5, pady=5)
        #self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.place(relheight=0.3, relwidth=1, rely=0.1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=0.45, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.3)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#ffffff", fg="#000000", font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.07, rely=0.004, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg="#6fa8dc",
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
       # msg2 = f"{bot_name}: {get_response(msg)}\n\n"   # ham tra ve output = function get_response tu chat.py
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)
             
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()