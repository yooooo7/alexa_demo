import random
from .methods import search_2_sug_movies, search_2_movie_actors, search_movie_labels, search_movie_release_date
from .methods import movie_overview_summary, movie_review_summary
from .methods import search_actor_gender, search_actor_2_movies, search_actor_bio_gender, search_actor_birth_gender

class Node():
    def __init__(self, templates: list, func = None):
        self.templates = templates
        self.func = func
    
    def template2sentence(self, arg):
        sentence = random.sample(self.templates, 1)[0]

        if self.func is None:
            return sentence
        
        isExist, values = self.func(arg)
        if not isExist:
            return values
        
        sentence = random.sample(self.templates, 1)[0].format(*values)
        return sentence


ROOT = Node(templates = ['Hey, how are you?', 'how are you?', 'Hey, how\'s it going?'])

NODE_1_POS_OTHER = Node(templates = ['nice to hear that, what\'s your favourite movie'])
NODE_1_NEG = Node(templates = ['sorry to hear that, forget it and let\'s talk about your favourite movie!'])

NODE_2_FAV_MOVIE_INFO = Node(templates = [
    'Really, do you want to see observers\' reviews or recommend you similar movies?'
])
NODE_2_MOVIE_INFO = Node(templates = [
    'What would you like to know? Movie overview, leading actors, genres, release date and observer reviews.'
])

NODE_3_SUG_MOVIE = Node(
    templates = ['I think you would enjoy {} and {}, which one you would like to know more'],
    func = search_2_sug_movies
)
NODE_3_LEAD_ACTOR = Node(
    templates = ['This movie stars {} and {}, do you what to know more actor information'],
    func = search_2_movie_actors
)
NODE_3_LABEL = Node(
    templates = [
        'this movie is labelled {}, \
        why not ask me movie overview, leading actors, category, release date, or observer reviews'
    ],
    func = search_movie_labels
)
NODE_3_RELEASE_DATE = Node(
    templates = [
        'this movie is released in {}, doing well worldwide. \
        I can tell you more about observer reviews, movie overview, leading actors and category'
    ],
    func = search_movie_release_date
)
NODE_3_OVERVIEW = Node(
    templates = [
        'I am excited to share the story with you. {}'
    ],
    func = movie_overview_summary
)
NODE_3_REVIEW = Node(
    templates = ['Some observer comment: {} anyway, any other things you want to know?'],
    func = movie_review_summary
)

NODE_4_CHOOSE_ACTOR = Node(templates = ['who would you like to know more'])

NODE_5_ACTOR_INFO = Node(
    templates = ['you can know more about the birth information, biography, and other movies acted by {}'],
    func = search_actor_gender
)

NODE_6_BIRTH_INFO = Node(
    templates = ['{} was born in {}, in {}. Do you want to know more about other movies she acted?'],
    func = search_actor_birth_gender
)
NODE_6_BIOGRAPHY = Node(
    templates = ['{}, do you want to know birth information or other movies {} acted'],
    func = search_actor_bio_gender
)
NODE_6_OTHER_MOVIES = Node(
    templates = ['She also acted in {} and {}. Do you want me to tell more?'],
    func = search_actor_2_movies
)

