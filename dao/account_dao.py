from dao.base_dao import BaseDao


class AccountDao(BaseDao):
    def __init__(self):
        super().__init__()

    def find_by_id(self, userid):
        account = None
        try:
            with self.connect.cursor() as cursor:
                sql = 'select userid,password from accounts where userid=%s;'
                cursor.execute(sql, userid)
                row = cursor.fetchone()

                if row:
                    account = dict()
                    account['userid'] = row[0]
                    account['password'] = row[1]

        finally:
            self.connect.close()

        return account
