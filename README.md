# :coin: Earn-SEU-Points-Daily

- [:coin: Earn-SEU-Points-Daily](#coin-earn-seu-points-daily)
  - [项目简介](#项目简介)
  - [免责声明](#免责声明)
  - [安全性](#安全性)
  - [使用方法](#使用方法)
    - [1. Fork 本项目](#1-fork-本项目)
    - [2. 配置变量](#2-配置变量)

## 项目简介

本项目使用 GitHub Actions 在线部署，每日自动运行脚本，完成东南大学-东大信息化 App 中的东豆奖励任务（如启动应用、浏览资讯等），赚取东豆。

## 免责声明

1. 本项目仅用于学习交流，不得用于任何违反法律法规、侵犯他人权益的行为；
2. 由于使用本项目造成的任何后果，均由使用者自行承担；
3. 本项目不提供任何形式的保证，亦不承担任何责任。

## 安全性

本项目使用 GitHub Actions 在线部署，您的一卡通号和密码将存储在 GitHub 服务器上，除 GitHub 服务器导致的泄露外，其他人无法查看。

## 使用方法

在此只提供 GitHub Actions 部署方法，本地使用较为简单，可自行修改。

### 1. Fork 本项目

Why？——只有在您自己的仓库中，才有权进行后续 Actions 的相关配置。

点击右上角的 :trident:Fork 按钮，或直接[点击此处](https://github.com/Golevka2001/Earn-SEU-Points-Daily/fork)创建您自己的 Fork 仓库。

点击页面中的 `Create fork` 按钮，即可完成。

### 2. 配置变量

进入您刚创建的 Fork 仓库，点击上方的 `Settings` 选项卡，在左侧菜单中找到 `Secrets and variables`，点击下拉菜单中的 `Actions`。

点击页面中的 `New repository secret` 按钮，依次创建以下变量：

|    Name    |  Secret  |
| :--------: | :------: |
| `USERNAME` | 一卡通号 |
| `PASSWORD` |   密码   |
