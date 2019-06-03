from ..ir import search_movie_2_actors, search_movie_overview
import random

class Node():
    def __init__(self, templates: list, func = None):
        self.templates = templates
        self.sentiment = None
        self.entities = None
        self.func = func
    
    def template2sentence(self, arg):
        sentence = random.sample(self.templates, 1)[0]

        if self.func is None:
            return sentence
        
        values = self.func(arg)
        sentence = random.sample(self.templates, 1)[0].format(*values)

        return sentence


ROOT = Node(templates = ['Hi, this is Sydney Jack. How are you?', 'how are you?', 'how\'s it going?'])

NODE_1_1 = Node(templates = [
    'That\'s good! Sports or movies are topics you could be interested in and we could talk about any of them.'
    ])
NODE_1_2 = Node(templates = [
    'Sorry to hear that. Sports or movies are topics you could be interested in and we could talk about any of them.'
    ])
NODE_1_3 = Node(templates = [
    'Sports or movies are topics you could be interested in and we could talk about any of them.'
    ])

NODE_2_1 = Node(templates = [
    'Sure. Have you seen a movie recently? What was that',
    'Let us chat. Did you see a movie these days? can you tell me the name',
    'Certainly. Have you watched a film over the past few days? what was that'
    ])
NODE_2_2 = Node(templates = [''])

NODE_3_1 = Node(
    templates = [
        'Is that the film with {} and {}?',
        'Is that movie the one depicting {} and {}?',
        'Are {} and {} the stars in the movie?'
    ],
    func = search_movie_2_actors
)

NODE_4_1 = Node(
    templates = ['I want to share you the story of it.{}'],
    func = search_movie_overview
)
NODE_4_2 = Node(
    templates = ['I want to share you the story of it even you do not like it.{}'],
    func = search_movie_overview
)

dialog_mapping = {
    ROOT: {
        NODE_1_1: { 'sentiment': ['pos'], 'entities': None },
        NODE_1_2: { 'sentiment': ['neg'], 'entities': None },
        NODE_1_3: { 'sentiment': ['other'], 'entities': None }
    },

    NODE_1_1: {
        NODE_2_1: { 'sentiment': None, 'entities': ['movie'] },
        NODE_2_2: { 'sentiment': None, 'entities': ['sport'] }
    },
    NODE_1_2: {
        NODE_2_1: { 'sentiment': None, 'entities': ['movie'] },
        NODE_2_2: { 'sentiment': None, 'entities': ['sport'] }
    },
    NODE_1_3: {
        NODE_2_1: { 'sentiment': None, 'entities': ['movie'] },
        NODE_2_2: { 'sentiment': None, 'entities': ['sport'] }
    },

    NODE_2_1: {
        NODE_3_1: { 'sentiment': None, 'entities': 'any' }
    },

    NODE_3_1: {
        NODE_4_1: { 'sentiment': ['pos'], 'entities': None },
        NODE_4_2: { 'sentiment': ['neg', 'other'], 'entities': None }
    }
}
