MOVIE_TEMPLATE = [
    {
        'needSentiment': False,
        'entityType': None,
        'templates': [
            'Sure. Have you seen a movie recently? What was that',
            'Let us chat. Did you see a movie these days? can you tell me the name',
            'Certainly. Have you watched a film over the past few days? what was that'
        ]
        #done0 要是回答no 跳3
    },
    {
        'needSentiment': False,
        'entityType': ['MovieActor'],
        'MovieActorTemplates': [
            'Is that the film with {} and {}?',
            'Is that movie the one depicting {} and {}?',
            'Are {} and {} the stars in the movie?'
        ],
        'templates': ['']
        #done1
    }, 
    {
        'needSentiment': True,
        'entityType': ['MovieDes'],
        'sentimentTemplates': {
            'pos': ['I want to share you the story of it.'],
            'neg': ['See you!']
        },
        'MovieDesTemplates': ['{}'],
        'templates': ['']
        #done2
    },
    {
        'needSentiment': False,
        'entityType': None,
        'templates':[
            'What is your all time favourite movie?',
            'Do you have one favourite movie? Which one is it?',
            'What is movie that you like all-time?'
            ]
        #done3
    },
    {
        'needSentiment': False,
        'entityType': ['MovieName', 'MovieDes'],
        'MovieNameTemplates':[
            'my best friend and I like the {} best.',
            '{} is my favorite.',
            '{} is amazing.',
            '{}, I cannot forget it since I first time watched it'
            ],
        'MovieDesTemplates': ['{}'],
        'templates': ['']
        #todo4
    },
    {
        'needSentiment': True,
        'entityType': None,
        'sentimentTemplates':  {
            'pos': [
                'How do you like the film?'
                'tell me more about your feelings',
                'Amazing, tell me more'
            ],
            'other': [
                'tell me more about what do you think',
                'I see, can you comment more'
            ],
            'neg': [
                'Why you comment negatively about this film',
                'may I ask for the reason'
            ]
        },
        'templates': ['']
    },  #done5
    {
        'needSentiment': True,
        'entityType':['MovieReviews'],
        'sentimentTemplates':  {
            'pos': ['Interesting','wow','amazing','good to hear that'],
            'other': ['I see','you are thoughtful','well'],
            'neg': ['Well','I see','any way, it did well at the box office']
        },
        'MovieReviewsTemplates':['some online users think {}'],
        'template':['']
    }, #done6
    {
        'needSentiment': False,
        'entityType': ['MovieActor'],
        'MovieActorTemplate':['It stars {} and {}',
                    'I like the performance of {} and {} in it'],
        'templates': ['']  
    },#done7
    {
        'needSentiment': False,
        'entityType': ['MovieLable'],
        'MovieLableTemplates': ['and this film is labeled {},{} and {}',
                                'it can be found under the category of {}, {} and {}',
                                'it is labled as {}, {} and {}'],
        'templates':['']  
    },#done8
    {
        'needSentiment': True,
        'sentimentTemplates':  {
            'pos': ['Interesting','wow','amazing','good to hear that','I like talking with you'],
            'other': ['I see','well','it is a very good experience talking with you','that is true'],
            'neg': ['Well','I see','that is true']}
        },
    {
        'needSentiment': False,
        'entityType': ['ActorMovie'],
        'MovieActor2':['have you seen {} other film'],
        'templates': ['']  
    }, #done9
    {
        'needSentiment': False,
        'entityType': ['RecommonActor2Movie'],
        'MovieActor2':['I highly recommend you {}, {}'], # 通过actor找电影 再找介绍
        'templates': [''] 
    } #10要是回答no 跳回4
]
