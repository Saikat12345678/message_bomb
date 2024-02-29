# message_bomb

#Linux
#(venv) # pip requirements > 

## Install system-wide using apt: If you want to install the package system-wide, you can use your system's package manager. For 
example, if you're using a Debian-based system like Ubuntu, you can use apt install python3-<package_name> to install Python packages system-wide.

## Create a virtual environment: You can create a virtual environment using python3 -m venv path/to/venv and then activate it using source path/to/venv/bin/activate. Once activated, you can use pip to install packages, and they will be isolated from the system-wide installation.

## Use pipx: If you're installing a Python application and want it to be isolated from your system-wide Python installation, you can use pipx install <package_name>. Pipx manages virtual environments for each package, providing isolation and easy management.

#Linux

step-1: apt install python3
step-2: python3 -m venv path/to/venv
step-0: source path/to/venv/bin/activate
step-4: pip install -r requirements.txt
step-5: python message_bomb.py <run file 

#Termux 


##Termux is a popular terminal emulator and Linux environment app for Android, which allows users to run Linux commands and programs on their Android devices. While Termux provides a comprehensive Linux environment, it doesn't natively support Python's virtual environments (venv) out of the box. However, you can still create virtual environments in Termux using the virtualenv or venv package.

Here's how you can set up a virtual environment using virtualenv:

step-1: pkg install python
step-2: pip install virtualenv
step-00: cd path/to/your/directory # Even if you don't give it
step-4: virtualenv venv
step-5: source venv/bin/activate
step-6: pip install -r requirements.txt
step-7: python message_bomb.py

step-00: deactivate


#Windows

Open Command Prompt or PowerShell: Press Win + R, type cmd or powershell, and hit Enter.

Navigate to your project directory: Use the cd command to navigate to the directory where you want to create the virtual environment.

Create a virtual environment: Use the following command to create a virtual environment named myenv:

step-1:python -m venv myenv
step-2:python -m venv myenv >or> python3 -m venv myenv
step-3:myenv\Scripts\activate
step-4: pip install -r requirements.txt
step-5:  python message_bomb.py


step-00:deactivate

