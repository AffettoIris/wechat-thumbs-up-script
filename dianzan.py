import pyautogui
import pyperclip
from pynput.keyboard import Controller, Key
import time
import sys
import random
import math

# 所有变动大的参数与值都提到这儿了
plantime = "2023-2-3 10:00:01"
myprofile = 'fox.png'
latestHead = (46, 170)
interval = 240

plantime = time.mktime(time.strptime(plantime, "%Y-%m-%d %H:%M:%S"))
pyautogui.PAUSE = 1
# 每五分钟重进朋友圈才能刷新盆友圈
# 进入朋友圈函数
def gotogate():
    if pyautogui.locateOnScreen('gateAbove.png'):
        gateAbove: object = pyautogui.locateOnScreen('gateAbove.png')
        gateX, gateY, gateWidth, gateWeight = gateAbove
        pyautogui.moveTo(gateAbove, duration=1)
        pyautogui.move(0, 50, duration=1)
        pyautogui.click()
    else:
        print("{} 未成功进入朋友圈".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        print("{} 退出程序".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        sys.exit()

# 返回颜色，注意我怕报错将过滤None值
def firsterpixel():
    if pyautogui.screenshot():
        shot = pyautogui.screenshot()
        # 在我布局不变时，(46, 170)是最新朋友圈推送者的中心像素点
        latestHeadGRB = shot.getpixel((46, 170))
        return latestHeadGRB
    else:
        print("{} 全屏截图失败，返回None值".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        return None

# 判rgb等函数
def rgbequals(oldrgb, newrgb):
    if newrgb != None:
        if oldrgb == newrgb:
            print("{} 颜色一样".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            return False
        else:
            print("{} 颜色不一样，说明换新榜首了".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            return True
    else:
        print("{} 由于上一步截全屏错误，本步返回False".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        return False

# 点赞函数。现在是后期，加入
def like():
    if pyautogui.locateOnScreen('DoubleDots.png'):
        latestDot = pyautogui.locateOnScreen('DoubleDots.png')
        x, y, width, height = latestDot
        print("{} 成功找到点点".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        pyautogui.click(x=(x + 10), y=(y + 10), button='left', duration=1)
        if pyautogui.locateOnScreen('love.png'):
            love = pyautogui.locateOnScreen('love.png')
            pyautogui.click(pyautogui.center(love), button='left', duration=1)
            print("{} 已点赞".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            # 评论功能
            # 加入if报错（暂不想学try抓错）
            pyautogui.moveTo(pyautogui.center(latestDot), duration=1)
            pyautogui.click()
            pyautogui.move(-74, 0, duration=1)
            pyautogui.click()
            print("{} 成功打开评论区".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            if pyautogui.locateOnScreen("commentbutton.png"):
                commentbutton = pyautogui.locateOnScreen("commentbutton.png")
                print("{} 成功定位发送按钮".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
                pyautogui.moveTo(pyautogui.center(commentbutton), duration=1)
                pyautogui.move(0, -37, duration=0.5)
                pyautogui.click()
                # 先做死评论，然后加入根据时间说早上好
                print("{} 准备打印评论".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
                typewords()
                print("{} 完成打印评论".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
                if pyautogui.locateOnScreen('gobutton.png'):
                    gobutton = pyautogui.locateOnScreen('gobutton.png')
                    pyautogui.moveTo(pyautogui.center(gobutton), duration=1)
                    pyautogui.click()
                    print("{} 已发送留言".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
                else:
                    print("{} 未能定位绿色的发送按钮".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            else:
                print("{} 未能定位发送按钮".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        else:
            pyautogui.click(x=(x + 50), y=(y + 20), button='left', duration=1)
            print("{} 点赞图标未识别成功，不能点赞".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
    else:
        print("{} 点点图标未识别成功".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))

def typewords():
    # today = time.strftime('%Y年%m月%d日 %H:%M:%S', time.localtime(time.time()))
    hour = time.strftime('%H', time.localtime(time.time()))
    pyautogui.click()
    keyboard = Controller()
    if hour in ['19', '20', '21', '22', '23', '24', '00', '01', '02', '03', '04', '05']:
        keyboard.type('朋友,晚上好呀!')
        time.sleep(5)
    elif hour in ['06', '07', '08', '09', '10']:
        keyboard.type('朋友,早上好呀!')
        time.sleep(5)
    elif hour in ['11', '12', '13']:
        keyboard.type('朋友,中午好呀!')
        time.sleep(5)
    else:
        keyboard.type('朋友,下午好呀!')
        time.sleep(5)
    time.sleep(1)
    print("{} 打印前须知，机器的打字有自己的中英文输入法状态，请留意需要切换到英文输入法".format(
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    str = '我是主人开发的beta版点赞机器人，主人有事在忙，请允许我代替主人为您点赞留言'
    for c in str:
        keyboard.type(c)
        time.sleep(0.7)
    pyautogui.move(1, 0)
    pyautogui.hotkey('ctrl', 'enter')
    poems = ['流年，长短皆逝。浮生，往来皆客。Hello, my boy or girl[哇]', '哇，算你厉害[哇]',
             '水晶帘动微风起，满架蔷薇一院香。愿我们岁月静好。', '斯人若彩虹，遇上方知有[哇]',
             '陌上人如玉，公子世无双。原来说的就是阁下呀[哇]', '[哇]', '哇塞，赞[哇]', '太棒了，无话可说[哇]']
    j = math.floor(random.random() * len(poems))
    print("{} 即将打印poems[{}]".format(
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), j))
    for c in poems[j]:
        keyboard.type(c)
        time.sleep(0.7)
    time.sleep(1)
    pyautogui.move(1, 0)

# 关闭键的x坐标与头像有固定值差距，y坐标更固定值
# 只需要稍微scroll以确保有头像，就可以找到关闭键
def closecircle():
    time.sleep(interval)
    pyautogui.scroll(2000)
    if pyautogui.locateOnScreen('fox.png'):
        fox = pyautogui.locateOnScreen('fox.png')
        xx, yy = pyautogui.center(fox)
        pyautogui.moveTo((xx + 36), 23, duration=1)
        pyautogui.click()
        return True
    else:
        print("{} 定位头像失败".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        return False

def mainthread():
    gotogate()
    pyautogui.scroll(-400, 1)
    global newrgb
    newrgb = firsterpixel()
    if (i == 0):
        global oldrgb
        oldrgb = (-1, -1, -1)
    if rgbequals(oldrgb, newrgb):
        like()
        oldrgb = newrgb
    else:
        print("{} 已赞过，本次循环跳过".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
    pyautogui.scroll(1000)
    if closecircle():
        print("{} 已退出朋友圈".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        return True
    else:
        print("{} error,退出程序".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        sys.exit()
        return False

# 主程序,i是计数器
i = 0
print("{} 运行前建议关掉鼠标，以免影响鼠标定位".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
while(True):
    nowtime = time.time()
    if nowtime >= plantime:
        print("{} 到达计划时间了，程序结束,GOODBYE".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        sys.exit()
    else:
        mainthread()
        i += 1