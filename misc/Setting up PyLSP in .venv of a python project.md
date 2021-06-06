# Setting up Sublime Text 4 for Python

source: https://yeray.dev/python/setting-up-sublime-text-4-for-python

21 May 2021 \- Last updated on 2 Jun 2021

Sublime Text has had its first major upgrade since 2017 with Sublime Text 4.

  Sublime Text is not an IDE nor it pretends to be, but its powerful plugin system has allowed the community to come up with clever ways to have some IDE capabilities.

  I’ve been using ST4 in its beta releases exclusively for some time and arrived at a setup that I enjoy, hopefully you will to.

  I will update this post with any developments in the tools and setup.

  more

  Disclaimer: This setup will not make ST4 behave like PyCharm or even like VSCode. When you choose ST4 you are sacrificing some IDE features for speed and performance.

  The tools

  I’ve used Sublime Text for Python since I bought my first ST3 license in 2017. At the time the state-of-the-art way of working in Python was to use Anaconda (not to be confused with Anaconda, the Python distribution). Anaconda still works in ST4 but it’s unfortunately lacking some maintenance and its approach has been superseded by language servers.

  Sublime Text does not officially support language servers, however, there is community support via the LSP project allowing plugins to call into different language servers and render results in ST4, and, of course, Python is no exception.

  There are two main language servers available for ST4: LSP-pyright, which will perform type checking via Microsoft’s Pyright, and LSP-pylsp, which is based on Python LSP Server.

  LSP-pyright, will only perform static typing, while LSP-pylsp has a plugin system that allows calling to other types of tools like linters and formatters like mypy, black, or isort.

  Personally, I don’t use Pyright, so I will focus on LSP-pylsp and configuring it with a set of common plugins.

  The setup

  LSP-pylsp is straight forward to setup as described in its README. Once installed go to the LSP-pylsp preferences and add the following configuration:

  {
    "pylsp.plugins.mypy-ls.enabled": true,
    "pylsp.plugins.flake8.enabled": true,
    "pylsp.configurationSources": ["flake8"],
    "pylsp.plugins.pyls_black.enabled": true,
}
  

  After restarting Sublime Text, open a project and you should see the following:

  
    
      Hovering over a symbol should render information about it with links to its definition and references:

    
    
      You should see Flake8 and mypy errors as you type by hovering over the warning and error squiggly lines or openin the LSP diagnostics panel with LSP: Toggle Diagnostics Panel:

    
    
      Invoke LSP: Format File to format with Black and isort:

    
    
      Invoke LSP: Rename to rename a symbol using Jedi

    
  

  Manual setup

  LSP-pylsp installs Python Language Server in ST4’s Package Storage directory with the Python interpreter present in your PATH environment variable. It then proceeds to create a virtual environment and install its dependencies on it.

  While this is likely completely fine for most users, you may want more control over the Python version and the versions of the dependencies, potentially ensuring they match the ones in your project. If that’s the case you can setup ST4 and Python LSP Server manually as follows:

  
    
      Install LSP using the package manager:
    
    
      In your project’s virtual environment (you are using a virtual environment, right?)
    
  

  pip install python-lsp-server[all] python-lsp-black mypy-ls pyls-isort
  

  And any other PyLSP plugins you see fit, these are the ones I use most.

  
    
      Go to the Sublime Text preferences, Package Settings, LSP, Settings, to open the general settings for LSP where we will configure some default options for PyLSP and its plugins.

    
    
      Add the following:
    
  

  {
    "clients": {
        "pylsp": {
            "enabled": false,  // we will enable PyLSP at the project level
            "selector": "source.python",
            "settings": {
                "pylsp.plugins.pyflakes.enabled": false, // enabled by default, use flake8
                "pylsp.plugins.pycodestyle.enabled": false, // enabled by default, use flake8
                "pylsp.plugins.flake8.enabled": true,  // flake8 is included in pyls
                "pylsp.configurationSources": [
                  "flake8",   // discover flake8 config in ~/.config/flake8, setup.cfg, tox.ini and flake8.cfg
                ],
                "pylsp.plugins.jedi_rename.enabled": true,  // included in pyls
                // File formatter, invoke via LSP: Format file
                "pylsp.plugins.autopep8.enabled": false,  // enabled by default, use black
                "pylsp.plugins.yapf.enabled": false,  // enabled by default, use black
                "pylsp.plugins.black.enabled": true,  // from python-lsp-black
                "pylsp.plugins.mypy_ls.enabled": true,  // from mypy-ls
            },
        },
    },
}

  

  Note that enabled is false in the global LSP settings. This is on purpose to prevent Sublime Text 4 from trying to start an Python LSP Server on all windows. The idea is to only start the server present in each project’s virtual environment separately.

  
    Save your Sublime Text Project if you haven’t yet and edit its configuration as follows:
  

  {
    // This section should be present already
    "folders":
    [
        {
            "path": "<ABSOLUTE_PATH_TO_YOUR_PROJECT>",
        }
    ],
    // Add this whole section if not present or just the LSP settings
    "settings": {
        "LSP": {
            "pylsp": {
                "enabled": true,
                "command": [
                    "<ABSOLUTE_PATH_TO_YOUR_VENV>/bin/pylsp",
                ],
                "settings": {
                    "pylsp.plugins.flake8.executable": "<ABSOLUTE_PATH_TO_YOUR_VENV>/bin/flake8",
                },
            },
        },
    },
}
  

  Make sure you replace <ABSOLUTE_PATH_TO_YOUR_VENV> with the absolute path to your virtual environment.

  
    You should be able to see the effects described in the setup above.
  

  Troubleshooting

  No flake8 linting

  If you find things are working but you are not getting flake8 errors, make sure you’ve set up the pylsp.plugins.flake8.executable setting in your project and it’s set to the correct absolute path. If it is not set, or if it is incorrect you will not get errors in Sublime Text but simply no linting information.

  Other

  If you find some of the plugins are not working or ST4 is showing an error about PyLSP crashing, you may want to add the following lines to the command list in the project’s config:

  "command": [
    "<ABSOLUTE_PATH_TO_YOUR_VENV>/bin/pylsp",
    "--log-file",
    "<ABSOLUTE_PATH_TO_A_LOG_FILE>",
    "--verbose"
],
  

  The server should restart on each change to the project’s configuration file, but you may need to restart ST4 (luckily it’s lightning fast). You should see the output of PyLSP in that log file which will help you debug any problems. Typical errors include missing dependencies and disabled or incorrect configurations, the logs will include which plugins are active and inactive.

  If you find any issues with this setup let me know in this blog’s repo.

  Extras

  You may also want to install the following Sublime Text packages:

  
    MagicPython
  

  Acknowledgements

  I would like to thank the Spyder IDE team for taking the time to fork and maintain Python LSP Server as well as to all the maintainers of the different plugins for PyLSP for adapting to the fork and releasing new versions promptly.

  And, of course, the Sublime HQ team for making an awesome text editor.

  Updates

  2021-06-02

  
    Amend Black plugin to python-lsp-black.
    Disable yapf formatter on LSP general settings as it seems to interfere with Black.
  

  2021-05-31

  
    Added LSP-pylsp as main method of setup.
    Amend incorrect statement that LSP is officially supported by Sublime Text when it’s a community project.
    Remove troubleshooting “index out of range” section which was fixed recently in LSP.
