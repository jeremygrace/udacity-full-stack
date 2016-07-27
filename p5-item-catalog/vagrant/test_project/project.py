from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup2 import Base, Restaurant, MenuItem
# Create Flask instance
app = Flask(__name__)

# Connect to Restaurantmenu.db
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

# Establish Active session
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Assign decorators
@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
	output = ""
	for i in items:
		output += i.name
		output += '</br>'
		output += i.price
		output += '</br>'
		output += i.description
		output += '</br></br>'
	return output

@app.route('/restaurants/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
	return "page ro create a new menu item. Task 1 COMPLETE!"

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
	return "page to edite a menu item. Task 2 COMPLETE!"

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
	return "page to delete a menu item. Task 3 COMPLETE!"



if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)