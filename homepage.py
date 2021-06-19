"""Script to create index, date and tag pages.
"""
from jinja2 import Environment
from jinja2 import FileSystemLoader

from create_sphinx_source import utf8_open

jinja_env = Environment(loader=FileSystemLoader("_templates"))


def conditional_write(filename, new):
    old = open(filename, "r").read()
    if new != old:
        utf8_open(filename, "w").write(new)
        print(".")


def pathto(*args):
    """Mock of sphinx' pathto() just for the homepage.
    Otherwise we cannot re-use our sphinx templates.
    """
    return ""


class Homepage(object):
    """Represents the homepage"""

    template = jinja_env.get_template("homepage.html")
    outfile = "_build/dirhtml/index.html"

    def __init__(self):
        pass

    def write(self):
        """Write out homepage"""
        conditional_write(self.outfile, self.content)

    @property
    def content(self):
        """Return rendered template, filled with content"""
        return self.template.render(weblogsnippet=self.weblogsnippet, pathto=pathto)

    @property
    def weblogsnippet(self):
        return utf8_open("_build/dirhtml/snippet.html").read()


def main():
    # homepage = Homepage()
    # homepage.write()
    import os
    # import re

    # old = open(os.path.join("_build", "dirhtml", "articles", "index.html")).read()
    # new = re.sub(r'href="([^/])', 'href="articles/\\1', old)
    # open(os.path.join("_build", "dirhtml", "index.html"), "w").write(new)

    index = open(os.path.join("_build", "dirhtml", "index.html")).read().splitlines()
    snippet = (
        open(os.path.join("_build", "dirhtml", "snippet.html")).read().splitlines()
    )

    with open(os.path.join("_build", "dirhtml", "index.html"), "w") as f:
        for line in index:
            if "Post" not in line:
                f.write(line + "\n")
            else:
                f.write("\n".join(snippet) + "\n")


main()
