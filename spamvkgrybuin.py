import vkbee
import asyncio
import time

###Connector#####
tocken= 'Сюды ваш токен,с этими ковычками - '
ownid = 'сюда ваш айди(Пример: 343076755)без  этих ковычек--> '
psid = 'сюда пост айди(Пример:261...)без этих ковычек--> '
###Completed#####






async def main(loop):
    vk=vkbee.VkApi(
        tocken,loop=loop
    )
    while True:
        a=await vkbee.VkApi.call(vk,'wall.createComment',{'owner_id':ownid,'post_id':psid,'sticker_id':14084})
        print(a)
        time.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
