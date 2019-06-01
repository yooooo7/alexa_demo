GREETING_TAMPLATE = [
    { 
        'needSentiment': False,
        'templates':  ['Hi, this is Sydney Jack. How are you?', 'how are you?', 'how\'s it going?']
    },
    { 
        'needSentiment': True,
        'sentimentTemplates':  {
            'pos': ['That\'s good!', 'Great!'],
            'other': [''],
            'neg': ['Sorry to hear that.']
        },
        'templates': ['Sports or movies are topics you could be interested in and we could talk about any of them.']
    }
]