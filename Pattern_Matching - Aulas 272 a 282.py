from dataclasses import dataclass

# def execute_command(command: str) -> None:
#     match command:
#         case 'ls':
#             print('$ listing directories.')
#         case 'cd':
#             print('$ changing directory.')
#         case _:
#             print('$ command not implemented.')
#
#     print('... rest of the code.')

# execute_command('ls')


# Lists
# def execute_command(command: str) -> None:
#     match command.split():
#         case ['ls', path, *arg]:
#             print('$ listing directory', path, *arg)
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('$ command not implemented.')
#
#     print('... rest of the code.')
#
#
# execute_command('ls /desktop/diogenes --force --all')


# pipe (or) operator
# def execute_command(command: str) -> None:
#     match command.split():
#         case ['ls' | 'list', *directories]:
#             for directory in directories:
#                 print('$ listing directories', directory)
#         case ['cd' | 'change', directory]:
#             print('$ changing directory to', directory)
#         case _:
#             print('$ command not implemented.')
#
#     print('... rest of the code.')
#
#
# execute_command('ls /desktop /diogenes /venv')
#

# case guard / if no case
# def execute_command(command: str) -> None:
#     match command.split():
#         case ['ls' | 'list', *directories] if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing directories', directory)
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing directory', directories[0])
#         case ['cd' | 'change', directory]:
#             print('$ changing directory to', directory)
#         case _:
#             print('$ command not implemented.')
#
#     print('... rest of the code.')
#
#
# execute_command('ls /desktop /diogenes /venv')


# Alias "as"
# def execute_command(command: str) -> None:
#     match command.split():
#         case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing directories', directory)
#             print(f'{the_command=}, {the_list=}')
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing directory', directories[0])
#         case ['cd' | 'change', directory]:
#             print('$ changing directory to', directory)
#         case _:
#             print('$ command not implemented.')
#
#     print('... rest of the code.')

# execute_command('ls /desktop /diogenes /venv')


# Dicts
# def execute_command(command: dict) -> None:
#     match command:
#         case {'command': 'ls', 'directories': [*_]}:  # list with one or more values
#             for directory in command['directories']:
#                 print('$ listing directories', directory)
#         case {'command': 'cd', 'directories': [_, *_]}:
#             print('$ changing directory to', command['directories'])
#         case _:
#             print('$ command not implemented.')
#
#     print('... rest of the code.')

# execute_command({'command': 'ls', 'directories': ['/dioge', '/venv', '/repo']})


# With classes (objects)

@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command: Command) -> None:
    match command:
        case Command(command='ls', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing directories', directory)
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing directory to', directory)
        case _:
            print('$ command not implemented.')

    print('... rest of the code.')


command = Command('ls', ['/dioge', '/venv', '/repo'])
execute_command(command)


