# SQL-Concatenator <img src="https://i.ibb.co/pRT6B9x/face.png" alt="" width="40"/>
A simple Python utility for concatenating some delimited input string into a format for a SQL IN statement.

![SQL Concatenator Demo](https://i.ibb.co/pXkrxHp/Concatenator.gif)

I originally created this while on the technical support team at Heavy Construction Systems Specialists (HCSS) because I would frequently find myself needing to write SQL queries that involved `IN` statements.
This little utility helped speed up the process, and I still find myself using it every so often while working with SQL.

## Usage

The compiled code exists in a standalone executable in the `dist` folder. The application can also be launched from the a terminal with the following command:
```python
python main.py
```

## Compiling

Everything should run out of the box by running main.py, for example:
```python
python main.py
```
The code can commpile into a standalone executable for those who wish to use the utility without the command line.
Instructions below for compiling into an executable.

## Building Executable

If you'd like to build the standalone executable, I've included the PyInstaller .spec file to accomplish that for you. To build a new .exe, open a command prompt window in the project directory and run the following:


```python
pyinstaller build.spec
```
When PyInstaller finishes running, the new .exe file will be located in /dist. You may need to run 'pip install pyinstaller' if you don't already have it.

## Usage
Using the SQL-Concatenator is pretty simple.
- Paste the un-concatenated input into the *Input* section
- Verify that the delimiter is properly set (Note that *Line* and *Custom* can both be selected. For custom-only delimiter, ensure that *Line* is unchecked).
- Click **Concatenate** to write to the *Output* section. **Copy to Clipboard** will do the thing that the button says.

## Tests

There are a few unit tests for various input configurations. To run tests:
```python
python main.py -test
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
