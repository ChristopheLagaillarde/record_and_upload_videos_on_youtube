# Program : append audio on video
# Description : This script will put an audio file on a video file
# Date : 14/08/22
# Author : Christophe Lagaillarde
# Version : 1.0

from moviepy.editor import VideoFileClip, AudioFileClip


def append_audio_on_video(audio_file: str, video_file: str, audio_image_lag_seconds: float) -> None:

    video_clip: VideoFileClip = VideoFileClip(video_file)
    audio_clip: AudioFileClip = AudioFileClip(audio_file)
    end: int = audio_clip.end

    audio_clip: AudioFileClip = audio_clip.subclip(audio_image_lag_seconds, end)

    final_clip: VideoFileClip = video_clip.set_audio(audio_clip)

    final_clip.write_videofile("final.mp4")

    return None
