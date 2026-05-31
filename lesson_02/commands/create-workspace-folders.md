---
description: Tạo file và thư mục bên trong thư mục workspace hiện hành
agent: build
---

# Tạo thư mục
Tạo các thư mục sau (chỉ tạo mới nếu chưa có. Không được ghi đè thư mục đã có):

- `.opencode/`
- `.opencode/skills/`
- `.opencode/agents/`
- `input/`
- `output/`
- `scripts/`
- `tmp/`

# Tạo file opencode.json
- Tạo file `.opencode/opencode.json` có nội dung (UTF-8) như sau:
```
{
    "$schema": "https://opencode.ai/config.json",
    "permission": {
        "bash": {
            "rm *": "deny",
            "del *": "deny",
            "Remove-Item *": "deny"
        }
    }
}
```
- Chỉ tạo mới nếu file `opencode.json` chưa có, không được ghi đè file hiện tại.

# Tạo file AGENTS.md

- Tạo file `AGENTS.md` có nội dung (UTF-8) như sau:
```
# User profile
Tên:
Chức vụ:

# Agent profile
Tên:
Chức vụ:
```

- Chỉ tạo mới nếu file `AGENTS.md` chưa có, không được ghi đè file hiện tại.