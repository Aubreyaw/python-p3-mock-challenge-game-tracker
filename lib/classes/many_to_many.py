class Game:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) == 0:   
            raise ValueError("Title must be more than 0 characters")
        self._title = title

    @property
    def title(self):
        return self._title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game == self]))
    
    def average_score(self, player):
        player_results = [result for result in Result.all if result.game == self and result.player == player]
        scores = [result.score for result in player_results]
        average = sum(scores) / len(scores)
        return average
    
class Player:
    
    def __init__(self, username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        if len(username) <2 or len(username) > 16:
            raise ValueError("Username must be between 2 and 16 characters")
        self._username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise TypeError("Username must be a string")
        if len(new_username) < 2 or len(new_username) > 16:
            raise ValueError("Username must be between 2 and 16 characters")
        self._username = new_username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        games = [result.game for result in Result.all if result.player == self]
        return list(set(games))

    def played_game(self, game):
        games_played = [result.game for result in Result.all if result.player == self]
        return game in games_played
    
    def num_times_played(self, game):
        games_played = len([result.game for result in Result.all if result.player == self and result.game == game])
        return games_played

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        if not isinstance(score, int):
            raise TypeError("Score must be a number")
        # Score validation in Result ensures scores are between 1 and 5000 inclusive.
        # Tests providing scores outside this range (like 5002) will raise a ValueError.
        if score < 1 or score > 5000:
            raise ValueError("Score must be between 1 and 5000")
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score