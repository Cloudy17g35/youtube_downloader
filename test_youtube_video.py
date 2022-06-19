from youtube_video import YoutubeVideo
import pytube

link_to_video = 'https://www.youtube.com/watch?v=D4T2N0yAr20&ab_channel=NeetCode'

yt_video = YoutubeVideo(link=link_to_video)

class TestYoutubeVideo:
    def test_get_streams(self):
        streams = yt_video.get_streams
        assert isinstance(streams, pytube.StreamQuery)
        assert len(streams) >= 1
    
