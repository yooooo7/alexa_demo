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
    templates = ['I want to share you the story of it.{}'],
    func = search_movie_overview
)
NODE_5_1 = Node(
    templates = ['what is your favorite movie of all the time']
)
NODE_6_1 = Node(
    templates = [
        'my best friend and I like the {} best.',
        '{} is my favorite.',
        '{} is amazing.',
        '{}, I cannot forget it since I first time watched it'
    ],
    func = search_movie_title
)
NODE_7_1 = Node(
    templates = ['How do you like the film?'
                'tell me more about your feelings',
                'Amazing, tell me more']
)
NODE_7_2 = Node(
    templates = ['tell me more about what do you think',
                'I see, can you comment more']
)
NODE_7_3 = Node(
    templates = ['Why you comment negatively about this film',
                'may I ask for the reason']
)
NODE_8_1 = Node(
    templates = ['Interesting,{}','wow,{}','amazing,{}','good to hear that,{}'],
    func = search_movie_reviews  #undefined func
)
NODE_8_2 = Node(
    templates = ['I see,{}','you are thoughtful,{}','well,{}'],
    func = search_movie_reviews  #undefined func
)
NODE_8_3 = Node(
    templates = ['Well,{}','I see,{}','any way, it did well at the box office, {}'],
    func = search_movie_reviews  #undefined func
)
NODE_9_1 = Node(
    templates = [
        'It stars {} and {}',
        'I like the performance of {} and {} in it'
    ],
    func = search_movie_2_actors
)
NODE_10_1 = Node(
    templates = [
        'and this film is labeled {},{} and {}',
        'and it can be found under the category of {}, {} and {}',
        'and it is labeled as {}, {} and {}'
    ],
    func = search_movie_labels  #undefined func
)
NODE_11_1 = Node(
    templates = ['I highly recommend you {}'],
    func = search_actor_2_movie #undefined func
)
NODE_12_1 = Node(
    templates  = ['{}'],
    func = search_movie_overview
)
NODE_13_1 = Node(
    templates = [
        'it was released in {}, doing very well, check it out and hope you will like it',
        'it was realeased in {} and has become a box office hit,I am sure you will love it'
    ],
    func = search_movie_release_date  #undefined func
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
    },
    NODE_4_1:{
        NODE_5_1:{'sentiment': None, 'entities':'any'}
    },
    NODE_4_2:{
        NODE_5_1:{'sentiment': None, 'entities':'any'}
    },
    NODE_5_1:{
        NODE_6_1:{'sentiment': None, 'entities': 'any'}
    },
    NODE_6_1:{
        NODE_7_1:{'sentiment': ['pos'],'entities':'any'},
        NODE_7_2:{'sentiment': ['other'],'entities':'any'},
        NODE_7_1:{'sentiment': ['neg'],'entities':'any'}
    },
    NODE_7_1:{
        NODE_8_1:{'sentiment': ['pos'],'entities':'any'},
        NODE_8_2:{'sentiment': ['other'],'entities':'any'},
        NODE_8_1:{'sentiment': ['neg'],'entities':'any'}
    },
    NODE_7_2:{
        NODE_8_1:{'sentiment': ['pos'],'entities':'any'},
        NODE_8_2:{'sentiment': ['other'],'entities':'any'},
        NODE_8_1:{'sentiment': ['neg'],'entities':'any'}
    },
    NODE_7_3:{
        NODE_8_1:{'sentiment': ['pos'],'entities':'any'},
        NODE_8_2:{'sentiment': ['other'],'entities':'any'},
        NODE_8_1:{'sentiment': ['neg'],'entities':'any'}
    },
    NODE_8_1:{
        NODE_9_1:{'sentiment': None, 'entities': 'any'}
    },
    NODE_8_2:{
        NODE_9_1:{'sentiment': None, 'entities': 'any'}
    },
    NODE_8_3:{
        NODE_9_1:{'sentiment': None, 'entities': 'any'}
    },
    NODE_9_1:{
        NODE_10_1:{'sentiment': None, 'entities': 'any'}
    },
    NODE_10_1:{
        NODE_11_1:{'sentiment': None,'entities':'any'}
    },
    NODE_11_1:{
        NODE_12_1:{'sentiment': None,'entities':'any'}
    },
    NODE_12_1:{
        NODE_13_1:{'sentiment': None,'entities':'any'}
    }
    
}
