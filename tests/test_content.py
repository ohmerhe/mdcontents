from mdcontents import json as json_content
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

jsonObject = json_content(markdown_string)
print(json.dumps(jsonObject))
