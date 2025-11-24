# VIP 追剧神器（简易版）

这是一个小型的桌面 Python 程序，可以免费观看爱奇艺、腾讯、优酷的一些付费和VIP内容，操作简单，有手就行
食用方法：打开网页版的爱奇艺（或腾讯、优酷），找到想看的视频，播放后复制网址到GUI程序进行解析，即可观看

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

```
# 安装依赖（可选在虚拟环境中）
python -m pip install --user -r requirements.txt
# 运行 pytest
python -m pytest -q
```




CI
- 推送到 GitHub 后，`.github/workflows/pytest.yml` 会在每次 push/PR 时运行 pytest（使用 Python 3.10/3.11）。
