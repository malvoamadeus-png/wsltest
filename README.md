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
├── app
│   ├── __init__.py
│   ├── banner.py
│   ├── calc.py
│   └── hello.py
└── main.py
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
python3 main.py
```

更稳妥的学习路径就是直接传源码，因为 Python 项目通常就是这样部署和运行的。

## 建议你现在就练

按这个顺序最合适：

1. `python3 main.py`
2. `git log --oneline --graph --all`
3. `git branch`
4. 自己新建两个分支，分别改 `app/hello.py` 和 `app/calc.py`
5. 合并回 `main`

## 常见命令速查

```bash
python3 main.py
git status
git branch
git switch main
git switch -c feature/xxx
git add .
git commit -m "your message"
git merge feature/xxx
git log --oneline --graph --all
```
