from argparse import ArgumentParser
import os
import sys


class BaseCommand(object):
    help = ""
    version = ""

    def get_help(self):
        return self.help

    def get_version(self):
        return self.version

    def create_parser(self, prog_name, subcommand, **kwargs):
        parser = ArgumentParser(
            prog='%s %s' % (os.path.basename(prog_name), subcommand),
            description=self.help or None,
            **kwargs
        )
        parser.add_argument('--version', action='version', version=self.get_version())
        parser.add_argument(
            '-v', '--verbosity', default=1,
            type=int, choices=[0, 1, 2, 3],
            help='Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output',
        )
        self.add_parser(parser)
        return parser

    def add_parser(self, parser):
        """
        Entry point for subclassed commands to add custom arguments.
        :param parser: [ArgumentParser] Created by method create_parser
        :return: [ArgumentParser] A custom for subclass command parser
        """
        pass

    def print_help(self, prog_name, subcommand):
        """
        Print the help message for this command
        """
        parser = self.create_parser(prog_name, subcommand)
        parser.print_help()

    def run_from_argv(self, argv):
        """
        Run from args
        :param argv: [list] List of args
        :return:
        """
        parser = self.create_parser(argv[0], argv[1])
        options = parser.parse_args(argv[2:])
        cmd_options = vars(options)
        args = cmd_options.pop("args", ())
        try:
            self.execute(*args, **cmd_options)
        except Exception as e:
            sys.stderr.write("{}\n\r".format(str(e)))
            sys.exit(-1)

    def execute(self, *args, **cmd_options):
        raise NotImplementedError("This method must be implemented.")
