import os.path
import jinja2
import markdown
import json

OUTPUT_PATH = 'catalogue'
TEMPLATES_PATH = 'catalogue/templates'

def _jinja_env():
    """create and return cubes jinja2 environment"""
    loader = jinja2.FileSystemLoader(TEMPLATES_PATH)
    env = jinja2.Environment(loader=loader)
    return env

def find_modules(modules_path):
    """Finds all modules in `modules_path` and returns a list of tuples
    `(path, info_file)` where `info_file` is full path to module's
    `module.json` file containing module information."""

    module_paths = []

    for (dirpath, dirnames, filenames) in os.walk(modules_path):
        for dirname in dirnames:
            module_dir = os.path.join(dirpath, dirname)
            info_file = os.path.join(module_dir, 'module.json')
            if os.path.exists(info_file):
                module_paths.append((module_dir, info_file))

    modules = []
    for (module_path, info_path) in module_paths:
        print "loading module info from %s" % info_path
        module = { "path": module_path }

        with open(info_path) as f:
            info = json.load(f)

        module.update(info)
        modules.append(module)

    return modules

def generate_index(modules):
    """Generates catalogue index `index.html` from list of `modules`"""

    print "generating module index page"

    env = _jinja_env()
    template = env.get_template("index.html")
    output = template.render(modules=modules)

    with open(os.path.join(OUTPUT_PATH, "index.html"), "w") as f:
        f.write(output)

def generate_modules(modules):
    """Generate module pages"""
    for module in modules:
        generate_module(module)

def generate_module(module):
    """Generate page for `module`"""

    print "generating page for module %s" % module["name"]

    env = _jinja_env()
    template = env.get_template("module.html")

    readme_path = os.path.join(module["path"], "README.md")
    if os.path.exists(readme_path):
        with open(readme_path) as f:
            text = f.read()

        module_text = markdown.markdown(text)
    else:
        module_text = ""

    files = []
    output = template.render(module=module,
                             module_text=module_text,
                             files=files)

    path = os.path.join(OUTPUT_PATH, "modules", module["name"]+".html")

    with open(path, "w") as f:
        f.write(output)

modules = find_modules("modules")
generate_index(modules)
generate_modules(modules)

