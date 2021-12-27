from pathlib import Path

import jinja2
from invoke import task

DEFINITIONS_DIR = [Path("draft") / "DataProducts"]


@task()
def bootstrap_html(ctx):
    """
    Creates corresponding HTML file next to each data product definition
    """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("utils"))
    for definitions_root in DEFINITIONS_DIR:
        for p in definitions_root.glob("**/*.json"):
            template = env.get_template("definition.html.jinja2")
            html_content = template.render(name=p.with_suffix("").name)
            html_file = p.with_suffix(".html")
            html_file.write_text(html_content)
            print(f"{html_file} written")


@task()
def convert_definitions(ctx):
    """
    Convert data product definitions from python sources to OpenAPI specs
    """
    from src.converter import convert_data_product_definitions

    convert_data_product_definitions()
