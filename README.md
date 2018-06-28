# Drugstore

## Installation

### Download selenium driver

~~~bash
wget https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip
~~~
### Install dependencies
~~~bash
virtualenv -p /usr/bin/python3.6 env
source env/bin/activate
pip install -r requirements.txt
~~~

### Run project
~~~bash
jupyter notebook
~~~
