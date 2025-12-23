from  rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):

    page_size = 5     # Number of items per page (e.g., 5 posts per page)

    page_size_query_param = 'page_size'    # Allows client (Vue) to change page size via ?page_size=10

    max_page_size = 20              # Prevents client from requesting too many records at once