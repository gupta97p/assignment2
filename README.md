It is a python django based project. So you need to install PIP first, though pip comes with python still if its not there you can install it by running 
`python get-pip.py` 
Verify it by running 
`pip -V`
After cloning this repo, cd into it.
Then in the terminal write
`pip install -r requirements.txt`

The above command will install all the dependencies required for this project to run

Then you just have to come into the test1 folder where you can see manage.py file, this file is responsible for running the project
`python3 manage.py runserver`

This will run the project on localhost:8000

Note: Based on different os and version of python, you might need to replace python3 with python,py,py3. This project is based on python 3.x
