import pygame


pygame.init()

def generate_crops():
	crop_list = []
	x = 0
	y = 0
	while y != 20832:
		if x != 256:
			crop_list.append((x, y, 16, 16))
			x += 16
		else:
			x = 0
			y += 16
	return crop_list

			

crop_list = generate_crops()
for i in range(len(crop_list)):
	print(crop_list[i])
print(len(crop_list))