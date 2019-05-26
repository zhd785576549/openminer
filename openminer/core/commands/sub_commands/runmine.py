"""
Run mine
"""
from openminer.core.commands import base


class Command(base.BaseCommand):

    help = "Start to run program to mine with multi process or use gpu."

    def add_parser(self, parser):
        parser.add_argument("--enable-gpu", desc="bo_enable_gpu", default=False, help="Weather use gpu or not.")

    def execute(self, *args, **cmd_options):
        pass
