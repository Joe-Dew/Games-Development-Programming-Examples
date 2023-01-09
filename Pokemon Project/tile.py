import pygame
import json
import tileSetup

pygame.init()
surface = pygame.display.set_mode((1600, 1600))


class Tile:
	def __init__(tile_set, json_file, layer_num):
		self.tile_set = tile_set
		self.json_file = json_file
		self.layer_num = layer_num
	def loadLayer(tile_set, json_file, layer_num):
		with open(json_file, "r") as file:
			data = json.load(file)
			print(data["layers"][layer_num]["data"][0])
			tile = pygame.image.load(tile_set[data["layers"][layer_num]["data"][0] - 18376])
			return tile

 
tile = Tile.loadLayer(tileSetup.Tilemap.tile_setup("C:/Users/josep/Dropbox/PC/Downloads/Pokemon.png", (16, 16)), "Roanoke Town.json", 0)
game = False
while not game:
	pygame.display.update()

	surface.blit(tile, (800, 800))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

