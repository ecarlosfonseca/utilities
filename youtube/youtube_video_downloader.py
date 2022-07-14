from pytube import YouTube, Playlist
  
def download_from_youtube(url: str, file_name: str, audio_only: bool):
    """Downloads video or audio files from youtube

    Args:
        url (str): Url from the file you want to save
        file_name (str): Final file name
    """
    
    yt = YouTube(url) 

    if audio_only:
        my_video = yt.streams.get_audio_only('mp4')
    else:
        my_video = yt.streams.get_highest_resolution()

    my_video.download(filename=f'{file_name}.mp4')

    print(f"File {file_name}.mp4 downloaded and saved on this script's directory")


download_from_youtube(
	'https://www.youtube.com/watch?v=25BP-eioBG4&ab_channel=SoulMatesRecords',
	'Nina_Simone_ft_Lauren_Hill',
	True)

def download_play_list(url: str, folder_name: str):
    """Downloads entire playlist from youtube to one folder located on the directory of this script

    Args:
        url (str): playlist url
        folder_name (str): name of the new folder to create with all files 
    """

    p = Playlist(url)

    for music_url in p.video_urls:
        yt = YouTube(music_url) 
        title = yt.title.replace('/', ' ')
        my_video = yt.streams.get_audio_only('mp4')
        my_video.download(output_path=folder_name, filename=f'{title}.mp4')
        print(f'{title} downloaded')

    print(f"Playlist downloaded and saved on {folder_name} folder")


download_play_list(
    'https://www.youtube.com/playlist?list=PL9MhESi6jTka0JlNTQmvNqDICF9Fn0kkK',
    'Whiplash_soundtrack/')
