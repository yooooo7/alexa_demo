MOVIE_TEMPLATE = [
    {
        'needSentiment': False,
        'entityType': None,
        'templates': [
            'Sure. Have you seen a movie recently?',
            'No problem. Did you see a movie these days?',
            'Certainly. Have you watched a film over the past few days?'
        ]
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
    },
    {
        'needSentiment': False,
        'entityType': ['ifHaveSeen'],
        'ifHaveSeenTemplates': {
            True: [''],
            False: ['']
        },
        'templates': ['']
    },
    {
        'needSentiment': True,
        'sentimentTemplates':  {
            'pos': [''],
            'other': [''],
            'neg': ['Can you tell me about it then.']
        },
        'entityType': ['MovieDescription'],
        'template':['{}']
    },
    {
        'needSentiment': True,
        'entityType': None,
        'templates': [
            'What is your all time favourite movie?',
            'Do you have one favourite movie? Which one is it?',
            'What is movie that you like all-time?']
    },

    {
        'needSentiment': False,
        'entityType': ['MovieTitle'],
        # func返回rate最高电影->movie description
        'templates': ['I like {} best! {}']
    },
    {
        'needSentiment': True,
        'sentimentTemplates':  {
            'pos': ['what do you like about it',
                    'how woudl you rate it',
                    'what impress on you most'],
            'other': [''],
            'neg': ['can you tell me why'],
        },
        'entityType':None,
        'template':['{}']
    },
    {
        'needSentiment': True,
        'sentimentTemplates':  {
            'pos': ['I totally agree',
                    'Wow',
                    'That is interesting'],
            'other': ['I see',
                      'you have a deep understanding of this movie'],
            'neg': ['It seems like you have thought in depth']},
        'entityType':None,
        'template': ['{}']  # imdb user comments according to user sentiment
    },
    {
        'needSentiment': False,
        'entityType': None,
        'templates': ['It stars {}']  # actors
    },
    {
        'needSentiment': False,
        'entityType': None,
        'templates': ['and this film is labeled {}']  # movie categories/labels
    }
]
