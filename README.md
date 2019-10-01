# Ubuntu-Fix127

Script to download and compile the current linux kernel(5.3.1) and apply the Header127 Patch for people who are experiencing the Header 127 bug with AMD Cards with the UEFI reset bug 

To run this script you will need python3 and pip3

``` sudo apt install python-3 python3-pip ```

Check which version of python is rubnning on your system with:
``` python --version ```

If it shows anything under python3 then you will need to change your enviorment variable to run python 3
``` sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1 ```
