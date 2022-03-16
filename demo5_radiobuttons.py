import tkinter
import tkinter.messagebox


class KILO_Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("200x200")
        self.main_window.title("input Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        # Select default buttons
        # self.rb2.select()

        self.rb1 = tkinter.Radiobutton(
            self.top_frame, text="option1", variable=self.radio_var, value=10
        )

        self.rb2 = tkinter.Radiobutton(
            self.top_frame, text="option2", variable=self.radio_var, value=20
        )

        self.rb3 = tkinter.Radiobutton(
            self.top_frame, text="option3", variable=self.radio_var, value=30
        )

        self.rb2.select()

        # Packing the buttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.ok_button = tkinter.Button(
            self.bottom_frame, text="OK", command=self.show_choice
        )

        self.reset_button = tkinter.Button(
            self.bottom_frame, text="Reset", command=self.rb1.select
        )
        self.ok_button.pack(side="left")
        self.reset_button.pack(side="left")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo(
            "Selection", "You have selected Option " + str(self.radio_var.get())
        )


kilo_conv = KILO_Converter()


print("Moving on...")
