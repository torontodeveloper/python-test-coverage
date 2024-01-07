import pytest
import operations

    
@pytest.mark.skip
def test_calculate_square()->None:
    input = 2
    expected_result = input**2
    actual_result = operations.calculate_square(2)
    assert expected_result == actual_result

@pytest.mark.skip(reason='negative test case')
def test_calculate_square1()->None:
    input = -1
    expected_result = 0
    actual_result = operations.calculate_square(-1)
    assert expected_result==actual_result, 'given negative side, we default to 0'

@pytest.mark.skip(reason='negative test case')
def test_calculate_square2()->None:
    input = [2,4,10]
    expected_result = [4,16,100]
    
    for item,result in zip(input,expected_result):
        actual_result = operations.calculate_square(item)
        assert pytest.approx(actual_result) == result

@pytest.mark.skip(reason='negative test case')      
def test_calculate_area_circle()->None:
    '''
    calculate area of circle
    '''
    input = [2,4,10]
    expected_result = [12.5664,50.2655,314.159]
    
    for item, result in zip(input,expected_result):
        actual_result = operations.calcualte_area_circle(item)
        assert pytest.approx(actual_result,rel=1e-3) == result
@pytest.mark.skip(reason='negative test case')       
def test_calculate_area_circle1():
    with pytest.raises(ValueError):
        operations.calcualte_area_circle(-4)