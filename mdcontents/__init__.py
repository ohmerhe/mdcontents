from mistune.plugins import PLUGINS
from mistune.markdown import Markdown
from mdcontents.renderer import JsonRenderer


def create_markdown(renderer=JsonRenderer(), plugins=None):

    if plugins:
        _plugins = []
        for p in plugins:
            if isinstance(p, str):
                _plugins.append(PLUGINS[p])
            else:
                _plugins.append(p)
        plugins = _plugins
    return Markdown(renderer=renderer, plugins=plugins)


json = create_markdown(plugins=['strikethrough', 'footnotes', 'table'])


__all__ = [
    'JsonRenderer', 'json', 'create_markdown'
]