"""
Mortgage loan calculation and simulation.
"""

from estate_project.domain.entities.mortgage import MortgageSimulationResult


# trunk-ignore(pylint/R0903)
class MortgageLoan:
    """
    A class to represent a mortgage loan.

    Attributes
    ----------
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

    def _calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment for the mortgage loan.

        Returns
        -------
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

    def _calculate_total_payment(self) -> float:
        """
        Calculate the total payment for the mortgage loan.

        Returns
        -------
            float: The total payment.
        """
        return round(self._calculate_monthly_payment() * self.loan_term * 12, 2)

    def simulate_loan(self, currency="€") -> MortgageSimulationResult:
        """
        Simulate the mortgage loan by calculating the monthly payment and the total payment.

        Returns
        -------
            MortgageSimulationResult:
            An object containing the loan amount,
            interest rate, loan term, monthly payment, and total payment.
        """
        return MortgageSimulationResult(
            loan_amount=str(self.loan_amount),
            interest_rate=str(self.interest_rate),
            loan_term=str(self.loan_term),
            monthly_payment=str(self._calculate_monthly_payment()),
            total_payment=str(self._calculate_total_payment()),
            currency=currency,
        )


# trunk-ignore(pylint/R0903)
class SimulateMortgageLoan:
    """
    A use case for simulating a mortgage loan.
    """

    @staticmethod
    # trunk-ignore(ruff/D417)
    def execute(
        loan_amount: float, interest_rate: float, loan_term: int, currency: str = "€"
    ) -> MortgageSimulationResult:
        """
        Execute the mortgage loan simulation use case.

        Args:
        ----
            loan_amount (float): The loan amount.
            interest_rate (float): The annual interest rate in percentage.
            loan_term (int): The loan term in years.
            currency (str): The currency.

        Returns:
        -------
            MortgageSimulationResult:
            An object containing the loan amount,
            interest rate, loan term, monthly payment, and total payment.
        """
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than 0.")
        if interest_rate <= 0:
            raise ValueError("Interest rate must be greater than 0.")
        if loan_term <= 0:
            raise ValueError("Loan term must be greater than 0.")
        mortgage = MortgageLoan(loan_amount, interest_rate, loan_term)
        return mortgage.simulate_loan(currency=currency)
