from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = 'size'
    max_page_size = 3
    last_page_strings = ('end',)

class WatchListLOPagination(LimitOffsetPagination):
    default_limit =3
    offset_query_param = 'start'
    max_limit = 3


class WatchListCPagination(CursorPagination):
    page_size = 3
    ordering = 'created'

