"""
Entities for all Mortgage Simulation
"""

from pydantic import BaseModel


class MortgageSimulationResult(BaseModel):
    """
    A class to represent the result of a mortgage loan simulation.

    Attributes:
        loan_amount (str): The loan amount.
        interest_rate (str): The annual interest rate in percentage.
        loan_term (str): The loan term in years.
        monthly_payment (str): The monthly payment.
        total_payment (str): The total payment.
        currency (str): unit of value
    """

    loan_amount: str
    interest_rate: str
    loan_term: str
    monthly_payment: str
    total_payment: str
    currency: str
