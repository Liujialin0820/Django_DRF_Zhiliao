from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size = 2

    max_page_size = 4
    # 用户自己指定一页展示多少数据
    page_size_query_param = "max_size"
    # 页码参数 默认是page
    page_query_param = "p"
    # http://127.0.0.1:8000/meituan/merchant?p=1&max_size=6
    # 返回4条数据 