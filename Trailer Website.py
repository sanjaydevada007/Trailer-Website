import fresh_tomatoes
import webbrowser
class movie():
    def __init__(self,mt,ms,pi,yt):
        self.title=mt
        self.storyline=ms
        self.poster_image_url=pi
        self.trailer_youtube_url=yt
    def strailer(self):
        webbrowser.open(self.trailer_youtube_url)
toy_story=movie("Toy Story","A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boys room",
         "http://www.techagesite.com/toy-story/movie-toy-story-wallpapers-hd-1920x1080-great-escape.jpg",
         "https://www.youtube.com/watch?v=KYz2wyBy3kc")
         
avatar=movie("Avatar","A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
              "http://wallpapercave.com/wp/vTucv7p.jpg",
              "https://www.youtube.com/watch?v=5PSNL1qE6VY")

A_Wednesday=movie("A Wednesday","A retiring police officer reminisces about the most astounding day of his career. About a case that was never filed but continues to haunt him in his memories - the case of a man and a Wednesday."
                  ,"http://wearepak.com/wp-content/uploads/2016/07/A-Wednesday-2008-Full-Movie-Hindi-Watch-Online-HD.jpg",
                  "https://www.youtube.com/watch?v=LGfwASavWNQ")

Ted=movie("Ted",
          "John Bennett, a man whose childhood wish of bringing his teddy bear to life came true, now must decide between keeping the relationship with the bear or his girlfriend, Lori.",
          "https://en.wikipedia.org/wiki/Ted_(film)#/media/File:Ted_poster.jpg",
          "https://www.youtube.com/watch?v=9fbo_pQvU7M")

Inception=movie("Inception",
                "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                "https://en.wikipedia.org/wiki/Inception#/media/File:Inception_(2010)_theatrical_poster.jpg",
                "https://www.youtube.com/watch?v=YoHD9XEInc0")

Dangal=movie("Dangal",
             "Biographical sports drama on former wrestler Mahavir Singh Phogat and his two wrestler daughters' struggle towards glory at the Commonwealth Games in the face of societal oppression.",
             "http://djmaza-djpunjab.com/wp-content/uploads/2016/10/Dangal-Trailer-.jpg",
             "https://www.youtube.com/watch?v=x_7YlGv9u1g")
movies=[toy_story, avatar, A_Wednesday, Ted, Inception, Dangal]
fresh_tomatoes.open_movies_page(movies)
