# FastAPI 学习实战仓库 🚀

零基础学习 Python Web 框架 —— FastAPI 的练习项目。

---

## 📖 项目介绍
本仓库用于记录 FastAPI 的学习过程，包含从基础接口编写到 Web 服务开发的所有代码示例。
FastAPI 是目前 Python 生态中**速度最快、易用性最高**的 Web 框架，支持自动生成 API 文档，是后端开发、接口开发的首选框架之一。

---

## 🛠️ 技术栈
- **编程语言**: Python 3.13
- **Web 框架**: FastAPI 0.115.12
- **ASGI 服务器**: Uvicorn
- **开发工具**: VS Code + Git

---

## 📁 项目结构
```text
fastapi_learn/
├── first_code.py       # 第一个 FastAPI 示例程序
│                       # 学习内容：fastapi 引入、3种服务启动方式、自动文档
├── README.md           # 项目说明文档（当前文件）
└── .gitignore          # Git 忽略配置（排除缓存、环境文件）

### ❓ 常见问题
1. **`src refspec main does not match any` 报错**
   原因：本地分支名与远程不匹配，本地为 `master`，远程为 `main`
   解决：`git branch -m master main` 重命名分支后重新推送

2. **Git 提交提示邮箱未配置**
   解决：执行 `git config --global user.name "你的GitHub用户名"` 和 `git config --global user.email "你的邮箱"`

3. **GitHub 看不到代码**
   原因：分支未切换，代码在 `master` 分支，需手动切换或统一分支名

### 📅 学习进度
- ✅ FastAPI 环境搭建与初始化（100%）
- ✅ 编写第一个 GET 接口（100%）
- ✅ 配置 Uvicorn 热重载（100%）
- ✅ GitHub 版本管理（100%）
- ⏳ 路径参数与查询参数（0%）
- ⏳ POST 请求与请求体处理（0%）
- ⏳ 数据校验与响应模型（0%）
- ⏳ 数据库集成（0%）

### 📌 作者信息
- GitHub: [@banana-Apple666](https://github.com/banana-Apple666)
- 项目用途：FastAPI 零基础学习记录
- 持续更新中...

### 📝 更新日志
- 2026-03-31: 完成第一个 FastAPI 接口，搭建项目仓库，完善 README
