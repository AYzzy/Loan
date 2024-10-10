from Class_work.src.Loan import Loan
import unittest

from Loan.Loan import LoanBorrow


class TestLoan(unittest.TestCase):
    def setUp(self):
        self.loan = LoanBorrow("Oluwayemi", "Jacob", 10000.00)

    def test_that_loan_borrower_have_a_name(self):
        expected = "Oluwayemi Jacob"
        self.assertEqual(self.loan.get_name(), expected)

    def test_that_loan_borrower_have_a_loan_amount(self):
        expected = 10_000.00
        self.assertEqual(self.loan.get_loan_amount(), expected)

    def test_that_borrower_can_not_borrow_less_than_2k(self):
        self.assertRaises (ValueError, LoanBorrow, "Oluwayemi", "Jacob", 1000.00)

    def test_that_interest_rate_will_be_1_when_you_borrow2k_to_10k(self):
        self.assertEqual(1, self.loan.get_interest())

    def test_that_interest_rate_will_be_3_when_you_borrow_11k_to_35K(self):
        self.loan = LoanBorrow("Oluwayemi", "Jacob", 35000.00)
        self.assertEqual(3, self.loan.get_interest())

    def test_that_interest_will_increase_to_7_when_you_borrow_36k_100K(self):
        self.loan = LoanBorrow("Oluwayemi", "Jacob", 100000.00)
        self.assertEqual(7, self.loan.get_interest())


    def test_that_you_can_not_borrow_more_than_100k(self):
        self.assertRaises (ValueError, LoanBorrow, "Oluwayemi", "Jacob", 100001.00)


    def test_that_loan_days_will_not_be_greater_than_10_days_for_loan_between_2k_to_10k(self):
        self.assertEqual(10_000.0, self.loan.get_loan_amount())
        self.assertEqual(1, self.loan.get_loan_period())


    def test_that_loan_days_will_not_be_greater_than_21_days_for_loan_between_11k_to_35k(self):
        self.loan = LoanBorrow("Oluwayemi", "Jacob", 15_000.00)
        self.assertEqual(15_000.0, self.loan.get_loan_amount())
        self.assertEqual(5, self.loan.get_loan_period())

    def test_that_loan_days_will_not_be_greater_than_45_days_for_loan_between_36k_to100k(self):
        self.loan = LoanBorrow("Oluwayemi", "Jacob", 75_000.00)
        self.assertEqual(75_000.0, self.loan.get_loan_amount())
        self.assertEqual(10, self.loan.get_loan_period())

    def test_that_loan_of_10000_will_pay_834_every_month(self):
        self.assertEqual(self.loan.monthly_payment(), 833.33)
