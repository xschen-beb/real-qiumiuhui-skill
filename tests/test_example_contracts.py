from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class ExampleContractsTest(unittest.TestCase):
    def test_readme_contains_disclaimer_and_install_sections(self):
        readme = read_text("README.md")
        for needle in [
            "风格启发",
            "同人整理",
            "非官方关联",
            "## 安装",
            "## 使用方式",
            "## 示例效果",
            "### 按模式分类（主）",
            "### 按场景快速索引（补充）",
            "## 仓库结构",
        ]:
            self.assertIn(needle, readme)

    def test_examples_cover_all_modes(self):
        expected_markers = {
            "examples/post-match.md": ["## 输入", "## 输出", "大黄", "武术队", "真老师"],
            "examples/debate.md": ["## 输入", "## 输出", "小小", "沙特", "骆驼", "罗尾巴"],
            "examples/live-chat.md": ["## 输入", "## 输出", "直播间短句", "真难绷"],
        }

        for relative_path, markers in expected_markers.items():
            content = read_text(relative_path)
            for marker in markers:
                self.assertIn(marker, content)
            self.assertNotIn("我是现实世界里已验证的真实球迷汇账号本人", content)


if __name__ == "__main__":
    unittest.main()
