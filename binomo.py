from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, time

class apiAlfaBinomo():
    def __init__(self, email, password, timeBotWait = 30, loginError = True):
        super().__init__()
        self.user = email
        self.password = password
        self.loginPage = 'https://binomo.com/'
        self.logout = 'https://binomo.com/auth'
        self.tradingOperation = 'https://binomo.com/'
        self.loginError = loginError
        self.timeBotWait = timeBotWait
        self.navegator()
        if self.loginError:
            self.login()
        else:
            self.noLogin()

    def navegator(self):
        try:
            self.driver = webdriver.Firefox()
        except:
            try:
                self.driver = webdriver.Opera()
            except:
                try:
                    self.driver = webdriver.Chrome()
                except:
                    try:
                        self.driver = webdriver.Ie()
                    except:
                        print('Navator From Error Critical')
                        exit()

    def login(self):
        self.driver.get(self.loginPage)
        while True:
            try:
                # acceso
                OneBtnActionInitSession = self.driver.find_element_by_xpath('/html/body/app-root/app-scroll/div/div/app-header/header/div[3]/ng-component[1]/vui-button[1]/button')
                OneBtnActionInitSession.click()
                TwoBtnActionInitSession = self.driver.find_element_by_xpath('/html/body/app-sidebar/div/vui-sidebar/div/div/div/app-scroll/div/div/ng-component/vui-tabs/div/div[1]/div/vui-tab-button[2]/div/button')
                TwoBtnActionInitSession.click()
                sleep(2)
                # correo y contraseña
                emailInput = self.driver.find_element_by_xpath('/html/body/app-sidebar/div/vui-sidebar/div/div/div/app-scroll/div/div/ng-component/div/ng-component/div/div/sign-in/div/form/div[1]/app-input/vui-input/div[1]/div[2]/vui-input-text/input')
                emailInput.send_keys(self.user)
                passwordInput = self.driver.find_element_by_xpath('/html/body/app-sidebar/div/vui-sidebar/div/div/div/app-scroll/div/div/ng-component/div/ng-component/div/div/sign-in/div/form/div[2]/app-input/vui-input/div[1]/div[2]/vui-input-password/input')
                passwordInput.send_keys(self.password)
                # ingresar
                intoLogin = self.driver.find_element_by_xpath('/html/body/app-sidebar/div/vui-sidebar/div/div/div/app-scroll/div/div/ng-component/div/ng-component/div/div/sign-in/div/form/vui-button/button')
                intoLogin.click()
                sleep(self.timeBotWait)
                break
            except:
                sleep(2)

    
    def noLogin(self):
        self.driver.get(self.tradingOperation)

    def timeBuy(self, time:int, seconds = False):
        dictTime = {
            1 : '',
            2 : '',
            3 : '',
            4 : '',
            5 : '',
        }

        while True:
            try:
                inputTimeBTN = self.driver.find_element_by_xpath('/html/body/app-root/app-scroll/div/div/ng-component/main/div/app-panel/ng-component/div/binary-time-input/vui-input/div[1]/div[1]')
                inputTimeBTN.click()
                break
            except IndexError as eIndex:
                print('No Esta El Tiempo Estipulado',eIndex)
                
        if seconds:
            countTime = 1
            for i in dictTime:
                dictTime[i] = f'/html/body/app-root/app-scroll/div/div/ng-component/main/div/app-panel/ng-component/div/binary-time-input/vui-input/div[1]/vui-popover/div[2]/app-scroll/div/div/div/div/vui-option[{str(countTime)}]'
                countTime += 1
        else:
            countTime = 1
            for i in dictTime:
                dictTime[i] = f'/html/body/app-root/app-scroll/div/div/ng-component/main/div/app-panel/ng-component/div/binary-time-input/vui-input/div[1]/vui-popover/div[2]/app-scroll/div/div/div/div[1]/vui-option[{str(countTime)}]'
                countTime += 1
            print(dictTime[time])

        while True:
            try:
                inputTimeSelect = self.driver.find_element_by_xpath(dictTime[time])
                inputTimeSelect.click()
                break
            except:
                pass


    def mount(self,money:int):
        dictMount = {
            3000 : '',
            15000 : '',
            30000 : '',
            60000 : '',
            150000 : '',
            300000 : '',
            600000 : '',
            3000000 : '',
        }

        countDictMount = len(dictMount)

        while True:
            try:
                inputMountBTN = self.driver.find_element_by_xpath('/html/body/app-root/app-scroll/div/div/ng-component/main/div/app-panel/ng-component/div/vui-input/div[1]/div[1]')
                inputMountBTN.click()
                break
            except IndexError as eIndexM:
                print('No Esta El Tiempo Estipulado',eIndexM)

        count = 1
        for i in dictMount:
            dictMount[i] = f'/html/body/app-root/app-scroll/div/div/ng-component/main/div/app-panel/ng-component/div/vui-input/div[1]/vui-popover/div[2]/app-scroll/div/div/div/vui-option[{str(count)}]'
            count += 1
        
        while True:
            try:
                inputTimeSelect = self.driver.find_element_by_xpath(dictMount[money])
                inputTimeSelect.click()
                break
            except:
                pass
        
    def EntitiesAvailable(self):
        BTNACTIVES = self.driver.find_element_by_xpath('/html/body/app-root/app-scroll/div/div/app-header/header/div[2]/ng-component/div/vui-button/button')
        BTNACTIVES.click()
        ACTIVESDIS = self.driver.find_element_by_xpath('/html/body/vui-popover/div[2]/assets-block/asset-list/div/app-scroll/div/div/div')
        actives = ACTIVESDIS.text
        listActives = actives.split('\n')
        listActives.remove('Disponible para Standard')
        listActives.remove('Disponible para Gold')
        listActives.remove('Disponible para VIP')
        return listActives

    def listOder(self):
        listOrderActives = self.EntitiesAvailable()
        lenLlistOActives = len(listOrderActives)
        dictActives = {}
        for i in range(0, lenLlistOActives, 3):
            iterListIndex = listOrderActives[i]
            iterListIndex_1 = listOrderActives[i + 1]
            iterListIndex_2 = listOrderActives[i + 2]
            dictActives[iterListIndex] = []
            dictActives[iterListIndex].append(iterListIndex_1)
            dictActives[iterListIndex].append(iterListIndex_2)
        return dictActives


    def actionDV(self, active:str):
        errorIter = "error index element"
        listOderDict = self.listOder()
        countElement = 1
        for i in listOderDict:
            try:
                act = self.driver.find_element_by_xpath(f'/html/body/vui-popover/div[2]/assets-block/asset-list/div/app-scroll/div/div/div/div[{countElement}]')
                actText = act.text
                if actText == i:
                    act.click() 
                    break
                countElement += 1
            except:
                countElement = 1
                break
        return errorIter

    def buy(self, action:str):
        while True:
            try:
                if action == 'CALL':
                    inputCALL = self.driver.find_element_by_xpath('/html/body/app-root/app-scroll/div/div/ng-component/main/div/app-panel/ng-component/binary-info/div[2]/div/vui-button[1]/button')
                    inputCALL.click()
                elif action == 'PUT':
                    inputPUT = self.driver.find_element_by_xpath('/html/body/app-root/app-scroll/div/div/ng-component/main/div/app-panel/ng-component/binary-info/div[2]/div/vui-button[2]/button')
                    inputPUT.click()
                else:
                    exit()
                break
            except:
                pass