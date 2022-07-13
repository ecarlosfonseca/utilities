import moviepy.editor

# read video file
video = moviepy.editor.VideoFileClip('video.mp4')

# convert video to audio
audio = video.audio

# save audio file
audio.write_audiofile('audio.mp3')