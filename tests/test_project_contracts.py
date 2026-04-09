from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    ROOT / "README.md",
    ROOT / "SKILL.md",
    ROOT / "agents" / "openai.yaml",
    ROOT / "prompts" / "core.md",
    ROOT / "prompts" / "guardrails.md",
    ROOT / "prompts" / "modes" / "post-match.md",
    ROOT / "prompts" / "modes" / "live-chat.md",
    ROOT / "prompts" / "modes" / "fan-qa.md",
    ROOT / "prompts" / "modes" / "debate.md",
    ROOT / "references" / "source-map.md",
    ROOT / "references" / "style-profile.md",
    ROOT / "references" / "phrasebook.md",
    ROOT / "references" / "topic-priors.md",
    ROOT / "references" / "stance-rules.md",
    ROOT / "examples" / "post-match.md",
    ROOT / "examples" / "debate.md",
    ROOT / "examples" / "live-chat.md",
]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class ProjectContractsTest(unittest.TestCase):
    def test_required_paths_exist(self):
        missing = [str(path.relative_to(ROOT)) for path in REQUIRED_PATHS if not path.exists()]
        self.assertEqual(missing, [])


class ReferenceContractsTest(unittest.TestCase):
    def test_source_map_records_public_sources_and_confidence_split(self):
        source_map = read_text("references/source-map.md")
        for needle in [
            "## 公开来源",
            "## 可直接观察到的信号",
            "## 基于公开信号的推断",
            "bilibili.com",
            "newrank.cn",
            "zeroroku.com",
        ]:
            self.assertIn(needle, source_map)

    def test_style_and_stance_docs_cover_required_topics(self):
        source_map = read_text("references/source-map.md")
        style_profile = read_text("references/style-profile.md")
        phrasebook = read_text("references/phrasebook.md")
        topic_priors = read_text("references/topic-priors.md")
        stance_rules = read_text("references/stance-rules.md")

        for needle in [
            "句子节奏",
            "先判后说的起手",
            "球迷对线升级",
        ]:
            self.assertIn(needle, style_profile)

        for needle in [
            "高置信表达",
            "中置信表达",
            "禁用表达",
            "外号使用",
            "大黄",
            "小小",
            "骆驼",
            "罗尾巴",
        ]:
            self.assertIn(needle, phrasebook)

        for needle in [
            "武术队",
            "大黄",
            "骆驼",
            "罗尾巴",
            "小小",
        ]:
            self.assertIn(needle, source_map)

        for needle in [
            "沙特联赛",
            "皇马",
            "C罗",
            "梅西",
            "金球奖",
            "曼城",
            "利物浦",
            "阿森纳",
            "马竞",
            "巴黎",
            "拜仁",
            "国米",
        ]:
            self.assertIn(needle, topic_priors)

        for needle in [
            "沙特联赛",
            "皇马",
            "C罗",
            "梅西",
            "金球奖",
            "巴萨",
            "曼城",
            "利物浦",
            "阿森纳",
            "马竞",
            "巴黎",
            "拜仁",
            "国米",
        ]:
            self.assertIn(needle, stance_rules)


class PromptContractsTest(unittest.TestCase):
    def test_core_prompt_contains_shared_output_formula(self):
        core_prompt = read_text("prompts/core.md")
        for needle in [
            "先下结论",
            "再摆依据",
            "最后收一句",
            "真老师",
            "不得声称自己就是现实世界里已验证的创作者",
        ]:
            self.assertIn(needle, core_prompt)

    def test_mode_prompts_cover_all_four_modes(self):
        expected_markers = {
            "prompts/modes/post-match.md": ["比赛主线", "决定性片段"],
            "prompts/modes/live-chat.md": ["短句连发", "弹幕节奏"],
            "prompts/modes/fan-qa.md": ["先回答问题", "不装看过"],
            "prompts/modes/debate.md": ["高冲突议题", "外号使用", "事实和立场分层"],
            "prompts/guardrails.md": ["不得冒充现实认证身份", "不得虚构内幕消息"],
        }

        for relative_path, markers in expected_markers.items():
            content = read_text(relative_path)
            for marker in markers:
                self.assertIn(marker, content)


class EntrypointContractsTest(unittest.TestCase):
    def test_skill_frontmatter_and_disclaimer_are_present(self):
        skill = read_text("SKILL.md")
        for needle in [
            "---",
            "name:",
            "description:",
            "风格启发",
            "非官方关联",
            "prompts/core.md",
            "prompts/guardrails.md",
            "真老师",
        ]:
            self.assertIn(needle, skill)

    def test_openai_metadata_contains_listing_fields(self):
        metadata = read_text("agents/openai.yaml")
        for needle in [
            "display_name:",
            "short_description:",
            "default_prompt:",
        ]:
            self.assertIn(needle, metadata)


if __name__ == "__main__":
    unittest.main()
