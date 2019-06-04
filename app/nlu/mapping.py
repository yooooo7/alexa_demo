from .normalization import normalization
dic = [['Star Wars', 'MOVIE_TITLE'], ['Avengers', 'MOVIE_TITLE'], ['The Avengers', 'MOVIE_TITLE'],
 ['Star Wars', 'MOVIE_TITLE'], ['Beauty and the Beast', 'MOVIE_TITLE'], ['Iron Man', 'MOVIE_TITLE'], 
 ['Captain America', 'MOVIE_TITLE'], ['Aquaman', 'MOVIE_TITLE'], ['The Lord of the Rings', 'MOVIE_TITLE'],
 ['Skyfall', 'MOVIE_TITLE'], ['The Dark Knight Rises', 'MOVIE_TITLE'], ['Toy Story', 'MOVIE_TITLE'], 
 ['Pirates of the Caribbean', 'MOVIE_TITLE'], ['Captain Marvel', 'MOVIE_TITLE'], 
 ['Despicable Me', 'MOVIE_TITLE'], ['Alice in Wonderland', 'MOVIE_TITLE'], ['The Hobbit', 'MOVIE_TITLE'],
 ['The Dark Knight', 'MOVIE_TITLE'], ["Harry Potter and the Philosopher's Stone", 'MOVIE_TITLE'], 
 ['The Lion King', 'MOVIE_TITLE'], ['Pirates of the Caribbean', 'MOVIE_TITLE'], ['Jumanji', 'MOVIE_TITLE'],
 ['The Hobbit', 'MOVIE_TITLE'], ['Finding Nemo', 'MOVIE_TITLE'], ['Gone with the Wind', 'MOVIE_TITLE'], 
 ['the Harry Potter', 'MOVIE_TITLE'], ['The Hobbit', 'MOVIE_TITLE'], ['shazam', 'MOVIE_TITLE'], 
 ['Dumbo', 'MOVIE_TITLE'], ['hellboy', 'MOVIE_TITLE'], ['green book', 'MOVIE_TITLE'], ['spider man', 'MOVIE_TITLE'], 
 ['La La Land', 'MOVIE_TITLE'], ['Ready Player One', 'MOVIE_TITLE'], ['Hereditary\xa0', 'MOVIE_TITLE'], ['Tomb Raider', 'MOVIE_TITLE'], 
 ['deadpool', 'MOVIE_TITLE'], ['The Godfather', 'MOVIE_TITLE'], ['the shawshank redemption', 'MOVIE_TITLE'],
 ['the dark knight', 'MOVIE_TITLE'], ['goodfellas', 'MOVIE_TITLE'], ["Schindler's List", 'MOVIE_TITLE'], 
 ['fight club', 'MOVIE_TITLE'], ['saving private ryan', 'MOVIE_TITLE'], ['back to the future', 'MOVIE_TITLE'], 
 ['the silence of the lambs', 'MOVIE_TITLE'], ['The Lord of the Rings', 'MOVIE_TITLE'], ['inception', 'MOVIE_TITLE'],
 ['citizen kane', 'MOVIE_TITLE'], ['Jaws', 'MOVIE_TITLE'], ['Jurassic Park', 'MOVIE_TITLE'], ['good will hunting', 'MOVIE_TITLE'], 
 ['American beauty', 'MOVIE_TITLE'], ['Monty Python and the Holy Grail', 'MOVIE_TITLE'], 
 ['Batman', 'MOVIE_TITLE'], ['Florida Basketball Association', 'LEAGUES'], ['Independent Basketball Association', 'LEAGUES'], 
 ['FIBA Americas League', 'LEAGUES'], ['NBL', 'LEAGUES'], ['National Basketball League', 'LEAGUES'], ['American Basketball Association', 'LEAGUES'], 
 ['Continental Basketball Association', 'LEAGUES'], ['CBA', 'LEAGUES'], ['NBA', 'LEAGUES'],
 ['ABA', 'LEAGUES'], ['National Collegiate Athletic Association', 'LEAGUES'], ['NCAA', 'LEAGUES'], 
 ['NBA Development League', 'LEAGUES'], ['NBDL', 'LEAGUES'], ['NBA D-League', 'LEAGUES'], ['NBA Development League', 'LEAGUES'], 
 ['National Basketball Association', 'LEAGUES'], ['NAIA', 'LEAGUES'], ['National Association of Intercollegiate Athletics', 'LEAGUES'], 
 ['National Basketball Association', 'LEAGUES'], ['Boston Celtics', 'NBATEAMS'], ['Brooklyn Nets', 'NBATEAMS'], 
 ['New York Knicks', 'NBATEAMS'], ['Philadelphia 76ers', 'NBATEAMS'], ['Toronto Raptors', 'NBATEAMS'],
 ['Chicago Bulls', 'NBATEAMS'], ['Cleveland Cavaliers', 'NBATEAMS'], ['Detroit Pistons', 'NBATEAMS'], 
 ['Indiana Pacers', 'NBATEAMS'], ['Milwaukee Bucks', 'NBATEAMS'], ['Atlanta Hawks', 'NBATEAMS'], 
 ['Charlotte Hornets', 'NBATEAMS'], ['Miami Heat', 'NBATEAMS'], ['Orlando Magic', 'NBATEAMS'], 
 ['Washington Wizards', 'NBATEAMS'], ['Dallas Mavericks', 'NBATEAMS'], ['Houston Rockets', 'NBATEAMS'], ['Memphis Grizzlies', 'NBATEAMS'], 
 ['New Orleans Pelicans', 'NBATEAMS'], ['San Antonio Spurs', 'NBATEAMS'], ['Denver Nuggets', 'NBATEAMS'], ['Minnesota Timberwolves', 'NBATEAMS'], 
 ['Oklahoma City Thunder', 'NBATEAMS'], ['Portland Trail Blazers', 'NBATEAMS'], ['Utah Jazz', 'NBATEAMS'], ['Golden State Warriors', 'NBATEAMS'], 
 ['Los Angeles Clippers', 'NBATEAMS'], ['Los Angeles Lakers', 'NBATEAMS'], ['Phoenix Suns', 'NBATEAMS'], ['Sacramento Kings', 'NBATEAMS'], ['Steven Spielberg', 'DIRECTORS'], 
 ['Peter Jackson', 'DIRECTORS'], ['Michael Bay', 'DIRECTORS'], ['James Cameron', 'DIRECTORS'], ['David Yates', 'DIRECTORS'], ['Christopher Nolan', 'DIRECTORS'], 
 ['Robert Zemeckis', 'DIRECTORS'], ['Ron Howard', 'DIRECTORS'], ['Tim Burton', 'DIRECTORS'], ['Ridley Scott', 'DIRECTORS'], ['Steven Spielberg', 'DIRECTORS'], 
 ['Michael Bay', 'DIRECTORS'], ['Peter Jackson', 'DIRECTORS'], ['Ron Howard', 'DIRECTORS'], ['Robert Zemeckis', 'DIRECTORS'], ['Christopher Nolan', 'DIRECTORS'], 
 ['James Cameron', 'DIRECTORS'], ['Tim Burton', 'DIRECTORS'], ['Clint Eastwood', 'DIRECTORS'], ['David Yates', 'DIRECTORS'], ['LeBron James', 'PLAYERS'], ['Kobe Bryant', 'PLAYERS'], 
 ['Michael Jordan', 'PLAYERS'], ['Dennis Rodman', 'PLAYERS'], ['Magic Johnson', 'PLAYERS'], ["Shaquille O'Neal", 'PLAYERS'], ['Charles Barkley', 'PLAYERS'], ['Kareem Abdul-Jabbar', 'PLAYERS'], 
 ['Dwight Howard', 'PLAYERS'], ['Dwyane Wade', 'PLAYERS'], ['Allen Iverson', 'PLAYERS'], ['Mike Harris', 'PLAYERS'], ['Carmelo Anthony', 'PLAYERS'], ['Bill Walton', 'PLAYERS'], 
 ['Jason Kidd', 'PLAYERS'], ['Stephen A. Smith', 'PLAYERS'], ['Lamar Odom', 'PLAYERS'], ['Tony Parker', 'PLAYERS'], ['Bill Bradley', 'PLAYERS'], ['Kevin Garnett', 'PLAYERS'], 
 ['Michael Warren', 'PLAYERS'], ['Kris Humphries', 'PLAYERS'], ['John Amaechi', 'PLAYERS'], ['Larry Bird', 'PLAYERS'], ['Karl Malone', 'PLAYERS'], 
 ['Alonzo Mourning', 'PLAYERS'], ['Steve Nash', 'PLAYERS'], ['Metta World Peace', 'PLAYERS'], ['Jason Collins', 'PLAYERS'], ['Isiah Thomas', 'PLAYERS'], ['Paul Pierce', 'PLAYERS'], 
 ['Jalen Rose', 'PLAYERS'], ['Jeremy Lin', 'PLAYERS'], ['Andre Drummond', 'PLAYERS'], ['Wilt Chamberlain', 'PLAYERS'], ['Vince Carter', 'PLAYERS'], ['Kevin Durant', 'PLAYERS'], 
 ['Carlos Boozer', 'PLAYERS'], ['Ray Allen', 'PLAYERS'], ['Grant Hill', 'PLAYERS'], ['Keanu Reeves', 'ACTORS'], ['Bruce Willis', 'ACTORS'], ['Tom Cruise', 'ACTORS'], ['Sandra Bullock', 'ACTORS'], 
 ['Tom Hanks', 'ACTORS'], ['Harrison Ford', 'ACTORS'], ['Jack Nicholson', 'ACTORS'], ['Leonardo DiCaprio', 'ACTORS'], 
 ['Robert Downey', 'ACTORS'], ['Johnny Depp', 'ACTORS'], ['Cameron Diaz', 'ACTORS'], 
 ['Tom Hanks', 'ACTORS'], ['Johnny Depp', 'ACTORS'], ['Aamir Khan', 'ACTORS'], ['Jim Carrey', 'ACTORS'], 
 ['Arnold Schwarzenegger', 'ACTORS'], ['Mel Gibson', 'ACTORS'], ['Brad Pitt', 'ACTORS'], ['Chris Evans', 'ACTORS'], ['Emma Stone', 'ACTORS'], 
 ['Jennifer Lawrence', 'ACTORS'], ['Sandra Bullock', 'ACTORS'], ['Amy Adams', 'ACTORS'], ['Scarlett Johansson', 'ACTORS'], 
 ['Anne Hathaway', 'ACTORS'], ['Meryl Streep', 'ACTORS'], ['Tom Hanks', 'ACTORS'], ['Denzel Washington', 'ACTORS'], ['Natalie Portman', 'ACTORS'], 
 ['Jessica Alba', 'ACTORS'], ['Angelina Jolie', 'ACTORS'], ['Elle Fanning', 'ACTORS'], ['Blake Lively', 'ACTORS'], ['Charlize Theron', 'ACTORS'], 
 ['Denzel Washington', 'ACTORS'], ['Jake Gyllenhaal', 'ACTORS'], ['Morgan Freeman', 'ACTORS'], ['Kevin Spacey', 'ACTORS'], ['Dwayne Johnson', 'ACTORS'], ['Anthony Hopkins', 'ACTORS'], 
 ['Edward Norton', 'ACTORS'], ['Ben Affleck', 'ACTORS'], ['Clint Eastwood', 'ACTORS'], ['Marlon Brando', 'ACTORS'], ['Sidney Poitier', 'ACTORS'], 
 ['Sean Penn', 'ACTORS'], ['Jack Nicholson', 'ACTORS'],['movie','TOPIC'],['sport','TOPIC']]

def mapping (user_input, dic = dic):
    for i in range(len(dic)):
        dic_i = normalization(dic[i][0])
        common_part= [j for j in user_input if j in dic_i]
        if len(common_part) == len(dic_i):
            return dic[i][1],' '.join(common_part)     
    return None, None

# print(mapping(['star', 'war']))
print(normalization('the harry potter'))
print(mapping(['harry', 'potter']))