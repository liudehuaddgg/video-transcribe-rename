#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
视频转录重命名脚本
根据视频旁白内容重命名视频文件
"""

import os
import subprocess
import re
import sys
from pathlib import Path
from faster_whisper import WhisperModel

# 配置
VIDEO_DIR = "/mnt/e/图片编号"
AUDIO_TEMP_DIR = "/tmp/video_audio"
MAX_FILENAME_LENGTH = 100  # 文件名最大长度

# 创建临时目录
os.makedirs(AUDIO_TEMP_DIR, exist_ok=True)

def extract_audio(video_path, audio_path):
    """从视频中提取音频"""
    cmd = [
        os.path.expanduser("~/.local/share/ffmpeg-downloader/ffmpeg/ffmpeg"),
        "-i", video_path,
        "-vn",  # 不包含视频
        "-acodec", "pcm_s16le",  # 16-bit PCM
        "-ar", "16000",  # 16kHz采样率
        "-ac", "1",  # 单声道
        "-y",  # 覆盖输出文件
        audio_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0

def transcribe_audio(audio_path, model):
    """使用faster-whisper转录音频"""
    segments, info = model.transcribe(audio_path, language="zh")
    text = " ".join([segment.text for segment in segments])
    return text.strip()

def sanitize_filename(text):
    """清理文件名，移除不合法字符"""
    # 移除Windows文件名不允许的字符
    text = re.sub(r'[<>:"/\\|?*]', '', text)
    # 移除首尾空格和点
    text = text.strip().strip('.')
    # 限制长度
    if len(text) > MAX_FILENAME_LENGTH:
        text = text[:MAX_FILENAME_LENGTH]
    # 如果为空，使用默认名称
    if not text:
        text = "未识别内容"
    return text

def main():
    print("正在加载Whisper模型...")
    # 使用small模型，平衡速度和准确性
    model = WhisperModel("small", device="cpu", compute_type="int8")
    
    # 获取所有视频文件
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']
    video_files = []
    for f in os.listdir(VIDEO_DIR):
        if any(f.lower().endswith(ext) for ext in video_extensions):
            # 跳过已经有中文名字的文件
            if re.search(r'[\u4e00-\u9fff]', f):
                print(f"跳过已命名文件: {f}")
                continue
            video_files.append(f)
    
    print(f"找到 {len(video_files)} 个需要处理的视频文件")
    
    # 处理每个视频
    results = []
    for i, video_file in enumerate(video_files, 1):
        video_path = os.path.join(VIDEO_DIR, video_file)
        print(f"\n[{i}/{len(video_files)}] 处理: {video_file}")
        
        # 提取音频
        audio_path = os.path.join(AUDIO_TEMP_DIR, f"audio_{i}.wav")
        print("  提取音频...")
        if not extract_audio(video_path, audio_path):
            print("  错误: 无法提取音频")
            continue
        
        # 转录
        print("  转录中...")
        try:
            text = transcribe_audio(audio_path, model)
            if text:
                print(f"  旁白内容: {text}")
                
                # 生成新文件名
                new_name = sanitize_filename(text)
                new_filename = f"{new_name}.mp4"
                new_path = os.path.join(VIDEO_DIR, new_filename)
                
                # 检查是否重名
                counter = 1
                while os.path.exists(new_path) and new_path != video_path:
                    new_filename = f"{new_name}_{counter}.mp4"
                    new_path = os.path.join(VIDEO_DIR, new_filename)
                    counter += 1
                
                # 重命名
                os.rename(video_path, new_path)
                print(f"  已重命名为: {new_filename}")
                results.append((video_file, new_filename, "成功"))
            else:
                print("  未识别到语音内容")
                results.append((video_file, "", "无语音"))
        except Exception as e:
            print(f"  错误: {e}")
            results.append((video_file, "", f"错误: {e}"))
        
        # 清理临时音频文件
        if os.path.exists(audio_path):
            os.remove(audio_path)
    
    # 输出汇总
    print("\n" + "="*50)
    print("处理完成汇总:")
    print("="*50)
    for old, new, status in results:
        if new:
            print(f"  {old} -> {new} [{status}]")
        else:
            print(f"  {old} [{status}]")

if __name__ == "__main__":
    main()
