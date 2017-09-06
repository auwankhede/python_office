import webbrowser

class TvShow(Video):
    ''' This class is used to display TvShow'''
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]    

    def __init__(self,movie_title, session, episode, trailer_youtube):
        #self.title = movie_title
        Video.__init__(self,movie_title)
        self.session = session
        self.episode = episode
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
