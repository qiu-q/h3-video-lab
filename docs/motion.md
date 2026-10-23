# 动作参考与动作迁移

## 我们目前真正做过什么

十套换装舞蹈是“服装参考图 + 首尾引导 + 文字描述动作”，动作由 H3 重新生成。没有输入原始舞蹈视频、没有提取骨架、没有逐帧迁移，也没有证明与原视频严格卡点一致。

## 三条路线

| 路线 | 输入与控制 | 状态 |
|---|---|---|
| 提示词重新生成 | 成年角色图、动作文字、首尾图 | 已实跑；适合小幅比心、摆肩等 |
| H3 R2V 视频参考 | 人物图 + 动作参考短片，明确两者职责 | 本机存在 ReferenceToVideo 节点；未实跑 |
| 姿态/深度等控制 | 提取动作序列，再配合兼容控制模型与工作流 | 方案研究；当前仓库没有验证兼容性与成片 |

## R2V 的下一次测试计划

1. 准备一个主体清晰、遮挡少、镜头稳定的成年角色图和 3–5 秒动作参考。
2. 将参考视频转成恒定 24fps，单独确认参考音轨是否需要；图像批次本身不携带音轨。
3. 使用 `MiniMaxH3ReferenceToVideo` 和 **ref2va** 模型，不能直接把现有 **fl2va** 文件改个名当作 R2V 权重。先检查所需权重是否齐全，本次未安装或运行这一方案。
4. 用人物图作为 `<Picture 1>`，动作视频作为 `<Video 1>`，提示词明确“保留人物图的外观和服装，参考视频只负责动作节奏”。
5. 将画幅从低分辨率开始，固定种子；保留参考输入、提示词、完整参数、执行耗时和成片。
6. 逐帧核对手势顺序、步伐、转身、遮挡恢复、人物与服装稳定性，另核对音乐节拍。

参考驱动属于生成式跟随，不能承诺逐帧精确复制。强求原动作一致时，应先建立动作误差与节拍误差的验收标准，再决定是否转到姿态控制路线。

### 待测提示词示例

```text
The adult character identity, clothing and appearance come from <Picture 1>.
Use <Video 1> as the reference for the sequence and timing of body gestures.
Keep a fixed full-body camera, stable background and consistent clothing.
Follow the motion while preserving the adult character's identity.
No extra people, no scene cut, no outfit changes, no text.
```

以上不是已成功迁移的演示。首尾 AddGuide 也不能代替完整舞蹈的骨架约束。
