import click
from time import sleep
import os.path
import json
from tabulate import tabulate

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_DIR = os.path.join(ROOT_PATH, "conf")
CONFIG_FILE = os.getenv("CONFIG_FILE", 'application.conf')
config_file_path = os.path.join(CONF_DIR, CONFIG_FILE)

if os.path.isfile(config_file_path):
    with open(config_file_path, 'r') as f:
        app_config = json.load(f)
else:
    app_config = {}


# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name, color='green')

CONTEXT_SETTINGS = dict(
    default_map=app_config
)


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


@cli.command()
@click.argument('host')
@click.option('--port', default=2181, help='db port')
@click.option('--protocol', prompt='proto', default='http', type=click.Choice(['http', 'https']))
def connect(host, port, protocol):
    click.echo('connecting: %s://%s:%s' % (protocol, host, port))
    with click.progressbar(length=5, label='progress') as bar:
        for i in range(5):
            bar.update(i)
            sleep(1)
    click.clear()
    click.echo('byy byy')


@cli.command()
@click.option('--port', prompt='enter port', help='db port')
def config(port):
    query_param = app_config.setdefault('query', {})
    query_param['port'] = port
    with open(config_file_path, 'w+') as f:
        json.dump(app_config, f)


@cli.command()
@click.option('--port', prompt="enter port")
@click.option('--format', prompt='format', default='tab', type=click.Choice(['tab', 'json']))
def query(port, format):
    click.echo('query port: %s' % port)

    def print_json(data_json):
        print json.dumps(data_json, indent=4, sort_keys=True)

    def print_tab(data_json):
        data = [row.values() for row in data_json]
        headers = data_json[0].keys()
        print tabulate(data, headers)

    options = {
        'tab': print_tab,
        'json': print_json
    }

    data_json = [
        {"name": "A", "age": 20, "some eles": "346surfgy", "more": "jhfsdkhfjksdhj"},
        {"name": "A", "age": 20, "some eles": "346surfgy", "more": "jhfsdkhfjksdhj"}
    ]

    options[format](data_json)

if __name__ == '__main__':
    cli()
