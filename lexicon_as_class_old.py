

class lexicon(object):

    verb_words = ['go', 'stop', 'kill', 'eat']
    stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
    noun_words = ['door', 'bear', 'princess', 'cabinet']
    direction_words = ['north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'bacl']


    def __init__(self):
        pass
	
    def scan(sentence):
        words = self.split_sentence(sentence)
	
        return "charlie"

    def split_sentence(self, sentence):
        """THis function splits the sentence"""
        words = sentence.split()
        return words
	
    def is_it_a_number(self, value):
        try:
            a = int(value)
            return True
        except ValueError:
            return False
	
	
	
    def assign_types(self, word):
        if word in self.direction_words:
            return 'direciton'
        elif word in self.stop_words:
            return 'stop'
        elif word in self.noun_words:
            return 'noun'
        elif word in self.verb_words:
            return 'verb'
        elif self.is_it_a_number(word):
            return int(word)
        else:
            return 'error'
	
	
		
	








class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
		
    def go(self, direction):
        return self.paths.get(direction, None)
		
    def add_paths(self, paths):
        self.paths.update(paths)
		
		