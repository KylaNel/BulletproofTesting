# Bulletproof Testing in Python
This is a workshop on testing and mocking in Python. 


## Set Up
To do this workshop, you will need to have installed Python, git, pip, and Coverage on your machine.

### Python
To check if you already have Python, run 
```
python --version
```
or
```
python3 --version
```
in the command line.

If you do not have Python on your machine, download it from [the official website](https://python.org/downloads/).

### Git
To check if you already have git, run 
```
git version
```
in the command line.

If you do not have git on your machine, install it following [the official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).


### Pip
To check if you already have pip, run 
```
pip --version
```
or
```
pip3 --version
```
in the command line.

If you do not have pip on your machine,  install it following [the official guide](https://pip.pypa.io/en/stable/installation/).



### Coverage
To check if you already have Coverage, run 
```
coverage --version 
```
in the command line.

If you do not have Coverage on your machine, install it by entering
```
pip install coverage
```
or
```
pip3 install coverage
```
in the command line.


## Getting Started
First, clone this repo

```
git clone https://github.com/beedel/bulletproof-testing.git
cd bulletproof-testing
```

Try running the application by entering `python3 main.py Ford` in the command line. Does it work?
You should see 
```angular2html
Ford Fiesta
Ford Mustang
Ford Focus
```
printed on the command line.

## Get to Know the Code
Have a look at the `src` directory. You will see three files - `CarApiClient.py`, `CarRepository.py`, and `CarResolver.py`.
All the files have a comment explaining their purpose. Try to understand what their code does to ensure you can write test cases for it.

Can you think of any happy/failure test cases for these files? What are the possible flows of the application? Do any of the classes ever throw an exception?

If you want to, you can also have a look at the `main.py` file. It sets up the database and runs the application.

## Running the Tests
Run a test with `python3 -m unittest test/<Filename>.py`

When you are done writing all of the tests, you can run all of them with `python3 -m unittest`, if it does not work you can try running `python3 -m unittest tests/test_*.py`.

## Get to Testing
Let's write some tests for this application.


### test_car_api_client.py
Start with the `test_car_api_client.py` file in the `tests/` folder. The comment above the class name includes guidance on what is already there and what is missing. Can you finish writing the test code for this class?

### test_car_resolver.py
Now look at the `test_car_resolver.py` file in the `tests/` folder. The comment above the class name includes guidance on what is already there and what is missing. Can you finish writing the test code for this class?

### Whoops!
You wrote all these test cases and thought you had it all. Think again!

In the `test_car_resolver.py` file you mocked out the database. This is good, because it makes your tests faster and ensures that you can control the values it returns.

But what if somebody changed the code for `CarRepository.py` and broke it?

Imagine an intern comes in, sees the line 
```
cursor.execute("SELECT * FROM cars WHERE brand=?", (manufacturer,))
```
and decides to follow proper naming conventions and change `brand` to `manufacturer`. After all, consistency is key!

Try changing it and running the application again. Does it break?

Now run the `test_car_resolver.py` file. All good?

We need to fix this. 

### CarResolverSmokeTest.py
Look at the `test_car_resolver_smoke_test.py` file in the `tests/` folder. The comment above the class name includes guidance on what is already there and what is missing. Can you finish writing the test code for this class?

## Motorbikes

Now you will do exercises related to Motorbikes. Look at MotorBikeConnector.py.
MotorBikeConnector is a class that connects to the internet and checks if a MotorBike exists and can retrieve its price.
Assume that anything in folder Internet is a pre-written 3rd party library that is well tested and cannot be modified. Assume that the post method for frequests works the same way as the post method for the python library requests.
Your task is to finish the error handling by adding an if statement to the code in MotorBikeConnector at the relevant place based on the task description below.
Then, you will need to complete the test cases to achieve a 100% line coverage for this class.
Some of the test cases have been written for you.

Before writing any tests please do the following:
1. Uncomment lines 29-31 in main.py. (you may comment out the rest of the lines in that method)
2. Run the code and observe what happens.
3. Change the url in MotorBikeConnector from bikernet to something else e.g.: google.com/... , see what happens and change it back to bikernet
4. Now change the subdirectory for either of the urls to something random and see what happens (e.g.: change /getPriceForBike to /getPriceForApple). Then set it back to what it was.

Now you can proceed and fill in the test cases in ```test_motorbike_connector.py``` .
In this exercise you will mainly be using @patch()
There's one there as an example to show you how to use @patch() (```test_check_if_bike_exists_returns_404()```). You still need to finish the assertion though.

Below is some help for using patch and mocks:
use patch to override call of frequests

   To patch you can use decorator @patch("path.to.what.you.want.to.mock") then pass in the mock into the testcase
   you can set the return value of a mock that you created using patching by setting its return_value property.
   
E.g.: for mock_function.return_value = True when mock_function is called it returns True
   
For dictionaries you might do something like 
```  python
   mock_function.return_value.key_one = True
   mock_function.return_value.key_two = False
   ```
It will return dictionary {key_one: True, key_two:False}

First test the happy scenario: if 200 response is returned by your mock check if return value is either true or false
   
Then test the non-200 response mock you made: see if it raises an Exception and returns None 
   
Then test the case where an Exception is being thrown by your mock: see if it raises and Exception and returns None
   
   As all the exceptions are handled you may instead want to check if the relevant lines were printed out.
   You can patch the print statement using @patch('builtins.print') and passing in mock_print to test case
   To assert a call was made to a mock you can use the assert_called_with method (e.g.: mock_print.assert_called_with("Line you expected on console))
   You can also check if it was printed out multiple times by using assert_has_calls like:
   ```python
   mock_print.assert_has_calls([
            call("Line you expect"),
            call("Another line you expect"),
            call("Yet another line you expect"),
        ], any_order=False)
   ```
   any_order is False if order matters, True otherwise

## Last 10 minutes
When you are nearing the end of the workshop, for any test cases you have not finished replace the contents of the test case with self.assertEqual(1,1)

Then on the command line/terminal/python envrionment at the top level of this project do ```pip install mutmut```

Run ```mutmut run``` and see how many mutants were created and how many survived. Calculate your mutation score (killed/total)

Run ```mutmut results``` and try analyzing your results using ```mutmut result-ids``` to see the result ids and ```mutmut show <id>``` to view a mutant.

Try and think if the mutant is sensible and how could you have improved your test cases.
## Extra

Check test coverage with:

`coverage run main.py Ford`

`coverage report -m`