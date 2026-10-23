# 环境与复现

## 已有环境

- Windows；RTX 5060 Ti 16GB；系统内存 16GB。
- ComfyUI 已安装于 `C:/Users/Administrator/Desktop/MiniMax-H3/ComfyUI`。
- 基础 Python：`C:/Users/Administrator/Desktop/MiniMax-H3/python/python.exe`。
- 已有模型：`minimax_h3_fl2va_pruned_w6a8.safetensors`、`qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`、`minimax_h3_video_vae_int8_convrot.safetensors`、`minimax_h3_audio_vae_fp32.safetensors`、`minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors`。
- 文件分别放在 `models/diffusion_models`、`text_encoders`、`vae`、`loras`，按工作流文件名核对。官方其他量化版本不能仅靠重命名替代当前版本。

## 复现顺序

1. 先查看已有总档案，不要再次安装已完成环境；启动已有 ComfyUI。
2. 从总档案取输入图，复制到 `ComfyUI/input`。`direct-first-last-api.json` 需要 `outfit10_01.png`，`guide-first-last-api.json` 需要 `outfit10_04.png`；分别对应总档案十套造型第 1 与第 4 张图。噜噜工作流需要 `lulu_electric_start.png`，内容是总档案的 `lulu-first-frame.png`。
3. 本仓库工作流均为 **ComfyUI API prompt JSON**；不保证拖入画布能还原布局。通过 `/prompt` 提交；要画布版本请使用 ComfyUI 对应模板重建节点或显式转换，不要把它误称为画布 JSON。
4. API 请求体为 `{"prompt": 工作流JSON对象}`，POST 到本机 `http://127.0.0.1:8188/prompt`；记录返回 prompt_id，再查询 `/history/{prompt_id}`，确认 success 后读取输出。
5. 在重跑前修改输出前缀，避免覆盖旧成片。核对所有模型名、图片名、帧数、画幅、采样器、种子。
6. 生成后检查实际视频帧数、fps、尺寸和音轨时长；文字提示里的秒数不等于程序参数。

## 提示词组织

现有脚本分为主体与镜头动作、`overall_soundscape` 声场、`non_diegetic_music` 配乐三块；多镜头用时间区间描述。台词、镜头切换时刻属于生成意图，不是确定时间码。精确字幕、卡点和可读 UI 在后期实现。

## 文件状态

工作流复制自已成功执行的归档；跨机器复现还依赖相同节点实现和权重。没有将整个运行环境打包，也没有把源程序历史绝对路径伪装为通用安装器。本仓库不包含参考视频动作迁移成片。
