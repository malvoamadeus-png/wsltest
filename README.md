# WSL + VS Code + Git 最小练习项目

这是一个最小 C 项目，适合练习：

- 在 Windows 上用 VS Code + WSL 写 Linux 程序
- 在 WSL 里编译并运行
- 用 Git 模拟多人分别开发不同模块
- 把项目或可执行文件带到 Linux 服务器上运行

## 项目结构

```text
.
├── Makefile
├── README.md
├── include
│   ├── banner.h
│   ├── calc.h
│   └── hello.h
└── src
    ├── banner.c
    ├── calc.c
    ├── hello.c
    └── main.c
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

## 在 WSL 中编译运行

进入项目目录：

```bash
cd /mnt/d/Coding/WSLTest
```

如果你的 WSL 还是新环境，先安装编译工具：

```bash
sudo apt update
sudo apt install -y build-essential
```

编译：

```bash
make
```

运行：

```bash
./build/demo_app
```

清理：

```bash
make clean
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

这样 VS Code 会直接以 WSL 环境打开当前目录。你写代码、编译、跑程序，都是在 Linux 环境里完成的。

## Git 最小练习流程

这个仓库很适合你自己练下面这套流程。

### 1. 查看当前分支

```bash
git branch
```

### 2. 从 `main` 切出一个功能分支

比如你扮演“开发者 A”，修改欢迎语模块：

```bash
git switch -c feature/hello-update
```

编辑 `src/hello.c` 后提交：

```bash
git add src/hello.c
git commit -m "update hello message"
```

### 3. 回到 `main` 再切另一个分支

比如你扮演“开发者 B”，修改计算模块：

```bash
git switch main
git switch -c feature/calc-update
```

编辑 `src/calc.c` 后提交：

```bash
git add src/calc.c
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

### 方式 1：传源码到服务器再编译

适合服务器有 `gcc` 和 `make`。

本地打包：

```bash
tar czf demo-source.tar.gz .
```

传到服务器：

```bash
scp demo-source.tar.gz user@your-server:/home/user/
```

服务器上解压、编译、运行：

```bash
tar xzf demo-source.tar.gz
cd WSLTest
make
./build/demo_app
```

### 方式 2：在 WSL 里先编译，再传可执行文件

如果目标服务器和你的 WSL 环境都是常见 Linux x86_64，并且兼容库没问题，可以直接传：

```bash
scp build/demo_app user@your-server:/home/user/
```

服务器上运行：

```bash
chmod +x demo_app
./demo_app
```

更稳妥的学习路径还是“传源码到服务器再编译”，因为兼容性问题更少。

## 建议你现在就练

按这个顺序最合适：

1. `make`
2. `./build/demo_app`
3. `git log --oneline --graph --all`
4. 自己新建两个分支，分别改 `src/hello.c` 和 `src/calc.c`
5. 合并回 `main`

## 常见命令速查

```bash
make
./build/demo_app
git status
git branch
git switch main
git switch -c feature/xxx
git add .
git commit -m "your message"
git merge feature/xxx
git log --oneline --graph --all
```
