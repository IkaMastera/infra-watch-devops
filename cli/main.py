import click 
from utils.ping import ping_host

@click.group()
def cli():
    """InfraWatch CLI - Monitor your system like an SRE."""
    pass

@cli.command()
@click.argument("host")
def ping(host: str):
    """Ping a host to check latency and status."""
    if ping_host(host):
        click.echo(f" {host} is reachable.")
    else:
        click.echo(f"{host} is not reachable.")
    

if __name__ == "__main__":
    cli()