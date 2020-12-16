from docutils import nodes
from docutils.parsers.rst import Directive

class task_node(nodes.Structural, nodes.Element):
    pass

class TaskDirective(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}

    has_content = False
    add_index = True

    def run(self):
        sett = self.state.document.settings
        languge_code = sett.languge_code
        env = self.state.document.settings.env

        # get access to parameters in conf.py
        config = env.config

        # get access to directive options
        options = self.options

        node = None

        return [node]