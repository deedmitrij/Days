from tkinter import *
import tkinter.ttk as ttk
from data.years_list import years
from data.days_list import days
from data.months_list import months
from Calculations import Calculation


class UI():

    calculation = Calculation()

    def run_main_window(self):

        self.root=Tk()
        self.root.title('Days')
        self.root.geometry('245x150')
        self.root.resizable(False, False)

        self.header_lable = Label(self.root, text="Введите дату рождения:")
        self.header_lable.grid(column=1, row=0, columnspan=2, ipadx=5, ipady=5, sticky=W)

        self.day_label = Label(self.root, text="день")
        self.day_label.grid(column=1, row=1, sticky=E)

        self.month_label = Label(self.root, text="месяц")
        self.month_label.grid(column=1, row=2, sticky=E)

        self.year_label = Label(self.root, text="год")
        self.year_label.grid(column=1, row=3, sticky=E)

        self.calculate_days_button = Button(self.root, text="Calc", command=self.click_calc_button)
        self.calculate_days_button.grid(column=3, row=1, columnspan=2, rowspan=3, ipadx=15, ipady=18, sticky=E)

        self.footer_lable = Label(self.root, text="Количество прожитых дней:")
        self.footer_lable.grid(column=1, row=4, columnspan=2, ipadx=5, ipady=5, sticky=W)

        self.err = StringVar()
        self.error_lable = Label(self.root, textvariable=self.err, fg='red')
        self.error_lable.grid(column=1, columnspan=2, row=5, sticky=NE)

        self.birth_day = StringVar()
        self.day_entry = ttk.Combobox(self.root, textvariable=self.birth_day, values=days, state='readonly', height=6,
                                      width=5)
        self.day_entry.current(0)
        self.day_entry.grid(column=2, row=1, padx=8, sticky=W)

        self.birth_month = StringVar()
        self.month_entry = ttk.Combobox(self.root, textvariable=self.birth_month, values=months, state='readonly',
                                        height=6, width=5)
        self.month_entry.current(0)
        self.month_entry.grid(column=2, row=2, padx=8, sticky=W)

        self.birth_year = StringVar()
        self.year_entry = ttk.Combobox(self.root, textvariable=self.birth_year, values=years, state='readonly',
                                       height=10, width=5)
        self.year_entry.current(0)
        self.year_entry.grid(column=2, row=3, padx=8, sticky=W)

        self.all_lived_days = IntVar()
        self.result_label = Label(self.root, textvariable=self.all_lived_days)
        self.result_label.grid(column=3, row=4, sticky=W)
        #calculate_days_button.bind("<<ComboboxSelected>>", calc)

        self.root.mainloop()

    def click_calc_button(self):
        self.b_day = int(self.birth_day.get())
        self.b_month = int(self.birth_month.get())
        self.b_year = int(self.birth_year.get())
        self.calculation.calc_days(self.b_day, self.b_month, self.b_year)
        if self.calculation.check_correct_date(self.b_day, self.b_month, self.b_year) == False:
            self.all_lived_days.set('0')
            self.err.set('Введите корректную дату')
        else:
            self.all_lived_days.set(self.calculation.days_of_birth_year + self.calculation.days_of_leaved_full_years + self.calculation.days_of_current_year + self.calculation.visokosnie_years)
            self.err.set('')