import os, pyautogui
import time

os.chdir('C:\\Users\\Vagabond\\Desktop\\FOnlineMiningScript')

times = 1
mineral_ore_PNG = ('minerals61day.PNG' or 'minerals61night.PNG' or 'minerals61evening.PNG' or 'mintest.PNG')
iron_ore_PNG = ('iron61.PNG' or 'iron61night.PNG')
brahmin_PNG = ('brahmin61day.PNG' or 'brahmin61night.PNG' or 'brahmin61evening.PNG')
overweight_PNG = ('overweight.PNG')
offer = ('offerButton.PNG')

def lookForIron():        # Если на экране не распознаёт железо, то идёт вправо и влево, по ходу пути ищёт руду.
    print('Не могу найти железо, иду вправо затем влево.')
    pyautogui.click(button='right')
    pyautogui.moveTo(1000, 300, duration=1)
    pyautogui.click()
    pyautogui.click(button='right')
    time.sleep(.5)
    ironLocation = pyautogui.locateCenterOnScreen(iron_ore_PNG, confidence=.8, grayscale=True)
    if ironLocation != None:
        print('Кажется, вижу железную руду.')
    else:
        time.sleep(2)
        ironLocation = pyautogui.locateCenterOnScreen(iron_ore_PNG, confidence=.8, grayscale=True)
        pyautogui.click(button='right')
        pyautogui.moveTo(600, 250, duration=1)
        pyautogui.click()
        pyautogui.click(button='right')
        time.sleep(.5)
        ironLocation = pyautogui.locateCenterOnScreen(iron_ore_PNG, confidence=.8, grayscale=True)
        if ironLocation != None:
            print('Кажется, вижу железную руду.')
        else:
            time.sleep(2)
            ironLocation = pyautogui.locateCenterOnScreen(iron_ore_PNG, confidence=.6, grayscale=True)
            print('Не вижу железную руду, ищу минералы.')

def tradebrahmin(t):    #Функция передачи руды брамину
    brahmin = pyautogui.locateCenterOnScreen(brahmin_PNG, confidence=.7)
    if brahmin == None:     #если брамина на экране нет - идёт искать его в левый нижний угол экрана
        print('Не вижу брамина. Иду искать.')
        pyautogui.click(button='right')
        pyautogui.moveTo(528, 322, duration=1)
        pyautogui.click()
        pyautogui.click(button='right')
        time.sleep(1)
        brahmin = pyautogui.locateCenterOnScreen(brahmin_PNG, confidence=.7)
        if brahmin != None:
            print('Кажется, вижу брамина.')
        else:
            time.sleep(4)
        brahmin = pyautogui.locateCenterOnScreen(brahmin_PNG, confidence=.7)
        #brahminExpectation = pyautogui.locateCenterOnScreen('findbrahmin.PNG')
        #print(brahminExpectation)
        #pyautogui.moveTo(brahminExpectation, duration=1)
        #pyautogui.click()
        #pyautogui.click(button='right')
    print('Идём к брамину.', t, 'секунд.')
    pyautogui.click(brahmin)
    while t:
        t -= 1
        time.sleep(0.5)
        tradeButton = pyautogui.locateCenterOnScreen('trade.PNG', confidence=.7)
        while tradeButton == None:
            time.sleep(1)
            tradeButton = pyautogui.locateCenterOnScreen('trade.PNG', confidence=.7)
        pyautogui.click(tradeButton)
        time.sleep(0.5)  # далее непосредственно процедура торговли.
        if pyautogui.locateCenterOnScreen('ironinv.PNG', confidence=.8, region=(0, 0, 700, 800)):
            print('Нашёл железо.')
            ironinv = pyautogui.locateCenterOnScreen('ironinv.PNG', confidence=.8, region=(0, 0, 700, 800))
            table = pyautogui.locateCenterOnScreen('table.png')
            pyautogui.moveTo(ironinv)
            print('Тащу железо.')
            pyautogui.dragTo(600, 440, 0.5, button='left')
            offerAll = pyautogui.locateCenterOnScreen('offerAll.PNG', confidence=.7)
            pyautogui.click(offerAll)
            pyautogui.press('enter')
        time.sleep(0.3)
        if pyautogui.locateCenterOnScreen('mineralsinv.PNG', confidence=.8, region=(0, 0, 700, 800)):
            print('Нашёл минералы.')
            mineralinv = pyautogui.locateCenterOnScreen('mineralsinv.PNG', confidence=.8, region=(0, 0, 700, 800))
            ##########table = pyautogui.locateCenterOnScreen('table.png')
            pyautogui.moveTo(mineralinv)
            print('Тащу минералы.')
            pyautogui.dragTo(600, 440, 0.5, button='left')
            offerAll = pyautogui.locateCenterOnScreen('offerAll.PNG', confidence=.8)
            pyautogui.click(offerAll)
            pyautogui.press('enter')
        offerTrade = pyautogui.locateCenterOnScreen('offerButton.PNG', confidence=.6, grayscale=True)
        print(offerTrade)
        pyautogui.click(offerTrade)
        pyautogui.press('esc', presses=2)
        MineEverything(times)
    if t == 0:
        print('Не дошли до брамина.')

def timerun(t1):    # Таймер для корелляции времени перебежки от одной жилы к другой
    while t1:       # А также непосредственно клики
        t1 -= 1
        #print(t1, 'секунд до запуска')
        time.sleep(1)
        if t1 == 0:
            if pyautogui.locateCenterOnScreen('char61day.PNG' or 'incorrectchar.PNG', confidence=0.6):
                pyautogui.move(0, 1)
                pyautogui.click(clicks=10, interval=1.6)
            else:
                pyautogui.move(-8, -8)
                pyautogui.click(clicks=10, interval=1.6)

def timer(t):      #Таймер для запуска программы кликера.
    print('Запускаем таймер. Время -', t, 'секунд.')
    while t:
        t -= 1
        print(t, 'секунд до запуска')
        time.sleep(1)
        if t == 0:
            mineIron(3)

def mineMineral(times):     #Поиск минералов на экране и первоначальный клик по ним
    mineralLocation = pyautogui.locateCenterOnScreen(mineral_ore_PNG, confidence=.6, grayscale=True)
    if mineralLocation == None:
        print('Не могу найти минералы, копаю железо.')
        mineIron(5)
        #tradebrahmin(30) #debug function, comment out
    else:
        pyautogui.click(mineralLocation)
        timerun(10)

def mineIron(times):   #Поиск железной руды на экране и первоначальный клик по ней
    ironLocation = pyautogui.locateCenterOnScreen(iron_ore_PNG, confidence=.6, grayscale=True)
    if ironLocation == None:
        lookForIron()
        mineMineral(2)
    else:
        pyautogui.click(ironLocation)
        timerun(10)

def MineEverything(times):
    for times in range(1, times):
        time.sleep(3)
        if pyautogui.locateCenterOnScreen(overweight_PNG, confidence=.85):
            print('Персонаж перегружен. Через 3 секунды производим выгрузку вещей в брамина.')
            tradebrahmin(30)
        else:
            times += 1
            print('Произвели копание/поиск уже', times, 'раз. Делаем ещё', times - 1, 'подхода.')
            timer(3)

MineEverything(100)