## 2.1 Installing Python

First, you’re going to need Python installed on your PC. This might seem obvious, but it’s a little more involved than it might first appear. Not all operating systems come with Python installed, and sometimes when Python is installed, it’s an older version. Even if the version of Python already installed on your PC is recent, it’s still a good idea to install Python for your use while developing.

If Python is installed along with the operating system, there’s a good chance it’s being used for system-level functions by the operating system. If that’s the case, there’s a good chance your operating system is dependent on the version of Python it came with, and any modules that were installed for that version to use.

The programming examples in this book will ask you to install additional third-party libraries using the Python package management tool pip. It’s a bad idea to install these other libraries in your system installed Python. This is because a newly installed version of a library might change the functionality of an existing system requirement and break it.

You also don’t want updates to the operating system to change the Python functionality you depend on for your development efforts.

With that in mind, you’ll install version 3.8.0 of Python that will be distinct from any operating system installed version. The newly installed version of Python is entirely under your control and independent of the operating system. This means you can add, remove, and update library modules as you see fit, and only your program code will be affected.

You’ll install the stable 3.8.0 version of Python so you’ll have the same version the example programs in this book were built and tested against to minimize runtime problems.

### 2.1.1 Windows

Depending on when you’re reading this book, Python may or may not be installed by default on Windows. The Windows operating system isn’t known to use Python, so once Python is installed, it is available solely for your development work.

Windows 10 versions 1903 and later make Python available in the Microsoft Store, which makes installation very easy. The Microsoft Store version of Python at the time of this writing is being evaluated, and not all features are guaranteed to be stable. This doesn’t mean you shouldn’t use it, just that you should be aware of these issues.

If you prefer, use the stable 3.8.0 version of Python available for your version of Windows by navigating to [http://www.python.org](http://www.python.org/) in your browser and following the Downloads links. For most users, the straightforward version to use is the executable installer suitable for your CPU and OS version.

During the installation process, the installer allows you to check a box that adds Python to your PATH environment variable. Check this box and save yourself some trouble later. If you miss this and Python doesn’t run from within PowerShell at the command prompt, you can always re-run the installer and add Python to the path.

### 2.1.2 Mac

On the Mac, there is currently an older version of Python installed, which you should avoid using for your development. Instead, install a recent version of Python that’s completely separate from the system. To perform this installation, use the pyenv utility program. This program lets you install as many versions of Python as you’d like, and switch between them. For your purposes, you’ll install Python version 3.8.0.

You’ll need to have the Homebrew program installed on your Mac to follow the next steps. Homebrew is a package manager for the Mac OS you can use to install many useful command-line tools, like pyenv. The Homebrew program and its installation instructions are available here, [https://brew.sh](https://brew.sh/). Open your terminal program and follow these command line steps to install pyenv:

1.  Run the command: brew install pyenv
2.  Enter this line into your shell configuration file (.zshrc for me, could be .bash\_profile for you):
3.  a) echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\\n eval "$(pyenv init -)"\\nfi' >> ~/.zshrc
4.  Run the command: exec “$SHELL”
5.  Run the command: pyenv install 3.8.0
6.  Run the command: pyenv versions

1. Run the command: brew install pyenv
2. Enter this line into your shell configuration file (.zshrc for me):
3. echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc
4. Run the command: exec “$SHELL”
5. Run the command: pyenv install 3.8.0
9. Run the command: pyenv versions

Line 1 installs the pyenv utility program on your Mac.

Line 2 adds useful setup information to your terminal configuration file to make using pyenv easier.

Line 3 re-runs your shell creation scripts, making the commands in line 2 active.

Line 4 installs Python version 3.8.0 onto your Mac in your home folder in the .pyenv folder.

Line 5 shows the versions of Python installed, and if this is the first time using pyenv, this will show the system version and the 3.8.0 version you just installed.

### 2.1.3 Linux

There are so many versions of Linux in general use it would be awkward and outside the scope of this book to present pyenv installation instructions for all those versions. However, if you’re using Linux as your development platform, you’re probably already familiar with how to find what you need to install applications like pyenv on the Linux system you’re using.

Even on Linux systems that have Python 3 installed, it’s better to install and explicitly control the version of Python you’re going to use for development. Once pyenv is installed, use it to install Python version 3.8.0 with the following command lines:

-   pyenv install 3.8.0
-   pyenv versions

The first command installed the version of Python you’re going to use for the examples in this book in a directory controlled by pyenv. That version is kept separate from any other Python versions installed with pyenv, and the system version of Python. The second will list the versions installed, which should show the version you just installed.
