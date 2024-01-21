import cv2 as cv
import numpy as np
from app import bot
from aiogram.types import FSInputFile
import os


spaces = {'hsv': cv.COLOR_BGR2HSV,
		'gray': cv.COLOR_BGR2GRAY,
		'lab': cv.COLOR_BGR2LAB}

options = {'blur': (3, 7, 7, 11, 19, 31),
		   'contrast': ((3, 3), (9, 9), (15, 15), (25, 25), (51, 51))}

rates = (10, 25, 50, 75, 100)


async def resize(img, size):
	return cv.resize(img, size)


async def read_rate(type, rate):
	rate_idx = rates.index(int(rate))
	return options[type][rate_idx]


async def change_color_space(img, space):
	return cv.cvtColor(img, spaces[space])


async def edit_photo(type, **params):
	await bot.send_message(params['id'], text=f'Обрабатываю изображение...',)
	img = cv.imread(params['path'])
	new_img = None

	if type == 'space':
		new_img = await change_color_space(img, params['space'])
	elif type == 'size':
		length, width = map(lambda x: int(x), params['size'].split('x'))
		new_img = await resize(img, (length, width))
	elif type == 'contrast':
		new_img = await increase_contrast(img, params['rate'])
	elif type == 'blur':
		new_img = await blur(img, params['rate'])

	path = os.path.join('./assets', str(params['id']) + '_new' + '.jpg')
	cv.imwrite(path, new_img)


async def delete_existing_data():
	photos = os.listdir("./assets")
	for p in photos:
		print(f'removed {os.path.join("./assets", p)}')
		os.remove(os.path.join("./assets", p))


async def send_and_delete_photo(id):
	dest = os.path.join('./assets', str(id) + '_new' + '.jpg')
	photo = FSInputFile(dest)
	await bot.send_photo(id, photo)
	os.remove(dest)


async def blur(img, rate):
	rate = await read_rate('blur', rate)
	return cv.medianBlur(img, rate)


async def increase_contrast(img, rate):
	rate = await read_rate('contrast', rate)

	lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
	l, a, b = cv.split(lab)
	clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=rate)
	cl = clahe.apply(l)
	merged = cv.merge((cl, a, b))
	enhanced_img = cv.cvtColor(merged, cv.COLOR_LAB2BGR)
	return enhanced_img