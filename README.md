# AdventOfCode2019
This project contains my solutions for advent of code (https://adventofcode.com/).
I have chosen to solve the tasks by using Python 3.7.0.

## Working process
In this project I have started from scratch and progressively updated my code and the structure of my project. The progress improvement can be seen by going from task in the beginning to later tasks.

I've also created a nice workspace to easily run my python code, with imports, directly from the task it self, in visual studio code, by pressing CMD+shift+B.

## Running my python files
I've had problems with getting imports from sibling folders to my python files. Where I tried many solutions and discovered a nice way to make it really easy. More info about this can be found from this stackOverflow question I posted: [import-python-file-from-another-folder-that-is-not-a-child](https://stackoverflow.com/questions/59147120/import-python-file-from-another-folder-that-is-not-a-child)

I come up with a way to make it really easy to have a folder structure like this and get the imports to work correctly in the terminal.

Basically what I did was:
 - created a pyhton script
 - created a task in visual studio code

With this I can now run my python files, with the imports, by only pressing cmd + shift + B.

---

### Explanation

The visual studio task:

```
{
	"version": "2.0.0",
	"tasks": [
		{
			"label": "Run python file",
			"type": "shell",
			"command": "python3 /PATH_TO_ROOT_FOLDER/run_python_file.py ${file}",
			"group": {
				"kind": "build",
				"isDefault": true
			},
			"presentation": {
				"reveal": "always",
				"panel": "new",
				"focus": true
			}
		}
	]
}
```
The part that we want to focus on is this one:
`"command": "python3 /PATH_TO_ROOT_FOLDER/run_python_file.py ${file}",`
 - This part run the new python file I created at the root folder, and passes the path to the file which is active

The python script:
```
import os, sys

# This is a argument given trough a shell command
PATH_TO_MODULE_TO_RUN = sys.argv[1]

ROOT_FOLDER = "root/"

def run_module_gotten_from_shell():
    # Here I take only the part of the path that is needed
    relative_path_to_file = PATH_TO_MODULE_TO_RUN.split(ROOT_FOLDER)[1]

    # Creating the shell command I want to run
    shell_command = createShellCommand(relative_path_to_file)

    os.system(shell_command)


# Returning "python3 -m PATH.TO.MODULE"
def createShellCommand(relative_path_to_file):
    part1 = "python3"
    part2 = "-m"

    # Here I change the string "dir1/task11.py" => "dir1.task11"
    part3 = relative_path_to_file.replace("/", ".")[:-3]

    shell_command = "{:s} {:s} {:s}".format(part1, part2, part3)
    return shell_command

run_module_gotten_from_shell()
```

 - This python script gets as parameter the path to the active file
 - Then it creates a shell command of the path (the shell command is like @kasper-keinänen 's answer)
 - Then it run that shell command

 With these modifications, I can run any file inside the root directory with imports from any file inside the root directory.

 And I can do it by only pressing cmd + shift + B in visual studio code.