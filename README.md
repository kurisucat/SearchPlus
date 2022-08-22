# SearchPlus

为应用程序根据网络环境切换更低延迟的搜索引擎，提供更好的体验。

## 用法

1. 克隆到本地
2. 安装所需运行库。

```bash
pip install -r requirements.txt
```

3. 运行程序

```bash
python main.py
```

4. 创建一个服务

```bash
cd /usr/lib/systemd/system #切换到服务路径
nano SearchPlus.service #创建一个服务
```

```bash
[Unit]
Description=SearchPlus
 
[Service]
Type=simple
ExecStart=/[clone 的路径]/main.py
Restart=always
RestartSec=5
StartLimitInterval=3
RestartPreventExitStatus=137
 
[Install]
WantedBy=multi-user.target
```

```bash
#^O [Return] ^X 来保存并退出 Nano 编辑器
systemctl enable SearchPlus #开机启动服务
service SearchPlus start #启动服务
```
