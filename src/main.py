from handlers import router
import asyncio
from app import bot, dp
from utils import delete_existing_data


async def main():
	dp.include_router(router)
	await delete_existing_data()
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


asyncio.run(main())