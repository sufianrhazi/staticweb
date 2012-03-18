#!/usr/bin/env python

import json
import jinja2
import sys
import os

class MyLoader(jinja2.BaseLoader):
    def __init__(self, path):
        self.path = path

    def get_source(self, env, template):
        path = os.path.join(self.path, template)
        try:
            with file(path, 'r') as f:
                return f.read().decode('utf-8'), path, True
        except IOError:
            raise jinja2.TemplateNotFound(path)


def main(varpath, inpath):
    loader = MyLoader(os.path.dirname(inpath))
    env = jinja2.Environment(loader=loader)

    env.globals['myrange'] = range

    outpath = inpath.rsplit('.', 1)[0] + '.html'
    with open(varpath, 'r') as f:
        options = json.loads(f.read())

    template = env.get_template(os.path.basename(inpath))

    data = template.render(**options)
    print "Writing to %s..." % outpath
    with open(outpath, 'w') as f:
        f.write(data)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage %s <variables.json> <input.tml>" % sys.argv[0]
        print "Writes to 'input.html'"
    else:
        main(sys.argv[1], sys.argv[2])
