from Panda import CMD_HELP



def HELP(module_name, commands):
    
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict

devs_id = [5057493677, 1593802955]

