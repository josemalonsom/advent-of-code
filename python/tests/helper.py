import importlib.resources

def get_file(package, file_name):
        with importlib.resources.as_file(importlib.resources.files(package).joinpath(file_name)) as fixture:
            return open(fixture, "r")