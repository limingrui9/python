class MusicPlayer(object):
	def __new__(cls,*a,**b):

		print("newfangfa")
		return super().__new__(cls)

	def __init__(self):
		print("initfangfa")

player = MusicPlayer()

print(player)


