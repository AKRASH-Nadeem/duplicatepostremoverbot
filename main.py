from pyrogram import Client,idle,filters
from config import session_string

app = Client("my_account",session_string=session_string)

@app.on_message((filters.channel | filters.group) & filters.command(['start']) & filters.outgoing)
async def reply_others(client,message):
    if not message.from_user.id == app.me.id:
        return
    chat_id = message.chat.id
    m_l = set()
    photo_unique_ids = set()
    video_captions = set()
    async for message in app.get_chat_history(chat_id):
        if message.text:
            if message.text in m_l:
                await message.delete()
            else:
                m_l.add(message.text)
        elif message.photo:
            if message.photo.file_unique_id in photo_unique_ids:
                await message.delete()
            else:
                photo_unique_ids.add(message.photo.file_unique_id)
            # print(message.photo)
        elif message.video:
            if message.caption in video_captions:
                # print("deleting video")
                await message.delete()
            else:
                video_captions.add(message.caption)
                # print("adding")
            # print(message)



if __name__=="__main__":
    app.start()
    app.send_message("me", "Bot Started")
    print("bot started")
    idle()
    app.stop()
