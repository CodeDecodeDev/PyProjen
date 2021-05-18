import commands
import commands_dict
import sys



def get_input():

    args = sys.argv

    if len(args) == 1:
        commands.main_cmd()

    
    else:
        handled = False
        for command_name in commands_dict.Commands.keys():
            if args[1] == command_name:
                commands_dict.Commands[command_name]()
                handled = True
                break
        if not handled:
            commands.command_not_found(" ".join(args[1:]))
get_input()