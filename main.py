import requests, json, time, datetime
from lxml import etree

def Epidemic(_username, _password, _useragent, _notify, _token):
    url = 'http://xg.kmmu.edu.cn/SPCP/Web/'
    session = requests.session()
    user_agent = _useragent
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': user_agent
    }
    resp = session.get(url=url,headers=headers)
    tree = etree.HTML(resp.text)
    reSubmiteFlag = tree.xpath('//*[@id="form1"]/input[1]/@value')[0]
    txtUid = _username
    txtPwd = _password
    # 封装post请求数据
    data = {
        'ReSubmiteFlag': reSubmiteFlag,
        'txtUid': txtUid,
        'txtPwd': txtPwd,
        'StuLoginMode': 1,
        'codeInput': ''
    }
    resp = session.post(url=url, data=data, headers=headers)
    tree = etree.HTML(resp.text)
    result = str(tree.xpath('/html/body/script/text()'))
    if result.find('用户名或者密码错误，请重新输入!') != -1:
        print(f'{get_time()} 用户名或者密码错误!')
        content = {
            "读取的账号": _username,
            "读取的密码": _password,
            }
        pushPlusNotify(_notify, _token, '登陆失败！', json.dumps(content), 'json')
    else:
        # 进入签到页面的URL
        indexUrl = 'http://xg.kmmu.edu.cn/SPCP/Web/Report/Index'
        resp = session.get(url=indexUrl, headers=headers)
        tree = etree.HTML(resp.text)
        result = str(tree.xpath('/html/body/script/text()'))
        if result.find('当前采集日期已登记！') != -1:
            print(f'{get_time()} 当前采集日期已登记！')
        elif result.find('只能1点至18点可以填报！') != -1:
            print(f'{get_time()} 只能1点至18点可以填报！')
        else:
            # 封装post数据包
            post_data = {
                'StudentId': tree.xpath('//*[@id="StudentId"]/@value')[0],
                'Name': tree.xpath('//*[@id="Name"]/@value')[0],
                'Sex': tree.xpath('//*[@id="Sex"]/@value')[0],
                'SpeType': tree.xpath('//*[@id="SpeType"]/@value')[0],
                'CollegeNo': tree.xpath('//*[@id="CollegeNo"]/@value')[0],
                'SpeGrade': tree.xpath('//*[@id="SpeGrade"]/@value')[0],
                'SpecialtyName': tree.xpath('//*[@id="SpecialtyName"]/@value')[0],
                'ClassName': tree.xpath('//*[@id="ClassName"]/@value')[0],
                'MoveTel': tree.xpath('//*[@id="MoveTel"]/@value')[0],
                'Province': str(tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/select[2]/@data-defaultvalue'))[2:4] + '0000',
                'City': tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/select[2]/@data-defaultvalue')[0],
                'County': tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/select[3]/@data-defaultvalue')[0],
                'ComeWhere': tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/input/@value')[0],
                'FaProvince': str(tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/select[2]/@data-defaultvalue'))[2:4] + '0000',
                'FaCity': tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/select[2]/@data-defaultvalue')[0],
                'FaCounty': tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/select[3]/@data-defaultvalue')[0],
                'FaComeWhere': tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/input/@value')[0],
                'radio_1': '71a16876-3d52-4510-8c96-09b232a0161b',
                'radio_2': '083d90f5-5fa2-4a6d-a231-fe315b5104a3',
                'radio_3': '994c60eb-6f68-48bd-8bda-49a8a7ea812c',
                'text_1': '',
                'radio_4': '18e9be47-deee-4eb0-8318-935f7ec832fd',
                'radio_5': '8dce119f-8eba-45b7-ac3c-ecb49e480dd3',
                'radio_6': 'fe8b77d7-0014-49e1-bea0-46b0bff13898',
                'Other': '',
                'GetAreaUrl': '/SPCP/Web/Report/GetArea',
                'IdCard': tree.xpath('//*[@id="IdCard"]/@value')[0],
                'ProvinceName': tree.xpath('//*[@id="ProvinceName"]/@value')[0],
                'CityName': tree.xpath('//*[@id="CityName"]/@value')[0],
                'CountyName': tree.xpath('//*[@id="CountyName"]/@value')[0],
                'FaProvinceName': tree.xpath('//*[@id="FaProvinceName"]/@value')[0],
                'FaCityName': tree.xpath('//*[@id="FaCityName"]/@value')[0],
                'FaCountyName': tree.xpath('//*[@id="FaCountyName"]/@value')[0],
                'radioCount': '6',
                'checkboxCount': '0',
                'blackCount': '1',
                'PZData': '[{"OptionName":"以上症状都没有","SelectId":"71a16876-3d52-4510-8c96-09b232a0161b","TitleId":"eb0c8db7-b4dd-4ad6-b58a-626fc3336f16","OptionType":"0"},{"OptionName":"否，身体健康","SelectId":"083d90f5-5fa2-4a6d-a231-fe315b5104a3","TitleId":"a9a30b10-f88e-4776-ac74-b5a10fa11886","OptionType":"0"},{"OptionName":"否，不是疑似感染者","SelectId":"994c60eb-6f68-48bd-8bda-49a8a7ea812c","TitleId":"37e33b7d-5575-48c3-b59b-d4b7f6a6a0b5","OptionType":"0"},{"OptionName":"否","SelectId":"18e9be47-deee-4eb0-8318-935f7ec832fd","TitleId":"986a95ff-5ce4-4417-9810-b1e190594f34","OptionType":"0"},{"OptionName":"否","SelectId":"8dce119f-8eba-45b7-ac3c-ecb49e480dd3","TitleId":"3a3a10c8-02a7-4f16-95e5-f8ef5c8bfd75","OptionType":"0"},{"OptionName":"健康","SelectId":"fe8b77d7-0014-49e1-bea0-46b0bff13898","TitleId":"6002f891-d80d-4e01-ad6d-651e01df394b","OptionType":"0"}]',
                'ReSubmiteFlag': tree.xpath('//*[@id="SaveBtnDiv"]/input[13]/@value')[0]
            }
            # 发起post请求
            resp = session.post(url=indexUrl, data=post_data, headers=headers)
            if datetime.datetime.now().hour  >= 12:
                # 封装pushplus的post数据包
                post_data = {
                    "自检步骤": "访问下面的网址，登录并签到，以检查是否签到成功",
                    "登录网址": url,
                    "学号及账号": tree.xpath('//*[@id="StudentId"]/@value')[0],
                    "密码": _password,
                    "姓名": tree.xpath('//*[@id="Name"]/@value')[0],
                    "性别": tree.xpath('//*[@id="Sex"]/@value')[0],
                    "班级": tree.xpath('//*[@id="ClassName"]/@value')[0],
                    "手机号": tree.xpath('//*[@id="MoveTel"]/@value')[0],
                    "当前所在地": tree.xpath('//*[@id="ProvinceName"]/@value')[0] + tree.xpath('//*[@id="CityName"]/@value')[0] + tree.xpath('//*[@id="CountyName"]/@value')[0] + tree.xpath('//*[@id="form1"]/div[1]/div[4]/div[2]/input/@value')[0],
                    "家庭住址": tree.xpath('//*[@id="FaProvinceName"]/@value')[0] + tree.xpath('//*[@id="FaCityName"]/@value')[0] + tree.xpath('//*[@id="FaCountyName"]/@value')[0] + tree.xpath('//*[@id="form1"]/div[1]/div[5]/div[2]/input/@value')[0],
                }
                pushPlusNotify(_notify, _token, '今早签到可能失败，请自查！（附签到表单内容）', json.dumps(post_data), 'json')
            print(f'{get_time()} 签到成功~')

def pushPlusNotify(notify, token, title, content, template):
    if notify: 
        url = 'http://www.pushplus.plus/send' 
        # 封装pushplus的post数据包
        data = {
            # 在 http://www.pushplus.plus/push1.html 申请token
            'token': token, 
            'title': title,
            'content': content,
            'template': template
            }
        # 发起post请求
        requests.post(url=url,data=data)

def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

with open('./user.json', 'r', encoding='utf-8') as user_file: 
    user_data = json.load(user_file)

with open('./config/user-agent.json', 'r', encoding='utf-8') as UA_file:
    UA_data = json.load(UA_file)

i = 0
for i in range(len(user_data)):
    m = i % len(UA_data)
    Epidemic(user_data[i]['_username'], user_data[i]['_password'], UA_data[m], user_data[i]['_notify'], user_data[i]['_token'])
