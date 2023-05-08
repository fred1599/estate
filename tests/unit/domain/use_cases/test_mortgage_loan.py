from decimal import Decimal

import pytest

from estate_project.domain.entities.mortgage import MortgageSimulationResult
from estate_project.domain.use_cases.mortgage_calculation import \
    SimulateMortgageLoan


@pytest.fixture
def simulate_mortgage_loan() -> SimulateMortgageLoan:
    return SimulateMortgageLoan()


def test_simulate_mortgage_loan(simulate_mortgage_loan) -> None:
    loan_amount = Decimal(300000)
    interest_rate = Decimal(3.5)
    loan_term = 25

    result: MortgageSimulationResult = simulate_mortgage_loan.execute(
        loan_amount, interest_rate, loan_term
    )

    assert isinstance(result, MortgageSimulationResult)
    assert result.monthly_payment == "1501.87"
    assert result.interest_rate == "3.5"
    assert result.total_payment == "450561.00"


def test_simulate_mortgage_loan_invalid_input(simulate_mortgage_loan) -> None:
    with pytest.raises(ValueError):
        simulate_mortgage_loan.execute(-300000, 3.5, 25)

    with pytest.raises(ValueError):
        simulate_mortgage_loan.execute(300000, -3.5, 25)

    with pytest.raises(ValueError):
        simulate_mortgage_loan.execute(300000, 3.5, -25)
