from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
import kb as kb
from classes import *
from app import bot
from utils import edit_photo, send_and_delete_photo
import os


router = Router()


@router.message(CommandStart())
async def start_handler(msg: Message):
	await msg.answer("Привет! Я могу провести некоторые операции с твоей картинкой, например изменить размер или цветовой формат. Просто отправь мне нужное изображение")


@router.message(Command('space'))
async def color_space_handler(msg: Message):
	await bot.send_message(msg.from_user.id,
	   text=f'В какой цветовой формат перевести изображение?',
	   reply_markup=kb.kb_spaces.as_markup())


@router.message(Command('size'))
async def size_handler(callback_query: CallbackQuery):
	await bot.send_message(callback_query.from_user.id,
		text=f'Введи размер изображения в формате 1200x600\n1200 - длина, 600 - высота в пикселях:',)


@router.message(Command('blur'))
async def blur_handler(callback_query: CallbackQuery):
	await bot.send_message(callback_query.from_user.id,
	   text=f'Выбери степень размытия:',
	   reply_markup=kb.kb_blur.as_markup())


@router.message(Command('contr'))
async def contrast_handler(callback_query: CallbackQuery):
	await bot.send_message(callback_query.from_user.id,
   		text=f'Выбери степень увеличения контрастности:',
   		reply_markup=kb.kb_contrast.as_markup())


@router.message(F.photo)
async def photo_handler(msg: Message):
	path = os.path.join('./assets', str(msg.from_user.id)+'.jpg')
	await bot.download(msg.photo[-1].file_id, destination=path)
	await msg.answer('Фото получено! Что мне необходимо сделать?', reply_markup=kb.kb_filters.as_markup())


@router.callback_query(Callback.filter(F.text == 'space'))
async def color_space_handler(callback_query: CallbackQuery):
	await bot.send_message(callback_query.from_user.id,
		text=f'В какой цветовой формат перевести изображение?',
		reply_markup=kb.kb_spaces.as_markup())


@router.callback_query(Callback.filter(F.text == 'size'))
async def size_handler(callback_query: CallbackQuery):
	await bot.send_message(callback_query.from_user.id,
		text=f'Введи размер изображения в формате 1200x600\n1200 - длина, 600 - высота в пикселях:',)


@router.callback_query(Callback.filter(F.text == 'contrast'))
async def contrast_handler(callback_query: CallbackQuery):
	await bot.send_message(callback_query.from_user.id,
   		text=f'Выбери степень увеличения контрастности:',
   		reply_markup=kb.kb_contrast.as_markup())


@router.callback_query(Callback.filter(F.text == 'blur'))
async def blur_handler(callback_query: CallbackQuery):
	await bot.send_message(callback_query.from_user.id,
	   text=f'Выбери степень размытия:',
	   reply_markup=kb.kb_blur.as_markup())


@router.callback_query(Callback.filter(F.text.in_({'gray', 'hsv', 'lab'})))
async def callback_query_handler(callback_query: CallbackQuery):
	path = os.path.join('./assets', str(callback_query.from_user.id) + '.jpg')
	await edit_photo(type='space', id=callback_query.from_user.id, path=path, space=callback_query.data[5:])
	await send_and_delete_photo(callback_query.from_user.id)


@router.message(F.text.lower().regexp(r'\d+x\d+'))
async def size_handler(msg: Message):
	path = os.path.join('./assets', str(msg.from_user.id) + '.jpg')
	await edit_photo(type='size', id=msg.from_user.id, path=path, size=msg.text)
	await send_and_delete_photo(msg.from_user.id)


@router.callback_query(Callback.filter(F.text.in_({'10c', '25c', '50c', '75c', '100c'})))
async def contrast_rate_handler(callback_query: CallbackQuery):
	path = os.path.join('./assets', str(callback_query.from_user.id) + '.jpg')
	await callback_query.answer(callback_query.data[5:-1])
	await edit_photo(type='contrast', id=callback_query.from_user.id, path=path, rate=callback_query.data[5:-1])
	await send_and_delete_photo(callback_query.from_user.id)


@router.callback_query(Callback.filter(F.text.in_({'10b', '25b', '50b', '75b', '100b'})))
async def blur_rate_handler(callback_query: CallbackQuery):
	await callback_query.answer(callback_query.data[5:-1])
	path = os.path.join('./assets', str(callback_query.from_user.id) + '.jpg')
	await edit_photo(type='blur', id=callback_query.from_user.id, path=path, rate=callback_query.data[5:-1])
	await send_and_delete_photo(callback_query.from_user.id)


@router.message(F.text)
async def message_handler(msg: Message):
	await msg.answer(f'Извини, не понимаю (')
