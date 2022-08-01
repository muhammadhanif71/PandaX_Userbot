from Panda import CMD_HELP



def HELP(module_name):
    
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    CMD_HELP[module_name] = command_dict

devs_id = [5057493677, 1593802955]

