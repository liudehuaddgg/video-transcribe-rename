# Video Transcribe Rename

批量视频转录重命名工具 - 根据视频旁白内容自动重命名视频文件

## 功能特点

- 自动提取视频音频并转录文字
- 使用 faster-whisper 进行语音识别（支持中文）
- 根据旁白内容智能重命名视频文件
- 批量处理，无需手动操作
- 支持 MP4、AVI、MOV 等常见视频格式

## 安装依赖

```bash
# 创建虚拟环境
python3 -m venv ~/.venv/whisper_env
source ~/.venv/whisper_env/bin/activate

# 安装 faster-whisper（比 openai-whisper 更轻量）
pip install faster-whisper ffmpeg-python imageio-ffmpeg

# 安装 ffmpeg（无需 sudo）
pip install ffmpeg-downloader
ffdl install -y
```

## 使用方法

```bash
# 激活虚拟环境
source ~/.venv/whisper_env/bin/activate

# 运行脚本
python video_transcribe_rename.py
```

## 配置

编辑脚本中的 `VIDEO_DIR` 变量，指定要处理的视频目录：

```python
VIDEO_DIR = "/path/to/your/videos"
```

## 工作原理

1. 扫描指定目录下的视频文件
2. 使用 ffmpeg 提取音频
3. 使用 faster-whisper 转录音频内容
4. 根据转录文本重命名视频文件
5. 自动处理重名文件和无语音视频

## 示例

处理前：
```
sora-video-5c32192e-3dd9-46c9-a81d-1817134a0ca2_.mp4
sora-video-61a8cf8a-d944-4dd6-abe8-9c17b9e01ae0_.mp4
```

处理后：
```
有时候看着别人过的好,不只是羡慕,更是意识到自己连做同样式的资格都没有。.mp4
當你不再抱怨環境 你就已經比過去的自己強大.mp4
```

## 注意事项

- 首次运行会下载 Whisper 模型（约 500MB）
- 处理时间取决于视频数量和长度
- 无语音的视频会保留原名
- 已有中文名的文件会自动跳过

## 技术栈

- Python 3.11+
- faster-whisper - 语音识别
- ffmpeg - 音频提取
- ctranslate2 - 模型推理加速

## License

MIT License
