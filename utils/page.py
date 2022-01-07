"""分页相关"""

from tortoise.queryset import QuerySet


def make_page(queryset: QuerySet, *, cur_page: int, per_page: int) -> QuerySet:
    """分页

    :param queryset: QuerySet
    :param cur_page: 当前页号
    :param per_page: 每页显示数量
    """
    return queryset.offset((cur_page - 1) * per_page).limit(per_page)
