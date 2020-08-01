# Instagram contests tool

It can help you to find a winner of the contest where the rules are:  
1. Mention your friend  
2. Like post  
3. Follow

To get the Winner you will have to enter **MEDIA_URL** and **USERNAME** of that media owner to your console and you will get the winner.

For example you entered in your console:
```
python main.py media_url username  
```
   
And a result you will get:
```
The winner is:>  "winners_username"
```
### setting up .env variables   
  You will  have to set your environment variables up with **.env** file where you going to store
  your **PASSWORD AND USERNAME**.  
  

  You can use [Notepad++](https://notepad-plus-plus.org/downloads/) to create this file for Windows,
or [CotEditor](https://coteditor.com/) for MacOS.
  
##### This is an example of how it looks like inside of your .env file. 
(You can choose your own variable names if you want)  
```
INSTAGRAM_USERNAME=YOURuserName
INSTAGRAM_PASSWORD=yOurPassWord
```
Variables has to be with CAPITAL letters and without any spaces at all!



## How to install  

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Project Goals  
To make life easier
