## Installation Windows
For now you will need to run Python 3.9 (Version 3.10 will not work) | 09.12.2021
If you have different Versions of Python installed on your machine you might need to change the Version used in you environment variables
https://www.geeksforgeeks.org/how-to-set-up-command-prompt-for-python-in-windows10/
The Keywords "py" and "python" might be connected to different versions
e.g.
```
py --version => python 3.9.9
```
```
python --version => python 3.10
```


If you are Running the right version,
Run Powershell in the repositorys main Folder (Shift + Rightclick > Run Phowershell)
Insinde Powershell switch to cmd, in order to have all the neccesary privileges

 ```
 cmd
 ```

Create and prepare the virtual Python environment
```
py -m venv venv
```
```
cd venv
```
```
Scripts\activate
```
```
cd..
```
```
pip install --upgrade pip
```
```
pip install wheel
```
```
pip install -r requirements.txt
```

### SASS & SCSS

For SASS and SCSS to work, you need to use "file Watchers" in PyCharm. **An installation of Node.js is mandatory**.


```cmd
npm --version
```


```cmd
npm install -g sass
```


## Start Web Service

### Normal Startup - Linux

Login activated, debuging deactivated

````
./startflask
````

### Normal Startup - Windows
```
python app.py
```
or
```
startup.bat
```

Note: If the Python environment is already installed, the following steps might be enough to activate the environment and start up the app
1. `cd venv`
2. `Scripts\activate`
3. `cd..`
4. `python app.py`