# None 意味着不需要，any 指不能为空
dialog_mapping = {
    ROOT: {
        NODE_1_POS_OTHER: { 'sentiment': ['pos', 'other'], 'intent': None },
        NODE_1_NEG: { 'sentiment': ['neg'], 'intent': None }
    },

    NODE_1_POS_OTHER: {
        NODE_2_FAV_MOVIE_INFO: { 'sentiment': None, 'intent': None }
    },
    NODE_1_NEG: {
        NODE_2_FAV_MOVIE_INFO: { 'sentiment': None, 'intent': None }
    },

    NODE_2_FAV_MOVIE_INFO: {
        NODE_3_SUG_MOVIE: { 'sentiment': None, 'intent': 'suggestMovie' },
        NODE_3_LEAD_ACTOR: { 'sentiment': None, 'intent': 'askLeadActor' },
        NODE_3_LABEL: { 'sentiment': None, 'intent': 'askMovieLabel' },
        NODE_3_RELEASE_DATE: { 'sentiment': None, 'intent': 'askMovieReleaseDate' },
        NODE_3_OVERVIEW: { 'sentiment': None, 'intent': 'askMovieOverview' },
        NODE_3_REVIEW: { 'sentiment': None, 'intent': 'askMovieReview' }
    },
    NODE_2_MOVIE_INFO: {
        NODE_3_SUG_MOVIE: { 'sentiment': None, 'intent': 'suggestMovie' },
        NODE_3_LEAD_ACTOR: { 'sentiment': None, 'intent': 'askLeadActor' },
        NODE_3_LABEL: { 'sentiment': None, 'intent': 'askMovieLabel' },
        NODE_3_RELEASE_DATE: { 'sentiment': None, 'intent': 'askMovieReleaseDate' },
        NODE_3_OVERVIEW: { 'sentiment': None, 'intent': 'askMovieOverview' },
        NODE_3_REVIEW: { 'sentiment': None, 'intent': 'askMovieReview' }
    },

    NODE_3_SUG_MOVIE: {
        NODE_3_SUG_MOVIE: { 'sentiment': ['neg', 'other'], 'intent': 'suggestMovie' },
        NODE_3_LEAD_ACTOR: { 'sentiment': ['neg', 'other'], 'intent': 'askLeadActor' },
        NODE_3_LABEL: { 'sentiment': ['neg', 'other'], 'intent': 'askMovieLabel' },
        NODE_3_RELEASE_DATE: { 'sentiment': ['neg', 'other'], 'intent': 'askMovieReleaseDate' },
        NODE_3_OVERVIEW: { 'sentiment': ['neg', 'other'], 'intent': 'askMovieOverview' },
        NODE_3_REVIEW: { 'sentiment': ['neg', 'other'], 'intent': 'askMovieReview' },

        # MOVIE_INFO
        NODE_2_MOVIE_INFO: { 'sentiment': None, 'intent': None }
    },
    NODE_3_LABEL: {
        NODE_3_SUG_MOVIE: { 'sentiment': None, 'intent': 'suggestMovie' },
        NODE_3_LEAD_ACTOR: { 'sentiment': None, 'intent': 'askLeadActor' },
        NODE_3_LABEL: { 'sentiment': None, 'intent': 'askMovieLabel' },
        NODE_3_RELEASE_DATE: { 'sentiment': None, 'intent': 'askMovieReleaseDate' },
        NODE_3_OVERVIEW: { 'sentiment': None, 'intent': 'askMovieOverview' },
        NODE_3_REVIEW: { 'sentiment': None, 'intent': 'askMovieReview' }
    },
    NODE_3_LEAD_ACTOR: {
        NODE_3_SUG_MOVIE: { 'sentiment': None, 'intent': 'suggestMovie' },
        NODE_3_LEAD_ACTOR: { 'sentiment': None, 'intent': 'askLeadActor' },
        NODE_3_LABEL: { 'sentiment': None, 'intent': 'askMovieLabel' },
        NODE_3_RELEASE_DATE: { 'sentiment': None, 'intent': 'askMovieReleaseDate' },
        NODE_3_OVERVIEW: { 'sentiment': None, 'intent': 'askMovieOverview' },
        NODE_3_REVIEW: { 'sentiment': None, 'intent': 'askMovieReview' },

        # ACTOR_INFO
        NODE_2_MOVIE_INFO: { 'sentiment': ['neg', 'other'], 'intent': None },
        # MOVIE_INFO
        NODE_4_CHOOSE_ACTOR: { 'sentiment': ['pos'], 'intent': None }
    },
    NODE_3_RELEASE_DATE: {
        NODE_3_SUG_MOVIE: { 'sentiment': None, 'intent': 'suggestMovie' },
        NODE_3_LEAD_ACTOR: { 'sentiment': None, 'intent': 'askLeadActor' },
        NODE_3_LABEL: { 'sentiment': None, 'intent': 'askMovieLabel' },
        NODE_3_RELEASE_DATE: { 'sentiment': None, 'intent': 'askMovieReleaseDate' },
        NODE_3_OVERVIEW: { 'sentiment': None, 'intent': 'askMovieOverview' },
        NODE_3_REVIEW: { 'sentiment': None, 'intent': 'askMovieReview' }
    },
    NODE_3_OVERVIEW: {
        NODE_3_SUG_MOVIE: { 'sentiment': None, 'intent': 'suggestMovie' },
        NODE_3_LEAD_ACTOR: { 'sentiment': None, 'intent': 'askLeadActor' },
        NODE_3_LABEL: { 'sentiment': None, 'intent': 'askMovieLabel' },
        NODE_3_RELEASE_DATE: { 'sentiment': None, 'intent': 'askMovieReleaseDate' },
        NODE_3_OVERVIEW: { 'sentiment': None, 'intent': 'askMovieOverview' },
        NODE_3_REVIEW: { 'sentiment': None, 'intent': 'askMovieReview' }
    },
    NODE_3_REVIEW: {
        NODE_3_SUG_MOVIE: { 'sentiment': None, 'intent': 'suggestMovie' },
        NODE_3_LEAD_ACTOR: { 'sentiment': None, 'intent': 'askLeadActor' },
        NODE_3_LABEL: { 'sentiment': None, 'intent': 'askMovieLabel' },
        NODE_3_RELEASE_DATE: { 'sentiment': None, 'intent': 'askMovieReleaseDate' },
        NODE_3_OVERVIEW: { 'sentiment': None, 'intent': 'askMovieOverview' },
        NODE_3_REVIEW: { 'sentiment': None, 'intent': 'askMovieReview' }
    },

    NODE_4_CHOOSE_ACTOR: {
        NODE_6_BIRTH_INFO: { 'sentiment': None, 'intent': None }
    },

    NODE_6_BIRTH_INFO: {
        NODE_6_OTHER_MOVIES: { 'sentiment': None, 'intent': None }
    }

    # NODE_5_ACTOR_INFO: {
    #     NODE_6_BIRTH_INFO: { 'sentiment': None, 'intent': 'askActorBirthInfo' },
    #     NODE_6_BIOGRAPHY: { 'sentiment': None, 'intent': 'askActorBio' },
    #     NODE_6_OTHER_MOVIES: { 'sentiment': None, 'intent': 'askActorOtherMovies' }
    # },

    # NODE_6_BIRTH_INFO: {
    #     NODE_6_BIRTH_INFO: { 'sentiment': None, 'intent': 'askActorBirthInfo' },
    #     NODE_6_BIOGRAPHY: { 'sentiment': None, 'intent': 'askActorBio' },
    #     NODE_6_OTHER_MOVIES: { 'sentiment': None, 'intent': 'askActorOtherMovies' }
    # },
    # NODE_6_BIOGRAPHY: {
    #     NODE_6_BIRTH_INFO: { 'sentiment': None, 'intent': 'askActorBirthInfo' },
    #     NODE_6_BIOGRAPHY: { 'sentiment': None, 'intent': 'askActorBio' },
    #     NODE_6_OTHER_MOVIES: { 'sentiment': None, 'intent': 'askActorOtherMovies' }
    # },
    # NODE_6_OTHER_MOVIES: {
    #     NODE_2_MOVIE_INFO: { 'sentiment': None, 'intent': None }
    # }
}
