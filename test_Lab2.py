import Lab2

def test_minmax_function():

    input = [1,2,3,4,5,6,7,8,9,10]
    result = Lab2.find_min_max(input)

    assert (result==1,10)
def test_avg_function():

    input = [2,4,6,8,10]
    result = Lab2.calc_average(input)

    assert (result == 6)

def test_median_function():

    input = [2,5,5,5,25,10]
    result = Lab2.calc_median_temperature(input)

    assert (result == 5)

