from aiogram.filters.callback_data import CallbackData
from aiogram.filters import Filter
from aiogram.types import Message


class Callback(CallbackData, prefix="type"):
	text: str


class MyFilter(Filter):
	def __init__(self, my_text: str) -> None:
		self.my_text = my_text

	async def __call__(self, message: Message) -> bool:
		return message.text == self.my_text