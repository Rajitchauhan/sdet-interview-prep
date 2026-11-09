
import pytest 

@pytest.mark.parametrize( "a , b , res" , [(2 , 2 , 4) , (2 , 0 , 2) , (2 , -1 , 1) , (0 , 0 , 0)])
def test_add(calc):
    assert calc.add(a , b) == res


@pytest.mark.smoke
def test_divide(calc):
    with pytest(ValueError) as exc:
        calc.divide(2 , 0)

    assert "can not divide by zero" in str(exc.value)
