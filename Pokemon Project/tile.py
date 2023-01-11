import pygame
import json
import tileSetup

pygame.init()
surface = pygame.display.set_mode((816, 816))


class Tile:
	def __init__(self, json_file, layer_num, tileSet, surface):
		self.json_file = json_file
		self.layer_num = layer_num
		self.tileSet = tileSet
		self.surface = surface
	def setupLayer(self, json_file, layer_num):
		with open(json_file, "r") as file:
			data = json.load(file)
			tile = data["layers"][layer_num]["data"][0]
			tileSet = pygame.image.load("Pokemon.png")
			return tile, tileSet
	def loadLayer(self, json_file, layer_num, tileSet, surface):
		with open(json_file, "r") as file:
			data = json.load(file)
			image = pygame.image.load(tileSet)
			tileList = tileSetup.generate_crops()
			x = 0
			y = 0
			count = 0
			for i in range(data["height"]):
				for j in range(data["width"]):
					surface.blit(image, (x, y), tileList[data["layers"][layer_num]["data"][count - 1] - 1])
					pygame.display.update()
					x += 16
					count = count + 1
				x = 0
				y += 16
	def load(json_file):
		with open(json_file, "r") as file:
			data = json.load(file)
			for i in range(len(data("layers"))):
				layer = Tile(json_file, i, "Pokemon.png", surface)
				layer.loadLayer(json_file, i, "Pokemon.png", surface)


tileSet = Tile("Roanoke Town.json", 0, "Pokemon.png", surface)

tile, tileSet = tileSet.setupLayer("test2.json", 0)

layer = Tile("Roanoke Town.json", 0, "Pokemon.png", surface)
layer.loadLayer("Roanoke Town.json", 0, "Pokemon.png", surface)
layer.loadLayer("Roanoke Town.json", 1, "Pokemon.png", surface)

game = False
while not game:
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

