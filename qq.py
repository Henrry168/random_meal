from mirai import Mirai, WebSocketAdapter, FriendMessage, Startup, Shutdown
#from apscheduler.schedulers.asyncio import AsyncIOScheduler
#from apscheduler.trigger.cron import CronTrigger

import main

bot = Mirai(
    qq=485036798,  # 改成你的机器人的 QQ 号
    adapter=WebSocketAdapter(
        verify_key='233123', host='localhost', port=8080
    )
)
"""
scheduler = AsyncIOScheduler()

@bot.on(Startup)
def start_scheduler(_):
    scheduler.start() # 启动定时器

@bot.on(Shutdown)
def stop_scheduler(_):
    scheduler.shutdown(True) # 结束定时器

@scheduler.scheduled_job(CronTrigger(hour=17, minute=36))
async def timer():
    await bot.send_group_message(1021229748,  main.最终文本())
"""

@bot.on(FriendMessage)
async def on_friend_message(event: FriendMessage):
    if str(event.message_chain) == '吃点啥':
        return bot.send(event, main.最终文本())

bot.run()
