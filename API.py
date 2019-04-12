import pymysql
import pymysql.cursors
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from decimal import Decimal


def getConnection():
     
    # You can change the connection arguments.
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='onlyme',                             
                             db='restaurants',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection


app = Flask(__name__)
api = Api(app)

class MainMenu(Resource):
        def get(self):
                connection = getConnection()
                cursor = connection.cursor()
                cursor.execute("select * from MenuSection") # This line performs query and returns json result
                result = cursor.fetchall()
                return {'Menu Section': [i for i in result]} # Fetches first column that is Employee ID

class ItemMenu(Resource):
        def get(self, section_id):
                def decimal_default(obj):
                        if isinstance(obj, Decimal):
                                return float(obj)
                        raise TypeError
                connection = getConnection()
                cursor = connection.cursor()
                cursor.execute("select * from ItemSection where sectionID=%d" %int(section_id)) # This line performs query and returns json result
                result = cursor.fetchall()
                #print(result[0])
                lst=[]
                for x in result:
                        lst.append({'ID': x["ID"], 'title': x["title"], 'price': dumps(Decimal(x["price"]), default=decimal_default), 'sectionID': x["sectionID"]})
                #print(lst)
                return {'Menu Section': [i for i in lst]} # Fetches first column that is Employee ID


class AddMenuSection(Resource):
        def post(self):
                connection = getConnection()
                cursor = connection.cursor()
                print(request.json)
                SectionName = request.json['sectionName']
                cursor.execute("insert into MenuSection (sectionName) values ('{0}')".format(SectionName))
                connection.commit()
                connection.close()
                return {'status':'success'}


class AddItemSection(Resource):
        def post(self):
                connection = getConnection()
                cursor = connection.cursor()
                print(request.json)
                Title = request.json['title']
                Price = request.json['price']
                SectionID = request.json['sectionID']
                cursor.execute("insert into ItemSection (title,price,sectionID) values('{0}','{1}','{2}')".format(Title,Price,SectionID))
                connection.commit()
                connection.close()
                return {'status':'success'}

class UpdateMenuSection(Resource):
        def post(self):
                connection = getConnection()
                cursor = connection.cursor()
                print(request.json)
                sectionID = request.json['sectionID']
                sectionName = request.json['sectionName']
                cursor.execute("update MenuSection set sectionName='{0}' where sectionID ={1}".format(sectionName,sectionID))
                connection.commit()
                connection.close()
                return {'status':'success'}


class UpdateItemSection(Resource):
        def post(self):
                connection = getConnection()
                cursor = connection.cursor()
                print(request.json)
                ID = request.json['ID']
                title = request.json['title']
                price = request.json['price']
                sectionID = request.json['sectionID']
                cursor.execute("update ItemSection set title='{0}', price='{1}', sectionID='{2}' where ID ={3}".format(title,price,sectionID,ID))
                connection.commit()
                connection.close()
                return {'status':'success'}

class MenuSection_Name(Resource):
        def get(self, section_id):
                connection = getConnection()
                cursor = connection.cursor()
                #conn = getConnection()
                cursor.execute("select * from MenuSection where sectionID =%d "  %int(section_id))
                result = cursor.fetchall()
                return jsonify(result)


class DeleteMenuSection(Resource):
        def post(self):
                connection = getConnection()
                cursor = connection.cursor()
                sectionID = request.json['sectionID']
                cursor.execute("delete from MenuSection where sectionID ={0} ".format(sectionID))
                #result = cursor.fetchall()
                connection.commit()
                connection.close()
                return {'status':'success'}

class DeleteItemSection(Resource):
        def post(self):
                connection = getConnection()
                cursor = connection.cursor()
                ID = request.json['ID']
                cursor.execute("delete from ItemSection where ID ={0} ".format(ID))
                #result = cursor.fetchall()
                connection.commit()
                connection.close()
                return {'status':'success'}
        

api.add_resource(MainMenu, '/mainmenu') # Route_1
api.add_resource(AddMenuSection, '/addmenu') # Route_1
api.add_resource(AddItemSection, '/additem') # Route_1
api.add_resource(UpdateMenuSection, '/editmenu') # Route_1
api.add_resource(UpdateItemSection, '/edititem') # Route_1
api.add_resource(ItemMenu, '/itemmenu/<section_id>')
api.add_resource(DeleteMenuSection, '/deletemenu')
api.add_resource(DeleteItemSection, '/deleteitem')
api.add_resource(MenuSection_Name, '/menuname/<section_id>')



if __name__ == '__main__':
     app.run(port='3000')