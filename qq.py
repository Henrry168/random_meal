from mirai import Mirai, WebSocketAdapter, GroupMessage, FriendMessage
import main
if __name__ == '__main__':
    bot = Mirai(
        qq=485036798, # 改成你的机器人的 QQ 号
        adapter=WebSocketAdapter(
            verify_key='233123', host='localhost', port=8080
        )
    )

    @bot.on(GroupMessage)
    def on_group_message(event: GroupMessage):
        if str(event.message_chain) == '今天吃点啥':
            return bot.send(event, main.最终文本())

    @bot.on(FriendMessage)
    async def on_friend_message(event: FriendMessage):
        if str(event.message_chain) == '今天吃点啥':
            return bot.send(event, main.最终文本())

    bot.run()