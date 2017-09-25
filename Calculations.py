import datetime


class Calculation():

    def calc_days(self, b_day, b_month, b_year):

        self.days_of_months = {0: 0, 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        self.now = datetime.datetime.now()

        self.current_day = self.now.day
        self.current_month = self.now.month
        self.current_year = self.now.year

        self.visokosnie_years = 0
        for el in range(b_year, self.current_year+1):
            if el % 4 == 0:
                self.visokosnie_years = self.visokosnie_years + 1

        self.lived_years = self.current_year - b_year

        self.days_of_birth_year = 0
        for key, value in self.days_of_months.items():
            if key <= b_month - 1:
                self.days_of_birth_year = self.days_of_birth_year + value
        self.days_of_birth_year = 365 - (self.days_of_birth_year + b_day)

        self.days_of_leaved_full_years = 365 * (self.lived_years - 1)

        self.days_of_current_year = 0
        for key, value in self.days_of_months.items():
            if key <= self.current_month - 1:
                self.days_of_current_year = self.days_of_current_year + value
        self.days_of_current_year = self.days_of_current_year + self.current_day

    def check_correct_date(self, b_day, b_month, b_year):
        for year in range(b_year, self.current_year+1):
            if year % 4 == 0:
                for key in self.days_of_months.keys():
                    if key == 2:
                        self.days_of_months[key] = 29
                for key, value in self.days_of_months.items():
                    if key == b_month and b_day > value:
                        return False
            elif year % 4 != 0:
                for key, value in self.days_of_months.items():
                    if key == b_month and b_day > value:
                        return False
