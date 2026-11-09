import pytest 
# from practice_1.wallet import Wallet
import wallet 

@pytest.fixture
def empty_wallet():
    return wallet.Wallet()

def test_default_initial_amount(empty_wallet):
    assert (
        empty_wallet.balance == 0
    ), "Expected initial wallet balance to be 0" 

@pytest.fixture 
def wallet_with_50():
    return wallet.Wallet(50)

def test_wallet_add_cash(wallet_with_50):
    wallet_with_50.add_cash(30)
    assert (wallet_with_50.balance == 80 
            ) ,"result will be 80"

@pytest.mark.parametrize(
    "earned, spent, expected", [(50, 10, 40), (100, 50, 50), (20, 20, 0)]
)
def test_wallet_transactions(earned, spent, expected):
    wt = wallet.Wallet(earned)
    wt.spend_cash(spent)
    assert ( wt.balance == expected) , f"must be {expected}"

def test_wallet_insufficient_spend(wallet_with_50):

    with pytest.raises(RuntimeError) as exc:
        wallet_with_50.spend_cash(100)
    assert "Insufficient balance" in str(exc.value)