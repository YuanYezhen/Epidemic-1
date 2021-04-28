# 正式开始部署

## 正式开始

1. [点击此处](https://github.com/chiupam/Epidemic)打开我的 Github Epidemic 项目

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/Epidemic.png)

2. 点击 `Fork` 按钮

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_1.png)

3. 先点击 `Settings`, 再点击 `Secret`, 最后点击 `New repository secret`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_2.png)

4. 先在 Name 中输入 PAT, 再在 Value 中输入 PAT 的值（申请方法点击[这里](https://gitee.com/chiupam/Epidemic/blob/master/Tutorial/PAT.md)）, 最后点击 `Add secret`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_3.png)

5. 先点击 `Settings`, 再点击 `Secret`, 最后点击 `New repository secret`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_4.png)

6. 先在 Name 中输入 USER, 再在 Value 中输入下方代码块中的模板（自行修改）, 更多模板请点击[这里](https://gitee.com/chiupam/Epidemic/blob/master/config/json.md)进行查阅学习, 如需申请 `_token`最请点击[这里](http://www.pushplus.plus/push1.html)进行申请, 最后点击 `Add secret`

```json
[
    {
        "_username": "修改为你的学号",
        "_password": "修改为你的身份证后6位",
        "_notify": false,
        "_token": "_notify为 ture 时才需要填"
    }
]
```

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_5.png)

7. 先点击 `Actions`, 再点击 `I understand my workflow, go ahead and enable them`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_7.png)

8. 先点击 `Auto Sync`, 再点击 `Enable workflow`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_8.png)

9. 先点击 `Epidemic Task`, 再点击 `Enable workflow`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_9.png)

10. 先点击 `Sync To Gitee`, 再点击如图所示按钮, 最后点击 `Disable workflow`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_10.png)

11. 先点击 `Epidemic Task`, 再点击 `Run workflow`, 最后点击 `Run workflow`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_11.png)

12. 点击 `Epidemic Task`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_12.png)

13. 点击 `deploy`

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_13.png)

14. 先点击 `deploy`, 再点击 `Bulid and publish`, 可见运行结果

![image](https://gitee.com/chiupam/Epidemic/raw/master/Tutorial/png/main_14.png)
