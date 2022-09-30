

# def execute_command(command: str) -> None:
#     match command:
#         case 'ls':
#             print('$ listing files.')
#         case 'cd':
#             print('$ changing directory..')
#         case _:
#             print('$ command not implemented.')
#
#     print('... rest of the code.')


def execute_command(command: str) -> None:
    match command.split():
        case ['ls', path, *arg]:
            print('$ listing files.', path, *arg)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:
            print('$ command not implemented.')

    print('... rest of the code.')


execute_command('ls /desktop/diogenes --force')