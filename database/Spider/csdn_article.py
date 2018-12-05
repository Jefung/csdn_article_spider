from sqlalchemy import *
from sql_factory.base_table import BaseTable


class CsdnArticle(BaseTable):
    table_columns = [
        Column('id', String(50), primary_key=True),
        Column('title', String(50)),
        Column('author', String(50)),
        Column('time', String(50)),
        Column('read_count', String(50)),
        Column('tags', String(255)),
        Column('content', TEXT),
    ]

    def is_exists(self, article_id: str, post_time: str = None) -> bool:
        res = self.get("id = " + article_id)
        if len(res) > 0:
            if post_time is not None and res[0]["time"] < post_time:
                return False
            return True
        else:
            return False
