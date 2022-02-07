from rest_framework import pagination


class KappazonPagination(pagination.PageNumberPagination):
    """
    Custom pagination class for Kappazon API:

    - Use the page query param to modify the current page
    - Use the limit query param to modify the number of items shown in each page. Max is 100.
    """

    page_query_param = 'page'
    page_size_query_param = 'limit'
    max_page_size = 100
