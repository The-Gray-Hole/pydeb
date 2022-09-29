
__all__ = [
    'config'
]

from argparse import Namespace
from configargparse import ArgParser
from os import getcwd
from .utils import simple_join


def config() -> Namespace:
    default_pydeb = simple_join(getcwd(), "PYDEB.yml")
    parser = ArgParser()
    parser.add_argument("-c", "--config", required=False, is_config_file=True, help="Configuration file path")
    parser.add_argument("action", action="store", help="build")
    parser.add_argument("--pydeb-file", type=str, action="store", default=default_pydeb, help="Pydeb yaml file")
    name_s = parser.parse_args()

    return name_s
