# fortvision task
Before running the test, you must enter your test data in the file [user_data.py](https://github.com/lambotik/forvision1/blob/main/data/user_data.py):

email = your_email

password = your password

After this, you can run txts in github actions or on your computer using the following commands:

1. ```git clone https://github.com/lambotik/forvision1.git```
2. ```cd forvision1```
3. ```pip3 install -r requirements.txt```
4. ```pytest -s -v --alluredir=test_result/ tests/```
5. ```allure serve test_result```

