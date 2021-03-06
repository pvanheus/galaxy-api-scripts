#!/usr/bin/env python

"""
    Copyright 2016 Peter van Heusden <pvh .at. sanbi.ac.za>

    This file is part of pvh's galaxy-api-scripts.

    galaxy-api-scripts is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    galaxy-api-scripts is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with galaxy-api-scripts.  If not, see <http://www.gnu.org/licenses/>.
"""

import common
import click

GALAXY_URL = 'https://galaxydev.sanbi.ac.za/api'

@click.group()
@click.option('--galaxy_url', default=GALAXY_URL)
@click.argument('api_key')
@click.pass_context
def cli(ctx, galaxy_url, api_key) -> None:
    ctx.obj['galaxy_url'] = galaxy_url
    ctx.obj['api_key'] = api_key

@cli.command()
@click.pass_context
def list_tools(ctx):
    url = ctx.obj['galaxy_url'] + '/tools'
    print(url)
    common.display(ctx.obj['api_key'], url)

@cli.command()
@click.argument('tool_id')
@click.pass_context
def display_diagnostics(ctx, tool_id):
    url = ctx.obj['galaxy_url'] + '/tools/{}/diagnostics'.format(tool_id)
    print(url)
    common.display(ctx.obj['api_key'], url)

@cli.command()
@click.pass_context
def list_resolvers(ctx):
    url = ctx.obj['galaxy_url'] + '/dependency_resolvers'
    print(url)
    common.display(ctx.obj['api_key'], url)

@cli.command()
@click.argument('api_key')
@click.argument('resolver_index')
@click.argument('tool_id')
@click.argument('version', required=False)
@click.pass_context
def resolve_dep(ctx, resolver_index, tool_id, version=None):
    url = ctx.obj['galaxy_url'] + '/dependency_resolver/{index}/dependency'.format(resolver_index)

@cli.command()
@click.pass_context
def list_tool_data(ctx):
    url = ctx.obj['galaxy_url'] + '/tool_data'
    print(url)
    common.display(ctx.obj['api_key'], url)

@cli.command()
@click.argument('tool_id')
@click.pass_context
def display_tool_data(ctx, tool_id):
    url = ctx.obj['galaxy_url'] + '/tool_data/{}'.format(tool_id)
    print(url)
    common.display(ctx.obj['api_key'], url)

@cli.command()
@click.argument('tool_id')
@click.pass_context
def reload_tool_data(ctx, tool_id):
    url = ctx.obj['galaxy_url'] + '/tool_data/{}/reload'.format(tool_id)
    print(url)
    common.display(ctx.obj['api_key'], url)

if __name__ == '__main__':
    cli(obj={})
