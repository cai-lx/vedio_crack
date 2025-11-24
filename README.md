# VIP 追剧神器（简易版）

这是一个小型的桌面 Python 程序（Tkinter），用于将用户输入的视频链接通过第三方解析器打开到默认浏览器。

主要文件
- `vedio_crack.py`：主程序（GUI）。
- `tests/test_build_parser_url.py`：针对 URL 拼接/校验的 pytest 测试。
- `requirements.txt`：测试所需依赖（`pytest`）。
- `.github/workflows/pytest.yml`：GitHub Actions CI，用于运行测试。
- `.github/copilot-instructions.md`：为 AI 代理准备的简明说明。

先决条件
- Python 3.10+ 安装在系统上。
- Windows 用户建议使用 PowerShell（示例使用 PowerShell 命令）。

在本地运行（PowerShell）
```powershell
cd "d:\\desk\\ll\\宝贝宝贝"
python "vedio_crack.py"
```

运行测试
```powershell
cd "d:\\desk\\ll\\宝贝宝贝"
# 安装依赖（可选在虚拟环境中）
python -m pip install --user -r requirements.txt
# 运行 pytest
python -m pytest -q
```

关于更改
- 已将原始文件名 `vedio crack.py` 规范化为 `vedio_crack.py`，方便导入与测试。
- 已抽取 `build_parser_url(video_url: str)` 作为纯函数并对其添加了单元测试（测试文件见 `tests/`）。
- UI 已从绝对定位 (`place()`) 改为 `grid()` 布局，窗口设置为不可调整大小。

注意事项
- 解析器地址使用第三方服务 `https://jx.xmflv.com/?url=`；这是运行时集成点，测试不直接访问该服务。
- 文件包含中文字符，保存为 UTF-8 编码以避免路径/编码问题。

CI
- 推送到 GitHub 后，`.github/workflows/pytest.yml` 会在每次 push/PR 时运行 pytest（使用 Python 3.10/3.11）。

如果你想让我把 README 翻译为英文、或把 README 中的运行路径改为相对路径（例如 `python -m vedio_crack`），告诉我下一步偏好。