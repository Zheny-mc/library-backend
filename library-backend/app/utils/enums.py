from enum import Enum

class Genre(Enum):
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE_FICTION = "Science Fiction"
    FANTASY = "Fantasy"
    MYSTERY = "Mystery"
    THRILLER = "Thriller"
    ROMANCE = "Romance"
    HORROR = "Horror"
    BIOGRAPHY = "Biography"
    HISTORY = "History"
    SCIENCE = "Science"
    TECHNOLOGY = "Technology"
    BUSINESS = "Business"
    SELF_HELP = "Self-Help"
    CHILDREN = "Children"
    YOUNG_ADULT = "Young Adult"
    POETRY = "Poetry"
    DRAMA = "Drama"
    COMEDY = "Comedy"
    ADVENTURE = "Adventure"
    CRIME = "Crime"
    DOCUMENTARY = "Documentary"

class Language(Enum):
    RUSSIAN = "Russian"
    ENGLISH = "English"
    SPANISH = "Spanish"
    FRENCH = "French"
    GERMAN = "German"
    ITALIAN = "Italian"
    PORTUGUESE = "Portuguese"
    CHINESE = "Chinese"
    JAPANESE = "Japanese"
    KOREAN = "Korean"
    ARABIC = "Arabic"
    HINDI = "Hindi"
    TURKISH = "Turkish"
    POLISH = "Polish"
    UKRAINIAN = "Ukrainian"
    BELARUSIAN = "Belarusian"
    KAZAKH = "Kazakh"
    UZBEK = "Uzbek"

def get_genres():
    return [{'value': genre.name, 'label': genre.value} for genre in Genre]

def get_languages():
    return [{'value': lang.name, 'label': lang.value} for lang in Language]

def get_genre_by_name(name):
    try:
        return Genre[name.upper()]
    except KeyError:
        return None

def get_language_by_name(name):
    try:
        return Language[name.upper()]
    except KeyError:
        return None
