import tkinter


class GradesGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("300x600")
        self.main_window.title("Grades")

        self.Frame1 = tkinter.Frame(self.main_window)
        self.Frame2 = tkinter.Frame(self.main_window)
        self.Frame3 = tkinter.Frame(self.main_window)
        self.Frame4 = tkinter.Frame(self.main_window)
        self.Frame5 = tkinter.Frame(self.main_window)

        self.test1prompt = tkinter.Label(
            self.main_window, text=" Enter the score for Test 1: "
        )
        self.test1Entry = tkinter.Entry(self.Frame1, width=10)
        self.test2prompt = tkinter.Label(
            self.main_window, text=" Enter the score for Test 2:"
        )
        self.test2Entry = tkinter.Entry(self.Frame2, width=10)
        self.test3prompt = tkinter.Label(
            self.main_window, text=" Enter the score for Test 3:"
        )
        self.test3Entry = tkinter.Entry(self.Frame3, width=10)

        self.AverageLabel = tkinter.Label(self.Frame4, "Average")
        self.AverageAnswerLabel = tkinter.Label(self.Frame4, text="Average:")

        ##self.AverageButton=tkinter.Button(self.Frame5,text='Average',command=self.get_average)
        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.test1prompt.pack(side="top")
        self.test2prompt.pack(side="top")
        self.test3prompt.pack(side="top")
        self.AverageLabel.pack(side="top")
        self.AverageAnswerLabel.pack(side="top")
        self.quit_button.pack(side="right")

        self.frame1.pack(side="top")
        self.frame2.pack(side="top")
        self.frame3.pack(side="top")
        self.frame4.pack(side="top")
        self.frame5.pack(side="top")

        tkinter.mainloop()


mygrades = GradesGUI()

# def get_average(self):
