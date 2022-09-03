import pytest
from functions import rating,point_calc,user_checker

def test_point_calc():
    assert point_calc([".",".","."]) == 3
    with pytest.raises(TypeError):
        point_calc("cat")
    assert point_calc(["1","2","3","4","5"]) == 5
