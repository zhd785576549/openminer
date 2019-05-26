"""
This command used to create a new address and store it in local wallet file.
The private address is unique for others
Type:
    t_addr: normal wallet address
    z_addr: zcash wallet address
"""
from openminer.core.commands import base


class Command(base.BaseCommand):

    def add_parser(self, parser):
        parser.add_argument("--type", dest="address_type", choices=["t_addr", "z_addr"], help="Wallet url")
        return parser

    def execute(self, *args, **cmd_options):
        address_type = cmd_options.get("address_type", "t_addr")
