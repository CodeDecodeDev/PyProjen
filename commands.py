import platform
import subprocess
import os



def main_cmd():

    print(
'''
Welcome to PyProjen!

Commands:
    make <project name>: Makes a project named <project name> (Passed argument) in the current directory.
    init: Initialzes, installs dependencies. Auto initializes when make is ran but still exists.
    help: Shows where to find help and register bug reports.

Bug reports:
    For bug reports, see https://github.com/something
'''
    )


def init():

    if platform.system() == "Linux" or platform.system() == "Darwin":

        subprocess.check_output(["pip3", "install", "virtualenv"])
        print("Initialized PyProjen")

    elif platform.system() == "Windows":

        subprocess.check_output(["pip", "install", "virtualenv"])
        print("Initialized PyProjen")

    else:

        try:

            subprocess.check_output(["pip3", "install", "virtualenv"])
            print("Initialized PyProjen")
        
        except:

            try:
                
                subprocess.check_output(["pip", "install", "virtualenv"])
                print("Initialized PyProjen")
            
            except:

                print("Failed to initialize. Check if pip is added to PATH and works by executing \"pip\" or \"pip3\"")


def make(project_name):
    
    init()
    
    subprocess.check_output(["mkdir", str(project_name)])
    os.chdir(os.getcwd() + "/" + project_name)
    subprocess.check_output(["virtualenv", "Python"])
    subprocess.check_output(["mkdir", ".vscode"])
    os.chdir(os.getcwd() + "/" + ".vscode")
    subprocess.check_output(["touch", "settings.json"])
    with open("settings.json", "w") as f:
        f.write("{\"python.pythonPath\": \"Python/bin/python\"}")
    os.chdir("..")
    subprocess.check_output(["touch", "app.py"])
    subprocess.check_output(["code", "."])


def command_not_found(command):

    print(f'''
Command {command} not found!
Run "PyProjen" to get a list of commands.
    ''')