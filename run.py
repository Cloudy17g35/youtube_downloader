from youtube_video import YoutubeVideo
import json
from typing import List

with open('config.json') as f:
    config_file = json.loads(f.read())
    links_to_videos:List[str] = config_file['links_to_videos']
    output_folder:str = config_file['output_folder']


def main():
    for link_to_video in links_to_videos:
        yt_video:YoutubeVideo = YoutubeVideo(link_to_video)
        streams = yt_video.get_streams
        video_with_highest_res = streams.get_highest_resolution()
        print(f'''Youtube video 
{yt_video} 
will be downloaded to folder: {output_folder}''')
        video_with_highest_res.download('Videos')

    
if __name__ == '__main__':
    main()