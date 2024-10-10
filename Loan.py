class LoanBorrow:

    def __init__(self, first_name, last_name, loan_amount):
        self.__loan_amount = self.__set_loan_amount(loan_amount)
        self.__name = first_name + ' ' + last_name
        self.__interest_rate = 0
        self.__loan_period = int
        self.__monthly_payment = 0.0



    def get_name(self):
        return self.__name

    def get_loan_amount(self):
        return self.__loan_amount

    def __set_loan_amount(self, loan_amount):
        if loan_amount < 2000 or loan_amount > 100_000:
            raise ValueError('Loan amount cannot be less than 2000 or greater than 100_000.')
        else:
            self.__loan_amount = loan_amount
            return self.__loan_amount


    def get_interest(self):
        self.__set_interest_rate()
        return self.__interest_rate

    def __set_interest_rate(self):
        loan_amount_greater_than_2k_and_less_than_11k = self.__loan_amount > 2000 and self.__loan_amount <= 10_000
        loan_amount_greater_than_11k_and_less_than_36k = self.__loan_amount > 11_000 and self.__loan_amount <= 35_000

        if loan_amount_greater_than_2k_and_less_than_11k:
            self.__interest_rate = 1
        elif  loan_amount_greater_than_11k_and_less_than_36k:
            self.__interest_rate = 3
        else:
            self.__interest_rate = 7


    def __set_loan_period(self):
        if self.__loan_amount > 2000 and self.__loan_amount <= 10000:
            self.__loan_period = 1
        elif self.__loan_amount > 10_000 and self.__loan_amount <= 35_000:
            self.__loan_period = 5
        else:
            self.__loan_period = 10

    def get_loan_period(self):
        self.__set_loan_period()
        return self.__loan_period

    def monthly_payment(self):
        upper =  self.__loan_amount  / (self.__interest_rate / 12)
        lower = 1-(1/(1+self.__interest_rate)*(self.__loan_period / 12))
        self.__monthly_payment = upper / lower
        return round(self.__monthly_payment, 2)



