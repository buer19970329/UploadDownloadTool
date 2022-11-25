def main_p1(path, account_file, subj_info=None):
    import asyncio
    from pyppeteer import launch
    from pyppeteer_stealth import stealth
    import os
    import random
    import pandas as pd
    import shutil

    if  os.path.exists(os.path.split(path)[:-1][0] + '/temp_cookies'):
        shutil.rmtree(os.path.split(path)[:-1][0] + '/temp_cookies', ignore_errors=True)

    # 以防T1文件夹混进奇怪的文件，所以检索一下
    t1_path = os.listdir(path)
    t1_path.sort()
    t1_list = []
    for file in t1_path:
        if file.endswith("nii.gz"):
            if not file.startswith("."):
                t1_list.append(file)
    i=0
    while i<len(t1_list):
        t1_list[i]=path+'/'+t1_list[i]
        i+=1

    # 读取sex & age
    if subj_info:
        sex_list = pd.read_csv(f'{subj_info}')['sex'].to_list()
        age_list = pd.read_csv(f'{subj_info}')['age'].to_list()

    # 读取账号信息
    account_list = pd.read_csv(f'{account_file}',header=None)[0].to_list()
    password_list = pd.read_csv(f'{account_file}',header=None)[1].to_list()

    # 随机时间，防止被检测
    def time_random():
        return random.randint(20,30)

    alldatadir = os.path.split(path)[:-1][0]
    async def main():
        path = os.getcwd()
        # 设置浏览器属性
        browser = await launch({
            # 'executablePath': '/Users/linxiaomin/Desktop/LINIP/Python/volbrain/auto_upload/Chromium.app',
            'headless': False,
            'dumpio': True,
            'userDataDir': alldatadir+"/temp_cookies",
            'args': ['--disable-infobars', '--no-sandbox', '--window-size=1366,850', ]
        })
        page = await browser.newPage()
        await page.setViewport({'width': 1366, 'height': 768})
        # 防止网站识别出脚本
        await stealth(page)
        page.setDefaultNavigationTimeout(80000)

        # 上传次数
        num=0

        # 每个账号上传次数
        account_num=10

        # 账号密码index
        index=0

        for t1_path in t1_list:

            if account_num==0:
                index+=1
                account_num=10
                if len(account_list)==index:
                    break

            if account_num==10:
                await page.goto("https://volbrain.upv.es/logout.php")
                await page.waitFor(3000)

                # 输入账号
                await page.type('#email',account_list[index],{'delay': time_random()})
                # 输入密码
                await page.type('#password',str(password_list[index]),{'delay': time_random()})
                await page.waitFor(1000)
                # 点击登录
                await page.evaluate('checkLogin();')
                await page.waitForNavigation()
                print("\033[0;37;41m\t %s\033[0m" % (account_list[index]))

            # 以防出错，多点几次.....
            await page.click('#pipeline1')
            await page.click('#pipeline1')
            await page.click('#pipeline1')

            # 上传结构像
            uploadPic = await page.waitForSelector('#volbrain_t1_file');
            await uploadPic.uploadFile(t1_list[num])
            await page.waitFor(3000)

            if subj_info:
                await page.select('#volbrain_patientssex',sex_list[num])
                await page.type('#volbrain_patientsage',str(age_list[num]))

            await page.evaluate("uploadData('volbrain');")
            await page.waitForNavigation()

            # Loop 10次！
            num+=1
            account_num-=1


        await browser.close()

    asyncio.get_event_loop().run_until_complete(main())

def main_p6(path, account_file, subj_info=None):
    import asyncio
    from pyppeteer import launch
    from pyppeteer_stealth import stealth
    import os
    import random
    import pandas as pd
    import shutil
    if  os.path.exists(os.path.split(path)[:-1][0] + '/temp_cookies'):
        shutil.rmtree(os.path.split(path)[:-1][0] + '/temp_cookies', ignore_errors=True)

    # 以防T1文件夹混进奇怪的文件，所以检索一下
    t1_path = os.listdir(path)
    t1_path.sort()
    t1_list = []
    for file in t1_path:
        if file.endswith("nii.gz"):
            if not file.startswith("."):
                t1_list.append(file)
    i=0
    while i<len(t1_list):
        t1_list[i]=path+'/'+t1_list[i]
        i+=1

    # 读取sex & age
    if subj_info:
        sex_list = pd.read_csv(f'{subj_info}')['sex'].to_list()
        age_list = pd.read_csv(f'{subj_info}')['age'].to_list()

    # 读取账号信息
    account_list = pd.read_csv(f'{account_file}',header=None)[0].to_list()
    password_list = pd.read_csv(f'{account_file}',header=None)[1].to_list()

    # 随机时间，防止被检测
    def time_random():
        return random.randint(20,30)

    alldatadir = os.path.split(path)[:-1][0]
    async def main():
        path = os.getcwd()
        # 设置浏览器属性
        browser = await launch({
            # 'executablePath': '/Users/linxiaomin/Desktop/LINIP/Python/volbrain/auto_upload/Chromium.app',
            'headless': False,
            'dumpio': True,
            'userDataDir': alldatadir+"/temp_cookies",
            'args': ['--disable-infobars', '--no-sandbox', '--window-size=1366,850', ]
        })
        page = await browser.newPage()
        await page.setViewport({'width': 1366, 'height': 768})
        # 防止网站识别出脚本
        await stealth(page)
        page.setDefaultNavigationTimeout(80000)

        # 上传次数
        num=0

        # 每个账号上传次数
        account_num=10

        # 账号密码index
        index=0

        for t1_path in t1_list:

            if account_num==0:
                index+=1
                account_num=10
                if len(account_list)==index:
                    break

            if account_num==10:
                await page.goto("https://volbrain.upv.es/logout.php")
                await page.waitFor(3000)

                # 输入账号
                await page.type('#email',account_list[index],{'delay': time_random()})
                # 输入密码
                await page.type('#password',str(password_list[index]),{'delay': time_random()})
                await page.waitFor(1000)
                # 点击登录
                await page.evaluate('checkLogin();')
                await page.waitForNavigation()
                print("\033[0;37;41m\t %s\033[0m" % (account_list[index]))

            # 以防出错，多点几次.....
            await page.click('#pipeline6')
            await page.click('#pipeline6')
            await page.click('#pipeline6')

            # 上传结构像
            uploadPic = await page.waitForSelector('#vol2brain_t1_file');
            await uploadPic.uploadFile(t1_list[num])
            await page.waitFor(3000)

            if subj_info:
                await page.select('#vol2brain_patientssex',sex_list[num])
                await page.type('#vol2brain_patientsage',str(age_list[num]))

            await page.evaluate("uploadData('vol2brain');")
            await page.waitForNavigation()

            # Loop 10次！
            num+=1
            account_num-=1


        await browser.close()

    asyncio.get_event_loop().run_until_complete(main())

