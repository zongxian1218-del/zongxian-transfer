import re

with open('src/swiftdrop/cli.py', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    "棕仙的传输软件 命令行：参数解析与子命令。": "Zongxian Transfer CLI: argument parsing and subcommands.",
    "棕仙的传输软件 1.0 —— 朋友间大文件传输 + 文件夹同步（纯标准库；源码包名 swiftdrop）": "Zongxian Transfer 1.0 - File transfer + folder sync (pure standard lib; package name swiftdrop)",
    "进度一律用「单行原地刷新」的进度条 + MB/s + ETA，不刷屏。": "Progress is displayed using a single-line in-place refresh progress bar + MB/s + ETA, without spamming the screen.",
    "打开图形界面": "Open Graphical UI",
    "列出发现的设备": "List discovered devices",
    "异地组网：识别 Radmin/Tailscale 等虚拟局域网地址": "Remote virtual LAN: Identify Radmin/Tailscale etc. virtual LAN addresses",
    "进入接收模式": "Enter receive mode",
    "使用说明": "Usage Guide",
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open('src/swiftdrop/cli.py', 'w', encoding='utf-8') as f:
    f.write(text)
