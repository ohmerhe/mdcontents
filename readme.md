## MDContents

MDContents target to parse markdown content to a structured data, and output with Json format.
MDContents is based on [mistune](https://github.com/lepture/mistune) project to parse markdown.

## Sample

### input

```
- Link: https://github.com
- AB Test key: https://github.com
- Feature Review Link : https://github.com
- Description:
  - do markdown parse
- Checklist:
  - [ ] PR Milestone
  - [x] PR Labels
- [ ] Is AB CleanUp : 
```

### output

```json
[
  {
    "list": [
      {
        "list_item": {
          "text": "Link: https://github.com"
        }
      },
      {
        "list_item": {
          "text": "AB Test key: https://github.com"
        }
      },
      {
        "list_item": {
          "text": "Feature Review Link : https://github.com"
        }
      },
      {
        "list_item": [
          {
            "text": "Description:"
          },
          {
            "list": [
              {
                "list_item": {
                  "text": "do markdown parse"
                }
              }
            ]
          }
        ]
      },
      {
        "list_item": [
          {
            "text": "Checklist:"
          },
          {
            "list": [
              {
                "list_item": {
                  "block_text": [
                    {
                      "text": "[ ]"
                    },
                    {
                      "text": " PR Milestone"
                    }
                  ]
                }
              },
              {
                "list_item": {
                  "block_text": [
                    {
                      "text": "[x]"
                    },
                    {
                      "text": " PR Labels"
                    }
                  ]
                }
              }
            ]
          }
        ]
      },
      {
        "list_item": {
          "block_text": [
            {
              "text": "[ ]"
            },
            {
              "text": " Is AB CleanUp :"
            }
          ]
        }
      }
    ]
  }
]
```
