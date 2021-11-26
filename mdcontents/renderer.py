from mistune.renderers import BaseRenderer


class JsonRenderer(BaseRenderer):
    NAME = "json"

    def text(self, text):
        return {"text": text}

    def link(self, link, children=None, title=None):
        if isinstance(children, str):
            children = [{"type": "text", "text": children}]
        return {
            "type": "link",
            "link": link,
            "children": children,
            "title": title,
        }

    def image(self, src, alt="", title=None):
        return {"image", src}

    def codespan(self, text):
        return {"codespan": text}

    def linebreak(self):
        return None

    def inline_html(self, html):
        return {"inline_html", html}

    def heading(self, children, level):
        return {"heading": {"children": children, "level": level}}

    def newline(self):
        return None

    def thematic_break(self):
        return None

    def block_code(self, children, info=None):
        return {
            "block_code": {
                "text": children,
                # "info": info
            }
        }

    def block_html(self, children):
        return {"block_html": children}

    def list(self, children, ordered, level, start=None):
        token = {
            "list": children,
        }
        if start is not None:
            token["start"] = start
        return token

    def list_item(self, children, level):
        if type(children) == list and len(children) == 1:
            return {"list_item": children[0]}
        return {"list_item": children}

    def block_text(self, text):
        if type(text) == list and len(text) == 1:
            return text[0]
        return {"block_text": text}

    def _create_default_method(self, name):
        def __ast(children):
            return {name: children}

        return __ast

    def _get_method(self, name):
        try:
            return super(JsonRenderer, self)._get_method(name)
        except AttributeError:
            return self._create_default_method(name)

    def finalize(self, data):
        return list(filter(None, data))
