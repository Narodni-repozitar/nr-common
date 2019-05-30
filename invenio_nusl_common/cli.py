from jsonref import JsonRef
import json
import click
import os


@click.command()
@click.argument('input', type=click.Path())
@click.argument('output', type=click.Path())
def refrep(input, output):
    """
    A script replacing references ($ref) in json schemas.
    :param input: Path to the source file with references.
    :param output: Path to place where json will be resolved.
    :return: Resolved json file without references.
    """
    old_json = json.load(open(input))
    new_json = JsonRef.replace_refs(old_json)
    with open(output, "w+") as write_file:
        json.dump(new_json, write_file)

    click.echo("JSON file was succesfully resolved and was saved at this location: {}".format(os.path.abspath(output)))


if __name__ == "__main__":
    refrep()
