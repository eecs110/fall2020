There is a known bug that happens on ***some*** newer MacOS laptops, that is described <a href="https://www.python.org/download/mac/tcltk/" target="_blank">here</a>.

You will know that you have this bug if you try to run one of the course Python files that makes use of the TKinter library (doing stuff with drawings), and your computer shuts down / logs out. If this bug happens to you, not to worry -- there is a workaround. Here is what we suggest:

You will still **EDIT** your python files as you normally would in IDLE. And don't forget to save. However instead of **RUNNING** your files in IDLE (don't press F5), you will use the terminal. To run your python files in terminal:

### 1. Navigate to the directory where your files are stored
First, navigate to the directory where your files are stored. If you don't know how to do this, please refer to the course materials in [Lesson 4](../lectures/week02-lecture02), which describe how to interact with your command line and run your python files using the command line.

### 2. Execute the appropriate Python file using pythonw
Once you're in the correct directory, please execute your file by typing:

```shell
$ pythonw your_file.py
```

Note the "w": `pythonw` instead of `python`. Please ask your TA if you have any questions about this and they can help you.