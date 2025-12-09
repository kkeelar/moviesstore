from django import template

register = template.Library()


RATING_ORDER = {
    'G': 0,
    'PG': 1,
    'PG-13': 2,
    'R': 3,
}


@register.filter(name='rating_allows')
def rating_allows(max_rating, movie_rating):
    """
    Returns True if a movie_rating is allowed under the provided
    max_rating. If max_rating is falsy (anonymous users), allow all.
    """
    if not movie_rating:
        return True
    if not max_rating:
        return True
    return RATING_ORDER.get(movie_rating, 99) <= RATING_ORDER.get(max_rating, 99)
