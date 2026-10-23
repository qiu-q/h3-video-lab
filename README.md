# H3 Video Lab · 本地视频生成实践手册

记录我们在 RTX 5060 Ti 16GB 上使用 ComfyUI + MiniMax H3 的实际视频实验，说明参数怎样改变时长、画幅、首尾帧、动作与音频。更新：2026-10-23。

这是部署、工作流编排和后期制作项目，不是基础模型原创训练项目。参数以归档工作流与本机节点源码为准；未跑过的方案单独标注。

## 从这里开始

| 你想做什么 | 阅读入口 |
|---|---|
| 控制秒数、帧数、分辨率、步数 | [参数与时长](docs/parameters.md) |
| 固定开头、结尾，插入中间姿势 | [首尾帧与关键帧](docs/keyframes.md) |
| 复刻参考视频动作 | [动作参考与迁移方案](docs/motion.md) |
| 复用本机环境与模型 | [环境和复现步骤](docs/reproduction.md) |
| 看真实任务耗时与限制 | [运行记录](docs/runs.md) |
| 导入已有流程 | [工作流目录](workflows) |

## 已完成的内容

- 首帧图生视频：教室光影、噜噜情侣短剧、动漫手势舞。
- 同图首尾帧约束：成年模特十套造型，每段小幅手势动作，合成 30 秒合集。
- 通过串联 AddGuide 设置第 0 帧与第 72 帧，批量任务复用文本条件。
- 生成音轨、字幕/UI 后期叠加、替换配音、检查媒体实际帧数。
- **未完成验证**：R2V 动作迁移、骨架精确驱动、长片连续生成、高清画质基准。

## 实际成果

<video src="examples/ten-outfit-dance-30s.mp4" controls></video>

[下载/观看十套造型 30 秒视频](examples/ten-outfit-dance-30s.mp4) · [查看已有交互作品集](https://qiu-q.github.io/local-ai-run-archive/)

原始总档案：[local-ai-run-archive](https://github.com/qiu-q/local-ai-run-archive)。本仓库收录聚焦 H3 的文档、实际工作流和精简证据；完整输入、成片与其他实验保留在总档案。

## 项目经历摘要

基于 ComfyUI 原生 H3 节点搭建本地音视频生成流程，使用量化模型及 8 步 Turbo LoRA，在 16GB 显存设备完成首帧图生视频、双端关键帧约束及十套服装短片批量生成。通过 Python/API 编排任务，复用条件编码并完成裁帧、转场、字幕与音轨合成；以工作流、运行耗时及帧数核验记录保存可追溯成果。

## 文档依据

1. 本机 `comfy_extras/nodes_minimax_h3.py`，源码哈希见 [source-version.json](evidence/source-version.json)。本机安装目录没有 Git 元数据，无法确认提交号。
2. [ComfyUI 原生节点源码](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_minimax_h3.py)。
3. [Comfy-Org 原生工作流说明](https://github.com/Comfy-Org/docs/blob/main/tutorials/video/minimax/minimax-h3-native.mdx)。
4. [官方模型发行页](https://huggingface.co/Comfy-Org/MiniMax-H3)。

模型及上游素材遵循各自许可；本仓库没有模型权重。源码和工作流含本机历史路径，跨机器使用前按环境说明调整。参考图、姿势、声音约束不保证逐像素、逐帧或逐字一致。
