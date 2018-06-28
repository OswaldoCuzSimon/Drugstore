# Drugstore

## Installation

### Download selenium driver

~~~bash
wget https://chromedriver.storage.googleapis.com/index.html?path=2.40/
unzip unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip
~~~
### Install dependencies
~~~bash
virtualenv -p /usr/bin/python3.6
source env/bin/activate
pip install -r requirements.txt
~~~

## Run project
~~~bash
jupyter notebook
~~~
