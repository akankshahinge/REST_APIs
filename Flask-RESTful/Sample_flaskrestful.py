from flask import flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

items = []

class Item(Resource):
  def get(self,name):
   for item in items:
    if item['name']==name:       [We can use filter function to filter data ie. item=next(filter(lamda x:x['name']==name,items),None)]
      return item
    return {'item':None}, 404    [return {'item':item}, 200 if item else 404]

  def post(self,name):
    data=request.get_json(silent=True)
    item={'name':'name','price':data['price']}
    items.append(item)
    return item, 201
  
  def delete(self, name):
    global items
    items=list(filter(lamda x:x['name']!=name,items))
    return {'message':'Item deleted'}
  
  def put(self,name):
    data=request.get_json()
    item=next(filter(lamda x:x['name']==name,items),None)
    if item is None:
      item={'name':name,'price':data['price']}
      items.append(item)
    else: 
      item.update(data)
    
  
class ItemList(Resource):
  def get(self):
    return {'items':items}
   
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port=5000, debug=True)
   
  
