from mirai import Mirai, WebSocketAdapter, FriendMessage, Startup, Shutdown

import main

bot = Mirai(
    qq=485036798,  # 改成你的机器人的 QQ 号
    adapter=WebSocketAdapter(
        verify_key='233123', host='localhost', port=8080
    )
)


@bot.on(Startup)
async def start_scheduler(_):
    await bot.send_group_message(1021229748,  main.最终文本())


@bot.on(FriendMessage)
async def on_friend_message(event: FriendMessage):
    if str(event.message_chain) == '吃点啥':
        return bot.send(event, main.最终文本())

bot.run()
