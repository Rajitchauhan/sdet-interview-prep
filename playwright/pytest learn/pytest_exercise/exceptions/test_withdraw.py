import withdraw
import pytest


def test_withdraw():
    wt = withdraw.withdraw(100 , 40)

    # print(wt)
    assert wt == 60 

def test_withdraw2():
    with pytest.raises(RuntimeError , match="Insufficient balance"):
        withdraw.withdraw(100 , 150)


def test_withdraw3():
    with pytest.raises(ValueError) as exc:
        withdraw.withdraw(100 , 0)

    assert "Amount must be greater than zero" in str(exc.value)




