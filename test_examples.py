class TestExamle:
    def test_check_math(self):
        a = 2
        b = 4
        expected_sum = a + b
        assert a + b == expected_sum, f"Sum of variables a and b is not equal to {expected_sum}"

    def test_check_math2(self):
        a = 2
        b = 4
        expected_sum = 13
        assert a + b == expected_sum, f"Sum of variables a and b is not equal to {expected_sum}"
