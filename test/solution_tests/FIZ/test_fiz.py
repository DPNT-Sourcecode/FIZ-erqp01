from solutions.FIZ import fizz_buzz_solution

class TestHlo2():
    def test_fiz(self):
        assert fizz_buzz_solution.fizz_buzz(3) == 'fizz'
        assert fizz_buzz_solution.fizz_buzz(12) == 'fizz'
        assert fizz_buzz_solution.fizz_buzz(10) == 'buzz'
        assert fizz_buzz_solution.fizz_buzz(15) == 'fizz buzz'
        assert fizz_buzz_solution.fizz_buzz(31) == 'fizz'
        assert fizz_buzz_solution.fizz_buzz(51) == 'fizz buzz'
        assert fizz_buzz_solution.fizz_buzz(53) == 'fizz buzz'
        assert fizz_buzz_solution.fizz_buzz(444) == 'deluxe'
        assert fizz_buzz_solution.fizz_buzz(55) == 'buzz deluxe'
        assert fizz_buzz_solution.fizz_buzz(55) == 'fizz deluxe'
        assert fizz_buzz_solution.fizz_buzz(8) == 8
        
        
        
        

