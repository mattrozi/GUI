#You can use check boxes for for selecting toppings (each with a different cost), 
# radio buttons for the type of crust selected (each with a different cost), buttons for calculation and quit. 
# The input box can be used to record the name of the person placing the order. 
# Use a message box to display the total cost of the pizza along with the name of the person placing the order.


import tkinter
import tkinter.messagebox


class Pizza_order:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("600x200")
        self.main_window.title("Pizza Delivery")
        self.main_window.configure(bg='Red')

        self.name_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)


        self.prompt_label = tkinter.Label(
            self.name_frame, text="Enter a name for the order: "
        )

        self.Toppings_label=tkinter.Label(self.middle_frame,text='Toppings:')

        self.Crust_label=tkinter.Label(self.bottom_frame,text='Crust Options:')

        self.customer_entry = tkinter.Entry(self.name_frame, width=20)

        self.prompt_label.pack(side='left')
        self.customer_entry.pack(side='right')
        self.Toppings_label.pack(side='left')
        self.Crust_label.pack(side='left')

        # Create IntVar objects to use with check buttons

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.topping4_var=tkinter.IntVar()
        self.topping5_var=tkinter.IntVar()
        self.topping6_var=tkinter.IntVar()
        self.topping7_var=tkinter.IntVar()

        self.radio_var = tkinter.IntVar()


        # set
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.topping4_var.set(0)
        self.topping5_var.set(0)
        self.topping6_var.set(0)
        self.topping7_var.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.middle_frame, text="Bacon", variable=self.cb_var1
        )
        self.cb2 = tkinter.Checkbutton(
            self.middle_frame, text="Pepperoni", variable=self.cb_var2
        )
        self.cb3 = tkinter.Checkbutton(
            self.middle_frame, text="Sausage", variable=self.cb_var3
        )

        self.topping4 = tkinter.Checkbutton(
            self.middle_frame, text="Onion", variable=self.topping4_var
        )

        self.topping5 = tkinter.Checkbutton(
            self.middle_frame, text="Olives", variable=self.topping5_var
        )

        self.topping6 = tkinter.Checkbutton(
            self.middle_frame, text="Peppers", variable=self.topping6_var,
        )

        self.topping7 = tkinter.Checkbutton(
            self.middle_frame, text="Pineapple", variable=self.topping7_var
        )

        self.rb1 = tkinter.Radiobutton(
            self.bottom_frame, text="Regular Crust", variable=self.radio_var, value=5
        )

        self.rb2 = tkinter.Radiobutton(
            self.bottom_frame, text="Thick Crust", variable=self.radio_var, value=10
        )

        self.rb3 = tkinter.Radiobutton(
            self.bottom_frame, text="Detroit Style", variable=self.radio_var, value=15
        )


        
        
        self.cb1.pack(side='left')
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')
        self.topping4.pack(side='left')
        self.topping5.pack(side='left')
        self.topping6.pack(side='left')
        self.topping7.pack(side='left')

        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')



        self.Calculation_button = tkinter.Button(
            self.main_window, text="Calculate", command=self.do_something
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.name_frame.pack(side="top")
        self.middle_frame.pack(side='top')
        self.bottom_frame.pack(side="top")

        
        self.quit_button.pack(side="bottom")
        self.Calculation_button.pack(side="bottom")

        tkinter.mainloop()

    def do_something(self):
        self.message = "The Toppings you have selected: \n"

        if self.cb_var1.get() == 1:
            self.message+=' Bacon \n'

        if self.cb_var2.get() == 1:
            self.message+=' Pepporoni \n'

        if self.cb_var3.get() == 1:
            self.message+=' Sausage \n'

        if self.topping4_var.get() == 1:
            self.message+=' Onion \n'

        if self.topping5_var.get() == 1:
            self.message+=' Olives \n'

        if self.topping6_var.get() == 1:
            self.message+=' Peppers \n'

        if self.topping7_var.get() == 1:
           self.message+=' Pineapple \n'

        tkinter.messagebox.showinfo("Order Receipt", self.message)

    #def calculate_price(self):
       # self.total_price=


my_order = Pizza_order()


print("Moving on...")
