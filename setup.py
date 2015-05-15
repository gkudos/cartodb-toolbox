'''
python setup.py bdist_wininst
'''
from distutils.core import setup
setup(name='CartoDB Toolbox For Arcgis',
    author='Juan Mendez (@dersteppen)',
    author_email='juan@gkudos.com',
    description='CartoDB Toolbox For Arcgis.',
    license='Apache 2.0',
    version='1.0',
    packages=['gkudos'],
    package_dir={'gkudos': 'gkudos'},
    package_data={'gkudos': ['esri/toolboxes/*.*']},
    classifiers=(
        'Development Status :: Production/Stable',
        'Intended Audience :: GIS Users',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
    )