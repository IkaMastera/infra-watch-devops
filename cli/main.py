import click 

@click.group()
def cli():
    """InfraWatch CLI - Monitor your system like an SRE."""
    pass

@cli.command()
@click.argument("host")
def ping(host):
    """Ping a host to check latency and status."""
    click.echo(f"Pinging {host}...")

if __name__ == "__main__":
    cli()