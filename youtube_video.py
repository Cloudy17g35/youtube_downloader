import pytube
    

class YoutubeVideo:
    
    def __init__(self, link:str):
        self.video = pytube.YouTube(link)
        
    @property
    def get_streams(self) -> pytube.StreamQuery:
        return self.video.streams
    

    def __str__(self):
        return f'''Title: {self.video.title}
Views: {self.video.views}
Length: {self.video.length / 60} min'''
    

    
    
    








