# WSL + VS Code + Git 最小练习项目

这是一个最小 Python 项目，适合练习：

- 在 Windows 上用 VS Code + WSL 写 Linux 程序
- 在 WSL 里运行 Python 程序
- 用 Git 模拟多人分别开发不同模块
- 把项目或可执行文件带到 Linux 服务器上运行

## 项目结构

```text
.
├── README.md
├── Dockerfile
├── requirements.txt
├── app
│   ├── __init__.py
│   ├── banner.py
│   ├── calc.py
│   └── hello.py
├── main.py
└── systemd
    └── demo-app.service
```

## 你会学到什么

这个程序会：

1. 打印欢迎语
2. 打印一个简单横幅
3. 计算两个整数的和

它被拆成了 3 个模块：

- `hello`：负责欢迎语
- `banner`：负责横幅输出
- `calc`：负责计算

这正适合练习“不同人改不同文件，然后合并”。

## 在 WSL 中运行

进入项目目录：

```bash
cd /mnt/d/Coding/WSLTest
```

确认 Python 可用：

```bash
python3 --version
```

运行：

```bash
python3 main.py
```

如果你想模拟“服务器常驻运行”模式，可以执行：

```bash
python3 main.py --loop --interval 5
```

停止时按 `Ctrl+C`。

如果你想创建虚拟环境，也可以这样：

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 main.py
```

## 在 VS Code 中打开

如果你已经安装好了：

- VS Code
- WSL
- VS Code 的 Remote - WSL 扩展

那么在 WSL 终端里执行：

```bash
code .
```

这样 VS Code 会直接以 WSL 环境打开当前目录。你写代码、运行程序，都是在 Linux 环境里完成的。

## 依赖文件

这个项目带了一个最小 [requirements.txt](/mnt/d/Coding/WSLTest/requirements.txt:1)。

当前它没有第三方依赖，但保留这个文件是为了让你的部署流程固定下来：

```bash
python3 -m pip install -r requirements.txt
```

注意：当前这个文件没有第三方依赖，所以某些旧版 `pip` 会提示“没有要安装的包”。这不影响程序运行。

## Docker 最小用法

Docker 可以先简单理解成：把“Python 运行环境 + 你的代码”一起装进一个镜像里。

这样做的好处是：

- 本地和服务器运行环境更一致
- 少一些“这台机器能跑，那台不能跑”的问题
- 部署时只需要 `docker run`

这个项目已经提供了：

- [Dockerfile](/mnt/d/Coding/WSLTest/Dockerfile:1)
- [.dockerignore](/mnt/d/Coding/WSLTest/.dockerignore:1)

### 1. 先安装 Docker

在 Windows 学习时，通常安装：

- Docker Desktop

然后开启：

- WSL 2 integration

如果是在 Linux 服务器上，则通常安装 Docker Engine。

### 2. 构建镜像

在项目目录执行：

```bash
docker build -t wsltest-python-demo .
```

### 3. 运行一次性模式

```bash
docker run --rm wsltest-python-demo
```

你应该看到和 `python3 main.py` 类似的输出。

### 4. 运行常驻模式

```bash
docker run --name wsltest-loop wsltest-python-demo python main.py --loop --interval 5
```

这时容器会持续运行。

### 5. 查看日志

```bash
docker logs -f wsltest-loop
```

### 6. 停止并删除容器

```bash
docker stop wsltest-loop
docker rm wsltest-loop
```

## Docker 和 systemd 的关系

这两个不是一回事：

- Docker：解决“程序放在什么运行环境里”
- systemd：解决“程序在 Linux 上如何作为服务被托管”

常见情况有两种：

- 不用 Docker，直接 `python3` 或 `venv` + `systemd`
- 用 Docker，再由 Docker 去运行容器

对你现在这个阶段，先学会 Docker 的 `build/run/logs` 就够了，不用急着把 Docker 和 `systemd` 叠在一起。

## Git 最小练习流程

这个仓库很适合你自己练下面这套流程。

另外，仓库里已经预置了两个示例分支，你可以直接观察：

- `feature/hello-update`
- `feature/calc-update`

### 1. 查看当前分支

```bash
git branch
```

### 2. 从 `main` 切出一个功能分支

比如你扮演“开发者 A”，修改欢迎语模块：

```bash
git switch -c feature/hello-update
```

编辑 `app/hello.py` 后提交：

```bash
git add app/hello.py
git commit -m "update hello message"
```

### 3. 回到 `main` 再切另一个分支

比如你扮演“开发者 B”，修改计算模块：

```bash
git switch main
git switch -c feature/calc-update
```

编辑 `app/calc.py` 后提交：

```bash
git add app/calc.py
git commit -m "improve calc module"
```

### 4. 合并两个分支

回到主分支：

```bash
git switch main
```

先合并一个分支：

```bash
git merge feature/hello-update
```

再合并另一个分支：

```bash
git merge feature/calc-update
```

如果两个人改的是不同文件，通常会自动合并成功。

## 观察提交图

```bash
git log --oneline --graph --all
```

这个命令很适合用来理解多人协作的分支结构。

## 带到 Linux 服务器上

你有两种常见方式：

### 方式 1：传源码到服务器再运行

适合服务器有 Python 3。

本地打包：

```bash
tar czf demo-source.tar.gz .
```

传到服务器：

```bash
scp demo-source.tar.gz user@your-server:/home/user/
```

服务器上解压、运行：

```bash
tar xzf demo-source.tar.gz
cd WSLTest
python3 -m pip install -r requirements.txt
python3 main.py
```

更稳妥的学习路径就是直接传源码，因为 Python 项目通常就是这样部署和运行的。

如果服务器装了 Docker，你也可以直接：

```bash
docker build -t wsltest-python-demo .
docker run --rm wsltest-python-demo
```

## 用 systemd 管理运行

如果你的程序只是临时测试，直接：

```bash
python3 main.py
```

如果你要在服务器上长期后台运行，才考虑 `systemd`。

这个仓库已经提供了一个模板文件：

- [systemd/demo-app.service](/mnt/d/Coding/WSLTest/systemd/demo-app.service:1)

使用前你需要先把里面这两个地方改成服务器上的真实路径和用户名：

- `YOUR_LINUX_USER`
- `/home/YOUR_LINUX_USER/WSLTest`

### 服务器操作步骤

先把项目拉到服务器，例如：

```bash
git clone <your-repo-url>
cd WSLTest
python3 -m pip install -r requirements.txt
```

先手工验证常驻模式能跑：

```bash
python3 main.py --loop --interval 5
```

确认没问题后，把 service 文件复制到系统目录：

```bash
sudo cp systemd/demo-app.service /etc/systemd/system/demo-app.service
```

重新加载配置并启动：

```bash
sudo systemctl daemon-reload
sudo systemctl enable demo-app
sudo systemctl start demo-app
```

查看状态：

```bash
sudo systemctl status demo-app
```

查看日志：

```bash
sudo journalctl -u demo-app -f
```

停止服务：

```bash
sudo systemctl stop demo-app
```

这套方式的重点不是“替代 Git”或“替代 Python”，而是让 Linux 负责：

- 后台启动
- 崩溃自动重启
- 开机自动运行
- 日志集中查看

## 建议你现在就练

按这个顺序最合适：

1. `python3 main.py`
2. `git log --oneline --graph --all`
3. `git branch`
4. 自己新建两个分支，分别改 `app/hello.py` 和 `app/calc.py`
5. 试一次 `python3 main.py --loop --interval 5`
6. 试一次 `docker build -t wsltest-python-demo .`
7. 合并回 `main`

## 常见命令速查

```bash
python3 main.py
python3 main.py --loop --interval 5
python3 -m pip install -r requirements.txt
docker build -t wsltest-python-demo .
docker run --rm wsltest-python-demo
docker run --name wsltest-loop wsltest-python-demo python main.py --loop --interval 5
docker logs -f wsltest-loop
docker stop wsltest-loop
docker rm wsltest-loop
git status
git branch
git switch main
git switch -c feature/xxx
git add .
git commit -m "your message"
git merge feature/xxx
git log --oneline --graph --all
sudo systemctl status demo-app
sudo journalctl -u demo-app -f
```
