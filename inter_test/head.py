# coding:utf-8


class Headers:
    @staticmethod
    def headinfo():
        Authorization = 'Bearer 4 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyYW5kb20iOiJZWk5ybUt0MmlGY2x5RTFFUGJnOFc4MUZIWk5yaWY2IiwiaWQiOiI2Njk5MTg2OTU3NDc1NTIwNTEyIiwiaXNzIjoiMjU4NzYuY29tIiwiZXhwIjoxNTk4MDU2NjM1fQ.-fdN_LJclXppotnkx_UTfVb_K1aGXAuQeL_lXgK532c'
        # 头部信息
        header = {'Content-Type': 'application/json',
                  'Authorization': Authorization,
                  'sycm': '1_1597210637177_447e4'}
        return header


