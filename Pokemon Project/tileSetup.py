import pygame


pygame.init()

class Tilemap:
	def __init__(self, x, y, crop_list):
		self.x = x
		self.y = y
		self.crop_list = crop_list
	def generate_crops():
		crop_list = []
		x = 0
		y = 0
		for i in range(20832 * 16):
			crop_list.append((x, y, 16, 16))
			if x != 256:
				x += 16
			else:
				x = 0
				y += 16
		return crop_list

			


tile_list = Tilemap.generate_crops()
for i in range(len(tile_list)):
	print("x = ", tile_list[i][0], "\n", "y = ", tile_list[i][1])
print(len(tile_list))
