from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 6

class MyLimitOffsetPagination(LimitOffsetPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 6

class MyCursorPagination(CursorPagination):
    page_size = 4
    ordering = '-id'