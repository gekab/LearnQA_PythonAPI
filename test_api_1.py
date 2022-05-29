import requests


class TestFirstAPI:
    def test_hello_call(self):
        # input values
        url = "https://playground.learnqa.ru/api/hello"
        name = 'Evgeny'
        data = {'name': name}

        # STR:
        # step #1
        response = requests.get(url, params=data)
        # expected result
        assert response.status_code == 200, "Wrong response code"

        # step #2
        response_dict = response.json()
        # expected result
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        # step #3
        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        # expected result
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"
