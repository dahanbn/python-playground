Useful link about Python venv: https://python.land/virtual-environments/virtualenv#Linux_and_MacOS_venv_activation

## 2.2 Python Virtual Environment

Now that you have Python 3.8.0 installed on your computer, completely separate from any system installed Python, you might think you’re ready to go. Even with a version of Python installed using the pyenv utility, you’ll want to use another level of decoupling from that version in your projects.

Python 3.8.0 provides the built-in ability to create virtual environments. Python virtual environments are _not_ like a virtual machine, which allows an entire OS to run as a guest inside a different OS. A Python virtual environment only creates a Python installation inside your project directory. This Python installation can have modules added to it with the pip command, and these modules are only installed and available from the project-specific Python.

### 2.2.1 Windows

In a Windows system, you installed Python directly rather than using pyenv, which works fine as Windows doesn’t use Python as part of its operation. You’ll still want to use a project-specific Python virtual environment to keep your system-level Python installation separated from any modules you’re going to install with pip.

To run the Python virtual environment activation and deactivation scripts, you’ll need to change the Execution Policy of your computer. To do that, you’ll need to run the PowerShell program as an administrator. To do this follow these steps:

1.  Click on the Windows Start icon
2.  Scroll down to the PowerShell menu selection and drop down the sub-menu
3.  Right-click on the PowerShell sub-menu item
4.  From that context menu select Run as Administrator
5.  Once you’re in PowerShell running as administrator, run this command:
6.  Set-ExecutionPolicy Unrestricted

The system will prompt you with a question, which you answer with ‘y’ and then hit the return key. At this point, exit PowerShell so you’re no longer in Administrator mode. You only need to do this once as it’s a system-wide setting.

Open the PowerShell program again, not as an administrator, to get to a command line prompt and follow these steps to create a new Python virtual environment specific to the project directory:

1.  Run the command mkdir <project directory name>
2.  Run the command cd <project directory name>
3.  Run the command python -m venv .venv
4.  Run the command .venv/Scripts/activate
5.  Run the command python -m pip install –-upgrade pip

Line 1 creates a new project directory with whatever name you want to give it.

Line 2 changes your current working context into the newly-created directory.

Line 3 uses the pyenv installed Python to create the Python virtual environment in the .venv directory. This might take a few moments to complete.

Line 4 activates the virtual environment, prepending the command prompt with (.venv), indicating the environment is active. Once the environment is active, any additional libraries installed will be installed in the .venv directory and won’t affect the system-level Python you previously installed. To deactivate the virtual environment, just enter deactivate at the command prompt.

Line 5 is optional and upgrades the version of the pip command that exists within the Python virtual environment you’ve just set up. If pip detects you are running an older version, it will print out a message informing you that you’re running an older version, and you should update that version. You can ignore the information and skip line 5 if you like, I included it because I ran the command to stop seeing that message.

### 2.2.2 Mac and Linux

Setting up a Python virtual environment on the Mac is straightforward if you’ve installed the Python 3.8.0 version using pyenv, as described previously. Open your terminal program and follow these steps to create a new Python virtual environment specific to the project directory:

1.  Run the command mkdir <project directory name>
2.  Run the command cd <project directory name>
3.  Run the command pyenv local 3.8.0
4.  Run the command python -m venv .venv
5.  Run the command source .venv/bin/activate
6.  Run the command pip install –-upgrade pip \[optional\]

Line 1 creates a new project directory with whatever name you want to give it.

Line 2 changes your current working context into the newly-created directory.

Line 3 creates the local file .python-version, which pyenv uses to control what version of Python to run when you’re working in this directory, in this case, the 3.8.0 version.

Line 4 uses the local Python version to create the Python virtual environment in the .venv directory.

Line 5 activates the virtual environment, prepending the command prompt with (.venv), indicating the environment is active. Once the environment is active, any additional libraries installed will be installed in the .venv directory and won’t affect the pyenv Python version previously installed. To deactivate the virtual environment, enter deactivate at the command prompt.

Line 6 is optional and upgrades the version of the pip command that exists within the Python virtual environment you’ve set up previously. If pip detects you are running an older version, it will print out a message informing you that you’re running an older version, and you should update that version. You can ignore the information and skip line 6 if you like, I included it because I ran the command it to stop seeing that message.
