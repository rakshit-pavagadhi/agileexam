import pytest
def calculate_fine(overdue_days):
    if overdue_days<0:
        raise ValueError("Overdue days cannot be negative")
    if overdue_days==0:
        return 0
    if overdue_days<=5:
        return overdue_days
    return 5+((overdue_days-5)*2)
@pytest.mark.parametrize(
    ("overdue_days", "expected_fine"),
    [
        (0, 0),   
        (3, 3),   
        (5, 5),   
        (6, 7),   
        (15, 25), 
    ],
)
def test_calculate_fine(overdue_days, expected_fine):
    assert calculate_fine(overdue_days)==expected_fine
@pytest.mark.parametrize("overdue_days", [-1, -10])
def test_calculate_fine_rejects_negative_days(overdue_days):
    with pytest.raises(ValueError, match="Overdue days cannot be negative"):
        calculate_fine(overdue_days)