import os, sys

PATH_TO_MODULE_TO_RUN = sys.argv[1]
ROOT_FOLDER = "adventOfCode/"


def run_module_gotten_from_shell():
    relative_path_to_file = PATH_TO_MODULE_TO_RUN.split(ROOT_FOLDER)[1]
    shell_command = createShellCommand(relative_path_to_file)

    os.system(shell_command)


# Returning "python3 -m PATH.TO.MODULE"
def createShellCommand(relative_path_to_file):
    part1 = "python3"
    part2 = "-m"
    part3 = relative_path_to_file.replace("/", ".")[:-3]

    shell_command = "{:s} {:s} {:s}".format(part1, part2, part3)

    return shell_command


run_module_gotten_from_shell()