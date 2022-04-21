from robohash import Robohash

# hash = "whatever-hash-you-want"

def create_robot(hash):
	rh = Robohash(hash)
	rh.assemble(roboset='set1')
	with open("./static/robots/robotimage.png", "wb") as f:
		rh.img.save(f, format="png")

