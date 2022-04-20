import pytest
from app.services.thingy.thingy import Thingy


@pytest.mark.parametrize(
    "arg1,expected",
    [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
    ]
)
def test_example(arg1, expected):
    # arrange
    test_obj = Thingy(arg1)
    # act
    actual = test_obj.run_a_thing()
    # assert
    assert actual == expected
