##微信证件照助手 利用paddleseg进行图像分割来完成背景换底

import os
import asyncio
from imgchange import image_change##导入人脸分割函数

from wechaty import (
    Contact,
    FileBox,
    Message,
    Wechaty,
    ScanStatus,
)
robot_state = 0 #机器人状态


async def on_message(msg: Message):
    talker = msg.talker()
    global robot_state
    if msg.text() == 'ding':
        await msg.say('这是自动回复: dong dong dong')
    if msg.text() == 'hi' or msg.text() == '你好' or msg.text()=='救救我' or msg.text()=='请求帮助':
        await talker.say('你好，这里是证件照小帮手，是否平时已经厌烦了各种证件照底色要求呢？别担心 小助手来帮你~(๑•̀ㅂ•́)و✧\n你可以回复更换证件照底色或前往其他星球来获得服务。（例如 去火星）')

    if msg.text() == '再见':
        await talker.say('很高兴为您服务，祝您生活愉快！')
    if msg.text() == '更换证件照底色':
        await talker.say('已收到证件照更换底色需求，请发送要更换的底色，如：蓝色，红色，白色，黑色！')
    if msg.text() == '白色':
        robot_state = 2
        await talker.say('已准备好将证件照更换为白底证件照，请发送图片')
    if msg.text() == '蓝色':
        robot_state = 3
        await talker.say('已准备好将证件照更换为蓝底证件照，请发送图片')
    if msg.text() == '红色':
        robot_state = 4
        await talker.say('已准备好将证件照更换为红底证件照，请发送图片')
    if msg.text() == '黑色':
        robot_state = 5
        await talker.say('已准备好将证件照更换为黑底证件照，请发送图片')
    if msg.text() == '去月球':
        robot_state = 6
        await talker.say('已准备带你传送到月球，请发送照片')
    if msg.text() == '去火星':
        robot_state = 7
        await talker.say('已准备带你前往火星，请发送照片')
    if msg.text() == '去天王星':
        robot_state = 8
        await talker.say('已准备好带你前往天王星，请发送照片')
     
    
    if robot_state == 2 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  更换白底护照
        await talker.say('已收到图像，开始更换中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './image/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        bg_path = './data/white.jpg'
        image_change(img_path,bg_path)

        file_box_final_result = FileBox.from_file('./output/'+img_name)
        robot_state = 0
        await talker.say('更换完成!')
        await msg.say(file_box_final_result)
    if robot_state == 3 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  更换蓝底证件照
        await talker.say('已收到图像，开始更换中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './image/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        bg_path = './data/blue.jpg'
        image_change(img_path,bg_path)

        file_box_final_result = FileBox.from_file('./output/'+img_name)
        robot_state = 0
        await talker.say('更换完成!')
        await msg.say(file_box_final_result)
    if robot_state == 4 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  更换红底证件照
        await talker.say('已收到图像，开始更换中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './image/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        bg_path = './data/red.jpg'
        image_change(img_path,bg_path)

        file_box_final_result = FileBox.from_file('./output/'+img_name)
        robot_state = 0
        await talker.say('更换完成!')
        await msg.say(file_box_final_result)
    if robot_state == 5 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  更换黑底证件照
        await talker.say('已收到图像，开始更换中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './image/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        bg_path = './data/black.jpg'
        image_change(img_path,bg_path)

        file_box_final_result = FileBox.from_file('./output/'+img_name)
        robot_state = 0
        await talker.say('更换完成!')
        await msg.say(file_box_final_result)
    if robot_state == 6 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  更换月球背景
        await talker.say('已收到图像，开始更换中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './image/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        bg_path = './data/yueqiu.jpg'
        image_change(img_path,bg_path)

        file_box_final_result = FileBox.from_file('./output/'+img_name)
        robot_state = 0
        await talker.say('更换完成!')
        await msg.say(file_box_final_result)
    if robot_state == 7 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  更换火星背景
        await talker.say('已收到图像，开始更换中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './image/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        bg_path = './data/huoxin.jpg'
        image_change(img_path,bg_path)

        file_box_final_result = FileBox.from_file('./output/'+img_name)
        robot_state = 0
        await talker.say('更换完成!')
        await msg.say(file_box_final_result)
    if robot_state == 8 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  更换天王星背景
        await talker.say('已收到图像，开始更换中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
    
        # 获取图片名
        img_name = file_box_user_image.name
    
        # 图片保存的路径
        img_path = './image/' + img_name
    
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        bg_path = './data/tianwangxin.jpg'
        image_change(img_path,bg_path)

        file_box_final_result = FileBox.from_file('./output/'+img_name)
        robot_state = 0
        await talker.say('更换完成!')
        await msg.say(file_box_final_result)

    

async def on_scan(
        qrcode: str,
        status: ScanStatus,
        _data,
):
    print('Status: ' + str(status))
    print('View QR Code Online: https://wechaty.js.org/qrcode/' + qrcode)


async def on_login(user: Contact):
    print(user)


async def main():
    # 确保我们在环境变量中设置了WECHATY_PUPPET_SERVICE_TOKEN
    if 'WECHATY_PUPPET_SERVICE_TOKEN' not in os.environ:
        print('''
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        ''')

    bot = Wechaty()

    bot.on('scan',      on_scan)
    bot.on('login',     on_login)
    bot.on('message',   on_message)

    await bot.start()

    print('[Python Wechaty] Ding Dong Bot started.')


asyncio.run(main())