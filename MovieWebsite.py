import webbrowser
import os

class Movie():

    MovieName = ""
    MovieLink = ""
    MovieImage = ""
    MovieDescription = ""
    
    def __init__(self, Name, Link, Image, Description):
        ''' Initialize class function '''
        self.MovieName = Name
        self.MovieLink = Link
        self.MovieImage = Image
        self.MovieDescription = Description

    def GetHTMLAttribute(self):
        ''' Converts Movie class data to html format '''
        HTML =  '''
        <div class = "MovieElement">
        <h2> MovieName </h2>
        <img id = "MovieID" src="MovieImage" width="220" height="340" align = "middle" hspace="20" onclick = "SetVideo('MovieLink')">
        </div>
        '''
        HTML = HTML.replace("MovieName", self.MovieName)
        HTML = HTML.replace("MovieID", self.MovieName)
        HTML = HTML.replace("MovieImage", self.MovieImage)
        HTML = HTML.replace("MovieLink", self.MovieLink)

        return HTML

def CreateMovies():
    ''' Simple function to create a list of movies '''

    MovieList = []

    MovieList.append(Movie("The NeverEnding Story", "https://www.youtube.com/embed/B3DcWtkKeIY", "https://upload.wikimedia.org/wikipedia/en/9/9b/Neverendingstoryposter.jpg", "A story that never ends"))

    MovieList.append(Movie("Jumanji", "https://www.youtube.com/embed/OJKHQLM8AbM", "https://upload.wikimedia.org/wikipedia/en/b/b6/Jumanji_poster.jpg", "A story about a board game"))

    MovieList.append(Movie("A.I.", "https://www.youtube.com/embed/sqS83f-NUww", "https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg", "A story about an android boy"))

    return MovieList

def CreateHTML(MovieList):
    ''' Creates a string formated for html and inserts the movie html into it '''
    HTML = '''
<!DOCTYPE html>
<html>
<head>
<style>

.Modal 
{
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 100px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

.Modal-content 
{
    position: relative;
    background-color: #fefefe;
    margin: auto;
    padding: 0;
    border: 1px solid #888;
    width: 80%;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
    -webkit-animation-name: animatetop;
    -webkit-animation-duration: 0.4s;
    animation-name: animatetop;
    animation-duration: 0.4s
}

@-webkit-keyframes animatetop 
{
    from {top:-300px; opacity:0}
    to {top:0; opacity:1}
}

@keyframes animatetop 
{
    from {top:-300px; opacity:0}
    to {top:0; opacity:1}
}

.Movies
{
    // width: 100px;
    // height: 100px;
    display: table-cell;
    text-align: center;
    // vertical-align: middle;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;

    margin: auto;
    // background-color: #999;
}

.MovieElement
{
    text-align: center;
    vertical-align: middle;
    display: inline-block;
    position: relative;
    float: left;
    height: 700px;
    width: 500px;
    max-height: 100%;
    max-width: 100%;
    min-height: 500px;
    min-width: 500px;
    overflow: hidden;
    background-position: 50% 50%;
    background-repeat:   no-repeat;
    background-size:     cover;        
}

</style>
</head>
<body>

<div class = "Movies">
    MovieElements
</div>

<div id="ModalID" class="Modal">
    <div class="Modal-content">
        <iframe id = "Video" src = "https://www.youtube.com/embed/XGSy3_Czz8k" frameborder="0" style="overflow: hidden; height: 80%;
        width: 80%; position: fixed;" height="100%" width="100%"></iframe>
    </div>
</div>

<script>

var Modal = document.getElementById('ModalID');

var Video = document.getElementById("Video");

window.onclick = function(event) 
{
    if (event.target == Modal) 
    {
        Modal.style.display = "none";
        Video.src = "";
    }
}

function SetVideo( Link )
{
    Video.src = Link + "?autoplay=1";
    Modal.style.display = "block";
}

</script>

</body>
</html>
    '''

    MovieHTML = ""
    for Movie in MovieList:
        MovieHTML += Movie.GetHTMLAttribute()

    HTML = HTML.replace("MovieElements", MovieHTML)

    return HTML


Movies = []

Movies = CreateMovies()

HTML = CreateHTML(Movies)

OutputFile = open('MovieWebsite.html', 'w')

Content = HTML

OutputFile.write(Content)
OutputFile.close()

WebsiteURL = os.path.abspath(OutputFile.name)
webbrowser.open('file://' + WebsiteURL, new=2)
