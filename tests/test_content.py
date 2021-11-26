from mistune.markdown import Markdown
from mdcontents.renderer import JsonRenderer
from mistune.renderers import HTMLRenderer, AstRenderer
import json

markdown_string = """
- Link: https://github.com
- AB Test key: https://github.com
- Feature Review Link : https://github.com
- Description:
  - do markdown parse
- Checklist:
  - [ ] PR Milestone
  - [x] PR Labels
- [ ] Is AB CleanUp : 
"""

md = Markdown(renderer=JsonRenderer())
jsonObject = md(markdown_string)
print(json.dumps(jsonObject))
