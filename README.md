# Report kind-of-automation app for Steven by Juwon Chun.

## <strong>Before you start ...</strong>
1. Open terminal and put command lines below to install pip
~~~
curl -O http://python-distribute.org/distribute_setup.py
sudo python distribute_setup.py
sudo rm distribute_setup.py
sudo easy_install pip
~~~
2. After installing pip, put the command below to install selenium
~~~
pip install selenium
~~~
3. To run this app, type 
~~~
python run.py
~~~

4. If one above doesn't work, try
~~~
python3 -m run.py
~~~
***
### How to set up username and password
1. Go to line 10, 11 and find variables *username* and *password*.
2. Put your username and password in ' (here) '


### How to add more menu
1. Go to line 27 and customize it with existing menu name on the website. (ex: 'new menu name == 3\n)
2. Go to line 29 and add *elif* statement. (ex: *elif* menu is 3: )

### How to find Xpath(preferably 'full Xpath') from Chrome
1. Put F12 and open console.
2. Right click on the element you want to find Xpath of.
3. Click 'Inspect' and find it in console.
4. Right click on the element info you found in console and click copy-copy Xpath

### Can't find help?
Just text me mate
