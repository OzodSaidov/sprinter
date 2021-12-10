from django.core.cache import cache
BASKET_SESSION_ID = "BASKET_SESSION_ID"


def get_or_create_session():
    """ Create dict in redis to keep session """

    if cache.get(BASKET_SESSION_ID):
        return cache.get(BASKET_SESSION_ID)
    else:
        cache.set(BASKET_SESSION_ID, {}, timeout=3600)
        return cache.get(BASKET_SESSION_ID)


def update_session(session, basket):
    """ Update session """

    basket_session = cache.get(BASKET_SESSION_ID)
    basket_session[session] = basket
    cache.set(BASKET_SESSION_ID, basket_session, timeout=3600)


def get_basket(session):
    """ Get basket of user by session key """

    basket_session = cache.get(BASKET_SESSION_ID)
    if basket_session.get(session) is not None:
        basket = basket_session.get(session)
    else:
        basket = []
        update_session(session=session, basket=basket)
    return basket


def delete_basket(session):
    """ Delete basket from session """

    basket_session = cache.get(BASKET_SESSION_ID)
    if basket_session.get(session) is not None:
        basket_session.pop(session)
        cache.set(BASKET_SESSION_ID, basket_session, timeout=3600)
