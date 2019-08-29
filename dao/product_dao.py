from dao.base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__()

    def find_by_category(self, category):
        products = []
        try:
            with self.connect.cursor() as cursor:
                sql = 'select * from products where category=%s;'
                cursor.execute(sql, category)
                rows = cursor.fetchall()

                for row in rows:
                    product = dict()
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['listprice'] = row[6]
                    product['unitcost'] = row[7]
                    products.append(product)

        finally:
            self.connect.close()

        return products

    def find_all(self):
        products = []
        try:
            with self.connect.cursor() as cursor:
                sql = 'select * from products;'
                cursor.execute(sql)
                rows = cursor.fetchall()

                for row in rows:
                    product = dict()
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['listprice'] = row[6]
                    product['unitcost'] = row[7]
                    products.append(product)

        finally:
            self.connect.close()

        return products

    def find_by_id(self, productid):
        product = None
        try:
            with self.connect.cursor() as cursor:
                sql = 'select * from accounts where productid=%s;'
                cursor.execute(sql, productid)
                row = cursor.fetchone()

                if row:
                    product = dict()
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['unitcost'] = row[7]

        finally:
            self.connect.close()

        return product
