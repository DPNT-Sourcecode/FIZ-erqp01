from solutions.HLO2 import hello2_solution

class TestHlo2():
    def test_hlo2(self):
        assert hello2_solution.hello('Mike') == 'Hello, Mike!'

