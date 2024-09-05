from importlib import resources

def get_file(package, file_name):
        with resources.as_file(resources.files(package).joinpath(file_name)) as fixture:
            return open(fixture, "r")