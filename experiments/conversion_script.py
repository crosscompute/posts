# Write a script that converts a.md to html

# from jinja2 import Template
from configparser import ConfigParser
from jinja2 import Environment
from jinja2 import FileSystemLoader
from markdown import markdown
from sys import argv


# print('This is the argv:', sys.argv[0])
# print('Argument List:', str(sys.argv))
# text_file = open('./a.md')


# Load configuration file
# Render jinja2 template

# command_arg = str(sys.argv[1])
# print(command_arg)
template_path = argv[1]
configuration_path = argv[2]

configuration = ConfigParser()
configuration.read(configuration_path)
# print(configuration)
# print(dict(configuration))
value_by_key = dict(configuration['default'])

with open(template_path, 'rt') as template_file:
    template_text = template_file.read()

# template = Template(template_text)
template = Environment(loader=FileSystemLoader('.')).from_string(template_text)
page_text = template.render(**value_by_key)

page_html = markdown(page_text)
print(page_html)
