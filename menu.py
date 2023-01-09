import pygame
import time

pygame.init()


class Button:
	def __init__(self, rect, col, width):
		self.rect = rect
		self.col = col
		self.width = width
	def draw(self, surface):
		pygame.draw.rect(surface, self.col, self.rect, self.width)
	def validate(self, mousepos):
		return self.rect[0] <= mousepos[0] <= self.rect[0] + self.rect[2] and self.rect[1] <= mousepos[1] <= self.rect[1] + self.rect[3]
	

class Menu:
	def __init__(self, text, font, col):
		self.text = text
		self.font = font
		self.col = col
	def build(self, surface, col):
		surface.fill(self.col)
	def drawText(self, surface, font, text, text_col, text_pos):
		self.font = pygame.font.Font(font[0], font[1])
		self.text = self.font.render(text, True, text_col[0], text_col[1])
		surface.blit(self.text, text_pos)
	def button_place(self, surface, button):
		self.button.draw(self.surface)


class Scene:
	def __init__(self):
		self.elements = []
	def add_element(self, *elements):
		for e in elements:
			self.elements.append(e)
	def render(self, surface):
		for e in self.elements:
			e.draw(surface)


load_button = Button([50, 250, 125, 30], (255, 0, 0), 0)
new_button = Button([50, 300, 125, 30], (255, 0, 0), 0)
options_button = Button([50, 350, 125, 30], (255, 0, 0), 0)
start = Scene()
start.add_element(new_button, options_button, load_button)

text = "Pokemon Placeholder"
font = (None, 40)
menu = Menu(text, font, (0, 0, 0))


def start_menu(surface):
	advance = False
	menu.build(surface, (0, 0, 0))
	start.render(surface)
	menu.drawText(surface, font, text, ((255, 0, 0), (0, 0, 0)), (150, 100))
	pos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			for element in start.elements:
				if element.validate(pos):
					element.col = (0, 255, 0)
					start.render(surface)
					pygame.display.update()
					if element == start.elements[2]:
						time.sleep(0.3)
						advance = True
		if event.type == pygame.MOUSEBUTTONUP:
			for element in start.elements:
				element.col = (255, 0, 0)
	return advance


advance_button = Button([50, 250, 125, 30], (255, 0, 0), 0)
back_button = Button([50, 300, 125, 30], (255, 0, 0), 0)
inter = Scene()
inter.add_element(advance_button, back_button)

text_2 = "Badges:"
font_2 = (None, 40)
menu_2 = Menu(text_2, font_2, (0, 0, 0))


def intermediate(surface):
	advance = True
	tile_proceed = False
	menu_2.build(surface, (0, 0, 0))
	inter.render(surface)
	menu_2.drawText(surface, font_2, text_2, ((255, 0, 0), (0, 0, 0)), (100, 100))
	pos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			for element in inter.elements:
				if element.validate(pos):
					element.col = (0, 255, 0)
					inter.render(surface)
					pygame.display.update()
					if element == inter.elements[1]:
						time.sleep(0.3)
						advance = False
		if event.type == pygame.MOUSEBUTTONUP:
			for element in inter.elements:
				element.col = (255, 0, 0)
	return tile_proceed, advance