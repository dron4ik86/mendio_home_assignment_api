import glob
import os
import importlib.util


def import_steps_modules(directory):
    """
    Import all Python modules found in the specified directory's subdirectories.
    """
    for path in glob.glob(directory + '/**/*.py', recursive=True):
        name = os.path.splitext(os.path.basename(path))[0]
        if name != '__init__':
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)


import_steps_modules(os.path.dirname(__file__))
