
#CartoDBToolbox

CartoDB Toolbox for Arcgis Desktop.  It allows you to upload data from Arcgis Desktop to a CartoDB account.


## Features

* Upload data from Arcgis Desktop to CartoDB

## Supported Versions

* Arcgis Desktop  10.3

## Install

### Prerequisites :  Requests Library

[Requests](http://docs.python-requests.org/en/latest/)
[Install Guide](http://docs.python-requests.org/en/latest/user/install/)

or...

Add the python that arcgis use to your system path. ( i.e. *c:\Python27\Arcgis10.3\*  )
* See [ How to set the path and environment variables in Windows](http://www.computerhope.com/issues/ch000549.htm)

Download the zipball  from  https://github.com/kennethreitz/requests/zipball/master

Unzip it.

Use the command Prompt to install the package: 
'''
cd kennethreitz-requests-ab1f493
python setup.py install
'''

### Toolbox 

Download the installer from  https://github.com/gkudos/cartodb-toolbox/releases/download/1.0/CartoDB.Toolbox.For.Arcgis-1.0.win32.exe

Run the installer


![Installer](docs/install01.png?raw=true "Installer")

![Installer](docs/install2.png?raw=true "Installer")

Once installed,  CartoDB toolbox must appear on ArcToolbox 

![Installer](docs/install3.png?raw=true "Installer")


## Use

You can use the import tool to CartoDB like any other toolbox.

Parameters:
* CartoDB User Name
* Your Api Key
* Features to be uploaded

![CartoDB Toolbox](docs/screenshot.png?raw=true "CartoDB Toolbox")

![CartoDB Toolbox](docs/importing_data.png?raw=true "CartoDB Toolbox")

And Voila! Your data now it is available on CartoDB 

![CartoDB Toolbox](docs/importing_ok.png?raw=true "CartoDB Toolbox")





