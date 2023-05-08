"""
Mortgage loan calculation and simulation
"""

from typing import Dict


class MortgageLoan:
    """
    A class to represent a mortgage loan.

    Attributes:
        loan_amount (float): The loan amount.
        interest_rate (float): The annual interest rate in percentage.
        loan_term (int): The loan term in years.
    """

    def __init__(
        self, loan_amount: float, interest_rate: float, loan_term: int
    ) -> None:
        self.loan_amount: float = loan_amount
        self.interest_rate: float = interest_rate
        self.loan_term: int = loan_term

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment for the mortgage loan.

        Returns:
            float: The monthly payment.
        """
        monthly_interest_rate: float = self.interest_rate / 12 / 100
        num_payments: int = self.loan_term * 12
        monthly_payment: float = (
            self.loan_amount
            * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments)
            / ((1 + monthly_interest_rate) ** num_payments - 1)
        )
        return round(monthly_payment, 2)

    def calculate_total_payment(self) -> float:
        """
        Calculate the total payment for the mortgage loan.

        Returns:
            float: The total payment.
        """
        return round(self.calculate_monthly_payment() * self.loan_term * 12, 2)

    def simulate_loan(self) -> Dict[str, float]:
        """
        Simulate the mortgage loan by calculating the monthly payment and the total payment.

        Returns:
            dict: A dictionary with the loan amount, interest rate, loan term, monthly payment, and total payment.
        """
        return {
            "loan_amount": self.loan_amount,
            "interest_rate": self.interest_rate,
            "loan_term": self.loan_term,
            "monthly_payment": self.calculate_monthly_payment(),
            "total_payment": self.calculate_total_payment(),
        }
