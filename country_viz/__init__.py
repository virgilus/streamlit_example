from os.path import join, dirname
from yaml import safe_load

# Loading config
# So all your modules have access to the same variables

config_path = join(dirname(dirname(__file__)), 'config.yaml')
with open(config_path, 'rb') as file:
    c = safe_load(file) # c is now a global dict config