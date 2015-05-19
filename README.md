
#CartoDBToolbox

CartoDB Toolbox for Arcgis Desktop.  It allows you to upload data from Arcgis Desktop to a CartoDB account.


## Features

* Upload data from Arcgis Desktop to CartoDB
* (For ArcGis Server /  Online layers you  can use the [Arcgis Connector](http://docs.cartodb.com/cartodb-platform/import-api.html#the-arcgis-connector)   )

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


## Basic Usage

You can use the import tool to CartoDB like any other toolbox.

Parameters:
* CartoDB User Name
* Your Api Key
* Features to be uploaded

![CartoDB Toolbox](docs/screenshot.png?raw=true "CartoDB Toolbox")

![CartoDB Toolbox](docs/importing_data.png?raw=true "CartoDB Toolbox")

And Voila! Your data is now available on CartoDB

![CartoDB Toolbox](docs/importing_ok.png?raw=true "CartoDB Toolbox")


## "Advanced" Usage

You can also use *CartoDB Toolbox* in model builder.

For example, this model clips features using a buffer. The geoprocessing results are automatically uploaded to CartoDB.

![CartoDB Toolbox](docs/Example_Model.png?raw=true "CartoDB Toolbox")

- Original data:

![CartoDB Toolbox](docs/agd.png?raw=true "CartoDB Toolbox")

- Clipped features uploaded to CartoDB:

![CartoDB Toolbox](docs/model_result.png?raw=true "CartoDB Toolbox")


# Contributors

- Juan Méndez ( [@dersteppen](https://twitter.com/dersteppen) )
  

# 3rd Party Scripts

-   [cartodb-utils.py](https://gist.github.com/andrewxhill/093c89fa45e5f657fec7)    by  Andrew W. Hill  ( [@andrewxhill](https://twitter.com/andrewxhill) )
-   [Zip (compress) Python script by Esri](http://arcg.is/1HsK0P0) 