def download(path,account_file, t1_type):
    import asyncio
    from pyppeteer import launch
    from pyppeteer_stealth import stealth
    import os
    import random
    import pandas as pd
    import shutil
    if  os.path.exists(os.path.split(path)[:-1][0] + '/temp_cookies'):
        shutil.rmtree(os.path.split(path)[:-1][0] + '/temp_cookies', ignore_errors=True)

    # # 以防T1文件夹混进奇怪的文件，所以检索一下
    if not os.path.exists(path + '/output'):
        os.makedirs(path + '/output')
    outputdir = path + '/output'

    t1_path = os.listdir(path)
    t1_path.sort()
    t1_list = []
    for file in t1_path:
        if file.endswith("nii.gz"):
            if not file.startswith("."):
                t1_list.append(file)
    i=0
    while i<len(t1_list):
        t1_list[i]=path+'/'+t1_list[i]
        i+=1

    # # 读取sex & age
    # sex_list = pd.read_csv(os.path.split(path)[:-1][0]+ '/subj_info.csv')['sex'].to_list()
    # age_list = pd.read_csv(os.path.split(path)[:-1][0]+ '/subj_info.csv')['age'].to_list()

    # 读取账号信息
    account_list = pd.read_csv(f'{account_file}',header=None)[0].to_list()
    password_list = pd.read_csv(f'{account_file}',header=None)[1].to_list()

    # 随机时间，防止被检测
    def time_random():
        return random.randint(20,30)

    alldatadir = os.path.split(path)[:-1][0]
    async def main():
        path = os.getcwd()
        # 设置浏览器属性
        browser = await launch({
            # 'executablePath': '/Users/linxiaomin/Desktop/LINIP/Python/volbrain/auto_upload/Chromium.app',
            'headless': False,
            'dumpio': True,
            'userDataDir': alldatadir+"/temp_cookies",
            'args': ['--disable-infobars', '--no-sandbox', '--window-size=1366,850', ]
        })
        page = await browser.newPage()
        await page.setViewport({'width': 1366, 'height': 768})
        # 防止网站识别出脚本
        await stealth(page)
        page.setDefaultNavigationTimeout(60000)


        # 每个账号下载次数
        account_num=1

        # 账号密码index
        index=0

        for i in account_list:
            if account_num==0:
                index+=1
                account_num=1

            if account_num==1:
                await page.goto("https://volbrain.upv.es/logout.php")
                await page.waitFor(3000)

                # 输入账号
                await page.type('#email',account_list[index],{'delay': time_random()})
                # 输入密码
                await page.type('#password',str(password_list[index]),{'delay': time_random()})
                await page.waitFor(1000)
                # 点击登录
                await page.evaluate('checkLogin();')
                await page.waitForNavigation()
                print("\033[0;37;41m\t %s\033[0m" % (account_list[index]))

            # download setting
            if account_num==1:
                await page._client.send("Page.setDownloadBehavior", {
                    "behavior": "allow", # 允许所有下载请求
                    "downloadPath": outputdir  # 设置下载路径
                })

                if t1_type =='native':
                    NodeList = await page.querySelectorAll('[href*="native"]')
                    for num,href in enumerate(NodeList):
                        if num < 10:
                            await href.click()
                        else:
                            break
                    await page.waitFor(10000)

                elif t1_type =='MNI':
                    NodeList = await page.querySelectorAll('[href*="upv.es"]')
                    for num,href in enumerate(NodeList):
                        if num in range(0,30,3):
                            await href.click()
                        else:
                            await page.waitFor(500)
                    await page.waitFor(10000)

                elif t1_type =='all':
                    NodeList = await page.querySelectorAll('[href*="upv.es"]')
                    for num,href in enumerate(NodeList):
                        if num in range(0,30,3):
                            await href.click()
                        else:
                            await page.waitFor(500)
                    await page.waitFor(10000)
                    NodeList = await page.querySelectorAll('[href*="native"]')
                    for num,href in enumerate(NodeList):
                        if num < 10:
                            await href.click()
                        else:
                            break
                    await page.waitFor(10000)

                # await page.click('a[href*="logout.php"]')
                # await page.waitForNavigation()
                # Loop 10次！
                account_num-=1

        await browser.close()

    asyncio.get_event_loop().run_until_complete(main())
