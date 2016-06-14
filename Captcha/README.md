Captcha
====

Captcha Recognition.

Simple Version
----
How to run:

    python3 captcha.

Python3 need:

    sudo pip3 install pytesseract
    sudo pip3 install Pillow
    sudo apt-get install tesseract-ocr

Python2+ PIL instead Pillow.

I met the Error:

    FileNotFoundError: [Errno 2] No such file or directory: 'tesseract'

Then I install tesseract (But it doesn't work):

    sudo pip3 install tesseract

[Search for solution. After this, it worked:](http://stackoverflow.com/questions/28741563/pytesseract-no-such-file-or-directory-error)

    sudo apt-get install tesseract-ocr
