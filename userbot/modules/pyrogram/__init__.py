from userbot import CMD_HELP


def HELP(module_name):
    
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    CMD_HELP[module_name] = command_dict

devs_id = [5057493677, 1593802955]


import glob
from os.path import basename, dirname, isfile, join

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")
]



import os


def __list_all_modules():
    import glob
    from os.path import basename, dirname, isfile

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_modules


MODULES = sorted(__list_all_modules())
