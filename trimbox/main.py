import logging
import re
import string
import sys
from pathlib import Path

import click
from rich.logging import RichHandler
from rich.traceback import install as traceback_install

PT_TO_MM = 2.835

if sys.stdin.isatty():
    traceback_install(show_locals=True)
    logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
else:
    logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger("trimbox")


@click.command()
@click.argument(
    "directory", type=click.Path(exists=True, file_okay=False, dir_okay=True)
)
def main(directory):
    trimbox_re = re.compile(
        rb"TrimBox\[(\d+\.*\d*) (\d+\.*\d*) (\d+\.*\d*) (\d+\.*\d*)\]"
    )
    for item in Path(directory).iterdir():
        if str(item).lower().endswith(".pdf"):
            with open(item, "rb") as pdf_file:
                for line in pdf_file:
                    if matches := trimbox_re.search(line):
                        a, b, c, d = (float(x) for x in matches.groups())
                        width = int((c - a) / PT_TO_MM)
                        height = int((d - b) / PT_TO_MM)
                        suffix = f"{width}x{height}mm"
                        if f"{width}x{height}mm" not in str(item):
                            LOG.info(f"Renaming {item}")
                            item.rename(
                                item.parent / f"{item.stem} {suffix}{item.suffix}"
                            )
                        else:
                            LOG.info(f"{item} already renamed.")
                        break


if __name__ == "__main__":
    main()
