from flask_frozen import Freezer
from website import app

freezer = Freezer(app)

# @freezer.register_generator
# def home():
# 	yield '/home'

# @freezer.register_generator
# def projects():
# 	yield '/projects'

# @freezer.register_generator
# def photography():
# 	yield '/photography'

# @freezer.register_generator
# def teaching():
# 	yield '/teaching'

# @freezer.register_generator
# def traveling():
# 	yield '/traveling'

if __name__ == '__main__':
	freezer.run(debug=True)

