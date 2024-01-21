from aiogram.utils.keyboard import InlineKeyboardBuilder
from classes import *


kb_filters = InlineKeyboardBuilder()
kb_filters.button(text=f"Изменить размер", callback_data=Callback(text='size').pack())
kb_filters.button(text=f"Изменить цветосхему", callback_data=Callback(text='space').pack())
kb_filters.button(text=f"Увеличить контрастность", callback_data=Callback(text='contrast').pack())
kb_filters.button(text=f"Размыть", callback_data=Callback(text='blur').pack())
kb_filters.adjust(2, 2)

kb_spaces = InlineKeyboardBuilder()
kb_spaces.button(text=f"Черно-белый", callback_data=Callback(text='gray').pack())
kb_spaces.button(text=f"HSV", callback_data=Callback(text='hsv').pack())
kb_spaces.button(text=f"LAB", callback_data=Callback(text='lab').pack())
kb_spaces.adjust(1, 2)

kb_contrast = InlineKeyboardBuilder()
kb_contrast.button(text=f"10%", callback_data=Callback(text='10c').pack())
kb_contrast.button(text=f"25%", callback_data=Callback(text='25c').pack())
kb_contrast.button(text=f"50%", callback_data=Callback(text='50c').pack())
kb_contrast.button(text=f"75%", callback_data=Callback(text='75c').pack())
kb_contrast.button(text=f"100%", callback_data=Callback(text='100c').pack())
kb_contrast.adjust(3, 2)

kb_blur = InlineKeyboardBuilder()
kb_blur.button(text=f"10%", callback_data=Callback(text='10b').pack())
kb_blur.button(text=f"25%", callback_data=Callback(text='25b').pack())
kb_blur.button(text=f"50%", callback_data=Callback(text='50b').pack())
kb_blur.button(text=f"75%", callback_data=Callback(text='75b').pack())
kb_blur.button(text=f"100%", callback_data=Callback(text='100b').pack())
kb_blur.adjust(3, 2)
