import pytest 


@pytest.mark.smoke
@pytest.mark.regression
def test_smoke():
    assert True

# @pytest.mark.regression
# def test_regression():
#     assert True

@pytest.mark.smoke
@pytest.mark.regression
def test_checkout_order():
    assert True

@pytest.mark.regression
def test_filter_by_color():
    assert True 



# pytest -m smoke -v
# pytest -m regression -v
# pytest -m "regression not smoke" -v 
    