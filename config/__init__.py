from configparser import ConfigParser, ParsingError
from os import path, pardir
from sys import exit

_script_dir = path.dirname(path.abspath(__file__))
_config_path = path.join(_script_dir, pardir, 'config.ini')
_config = ConfigParser()

try:
    _config.read(_config_path)
except ParsingError:
    print('Invalid or absent config.ini file. Exiting')
    exit(1)


def _read_config(config_name):
    try:
        return _config['general'][config_name]
    except KeyError:
        print(f'Key {config_name} is absent in config.ini. Exiting')
        exit(1)


dropbox_token = _read_config('dropbox_token')
database_path = _read_config('database_path')
