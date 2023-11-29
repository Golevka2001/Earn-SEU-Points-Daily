# :coin: Earn-SEU-Points-Daily

[![Earn points daily](https://github.com/Golevka2001/Earn-SEU-Points_Daily/actions/workflows/earn_points_daily.yml/badge.svg)](https://github.com/Golevka2001/Earn-SEU-Points_Daily/actions/workflows/earn_points_daily.yml)

- [:coin: Earn-SEU-Points-Daily](#coin-earn-seu-points-daily)
  - [:page_facing_up: 项目简介](#page_facing_up-项目简介)
  - [:loudspeaker: 免责声明](#loudspeaker-免责声明)
  - [:lock: 安全性](#lock-安全性)
  - [:joystick: 使用方法](#joystick-使用方法)
    - [1. Fork 本项目](#1-fork-本项目)
    - [2. 配置变量](#2-配置变量)
    - [3. 测试工作流](#3-测试工作流)
    - [4. 修改运行时间【可选】](#4-修改运行时间可选)

## :page_facing_up: 项目简介

本项目可以在线自动完成 东南大学 - 东大信息化 App 中的东豆奖励任务（如启动应用、浏览资讯等），赚取东豆。项目支持使用 GitHub Actions 在线部署，每日定时自动运行脚本。

东豆可用于兑换礼品，详见[微信公众号推送](https://mp.weixin.qq.com/s/5L_EalxGOxjfl8w_xCN5Dg)。

## :money_with_wings: 获取途径与奖励上限

|   获取途径   | 单次奖励 |    奖励上限    |
| :----------: | :------: | :------------: |
|   打开 APP   |    5     |    15 / 日     |
|   登录 APP   |    5     | （未成功触发） |
| 浏览资讯文章 |    10    |    50 / 周     |
|  打开轻应用  |    10    |    50 / 周     |

一周总奖励上限：`15 * 7 + 50 + 50 = 205`

_:warning: 注：本项目只负责代替手动点击，是否达到上限的判断和增加余额的操作由服务端处理。_

## :loudspeaker: 免责声明

1. 本项目仅用于学习交流，不得用于任何违反法律法规、侵犯他人权益的行为；
2. 由于使用本项目造成的任何后果，均由使用者自行承担；
3. 本项目不提供任何形式的保证，亦不承担任何责任。

## :lock: 安全性

本项目使用 GitHub Actions 在线部署，您的一卡通号和密码将存储在 GitHub 服务器上，除 GitHub 服务器导致的泄露外，其他人无法查看。

可以[点击这里](https://github.com/Golevka2001/Earn-SEU-Points_Daily/actions/workflows/earn_points_daily.yml)查看我个人使用 GitHub Actions 的运行日志，查看是否存在隐私信息泄露等问题。

## :joystick: 使用方法

在此只提供 GitHub Actions 部署方法，本地使用较为简单，可自行修改。

### 1. Fork 本项目

Why？——只有在您自己的仓库中，才有权进行后续 Actions 的相关配置。

点击右上角的 :trident:`Fork` 按钮，或直接[点击此处](https://github.com/Golevka2001/Earn-SEU-Points-Daily/fork)创建您自己的 Fork 仓库。

点击页面中的 `Create fork` 按钮，即可完成。

### 2. 配置变量

进入您刚创建的 Fork 仓库，点击上方的 :gear:`Settings` 选项卡，在左侧菜单中找到 `Secrets and variables`，点击下拉菜单中的 `Actions`。

点击页面中的 `New repository secret` 按钮，依次创建以下变量：

|    Name    |      Secret      |
| :--------: | :--------------: |
| `USERNAME` | 填入您的一卡通号 |
| `PASSWORD` |   填入您的密码   |

_:warning: 注：关于隐私信息的安全性已在[上文](#安全性)中进行了说明，如需了解更多内容请参考[GitHub 官方文档](https://docs.github.com/en/actions/reference/encrypted-secrets)。_

### 3. 测试工作流

为检查变量配置是否正确/脚本是否还可用，建议先手动运行一次 Actions。

点击上方的 :play_or_pause_button:`Actions` 选项卡，点击左侧菜单中的 `Earn points daily`，点击页面中的 `Run workflow` 按钮，随后脚本将开始运行，您可以在日志中的 **Earn points** 部分查看运行情况。

若日志最后出现 **东豆余额：xxx -> xxx**，则表明脚本运行成功，退出即可，后续将由 GitHub Actions 按照配置的定时任务每日自动运行。

### 4. 修改运行时间【可选】

默认情况下，脚本将于每日 9:11 运行，您可以根据自己的需求修改运行时间。修改 [earn_points_daily.yml](.github/workflows/earn_points_daily.yml) 中的 `cron` 字段即可。

注意事项与建议：

- 使用 UTC 时间；
- 尽量避开整点（使用高峰），而选择相对随意的时间；
- 由于 GitHub Actions 需要分配资源以及配置环境与依赖，所以运行时间有延迟是正常的。
