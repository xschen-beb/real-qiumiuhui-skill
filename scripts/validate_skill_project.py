from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "SKILL.md",
    "agents/openai.yaml",
    "prompts/core.md",
    "prompts/guardrails.md",
    "prompts/modes/post-match.md",
    "prompts/modes/live-chat.md",
    "prompts/modes/fan-qa.md",
    "prompts/modes/debate.md",
    "references/source-map.md",
    "references/style-profile.md",
    "references/phrasebook.md",
    "references/topic-priors.md",
    "references/stance-rules.md",
    "examples/post-match.md",
    "examples/debate.md",
    "examples/live-chat.md",
]

TEXT_REQUIREMENTS = {
    "README.md": ["风格启发", "同人整理", "非官方关联", "按模式分类（主）", "按场景快速索引（补充）"],
    "SKILL.md": ["适用场景", "prompts/core.md", "prompts/guardrails.md", "真老师"],
    "examples/post-match.md": ["## 输入", "## 输出"],
    "examples/debate.md": ["## 输入", "## 输出"],
    "examples/live-chat.md": ["## 输入", "## 输出"],
}

missing = [path for path in REQUIRED if not (ROOT / path).exists()]
if missing:
    for path in missing:
        print(f"MISSING: {path}")
    sys.exit(1)

for relative_path, required_snippets in TEXT_REQUIREMENTS.items():
    content = (ROOT / relative_path).read_text(encoding="utf-8")
    for snippet in required_snippets:
        if snippet not in content:
            print(f"MISSING TEXT: {relative_path} -> {snippet}")
            sys.exit(1)

print("技能包结构校验通过")
