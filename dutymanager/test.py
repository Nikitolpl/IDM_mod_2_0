from vkbottle.user import User, Message

user = User("da0f2da472f050977ddfc33dec8d5414797371305081a3ef009a631d139cd2bd5d9c3a7bdea06616824e8")


@user.on.message_handler(text="!лп тест")
async def wrapper(ans: Message):
    print("Что-то получиили")
    await user.api.messages.edit(
        peer_id=ans.peer_id,
        message_id=ans.message_id,
        message="Тест пройден!"
    )


user.run_polling()
