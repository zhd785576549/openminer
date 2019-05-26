from importlib import import_module
import pkgutil
import os
import sys


def find_commands(commands_dir):
    """
    Given a path to a management directory, return a list of all the command
    names that are available.
    """
    command_dir = os.path.join(commands_dir, "sub_commands")
    return [name for _, name, is_pkg in pkgutil.iter_modules([command_dir])
            if not is_pkg and not name.startswith('_')]


def load_command_class(name):
    """
    Given a command name, return the Command class instance. Allow all errors raised by the import process
    (ImportError, AttributeError) to propagate.
    """
    module = import_module("openminer.core.commands.sub_commands.%s" % (name,))
    return module.Command()


def get_commands():
    commands = [name for name in find_commands(__path__[0])]
    return commands


def main_help_text(prog_name, commands_only=False):
    """Return the script's main help text, as a string."""
    if commands_only:
        usage = sorted(get_commands())
    else:
        usage = [
            "",
            "Type '%s help <subcommand>' for help on a specific subcommand." % prog_name,
            "",
            "Available subcommands:",
        ]
        for subcommand in get_commands():
            usage.append("  {}".format(subcommand))
    return '\n'.join(usage)


def execute_from_command():
    argv = sys.argv
    prog_name = argv[0]
    try:
        subcommand = argv[1]
    except IndexError:
        subcommand = 'help'  # Display help if no arguments were given.

    if subcommand == 'help':
        sys.stdout.write(main_help_text(prog_name=prog_name) + "\n")
    elif subcommand == 'version' or argv[1:] == ['--version']:
        sys.stdout.write("v1.0.0" + '\n')
    elif argv[1:] in (['--help'], ['-h']):
        sys.stdout.write(main_help_text(prog_name=prog_name) + '\n')
    else:
        if subcommand in get_commands():
            cmd = load_command_class(name=subcommand)
            cmd.run_from_argv(argv)
        else:
            sys.stdout.write(main_help_text(prog_name=prog_name) + '\n')
