# 🚀白菜GPT🚀高速超稳中转API帮助文档(免手机注册版)
## 国内直连 无需代理 价格和官方一致，单笔消费满300元7折优惠，点击购买！

> 支持GPT3.5 、GPT4.0 、GTP4o 、DALLE.3 、text-embedding 等多种模型


# 🎁 购买链接

拍下24小时自动秒发APIKEY

电脑或手机浏览器点击[淘宝](http://e.tb.cn/h.gH4gxUT6fd8mDry?tk=IvOP38MGMgQ)：

【淘宝】http://e.tb.cn/h.gH4gxUT6fd8mDry?tk=IvOP38MGMgQ CZ0016 「企业级中转APIKEY4.0高速稳定一秒响应官方倍率」
点击链接直接打开 或者 淘宝搜索直接打开

💡也可以手机淘宝扫码下方二维码

![image](https://github.com/user-attachments/assets/1482d718-6677-40ca-bdcf-6f5fdf3c39fb)

🔥Tip

> 📣强烈建议您Ctrl+D收藏我们，下次打开更方便。
> 
> 📣请仔细阅读说明，并遵循指引操作，非常感谢您的配合。

# 🚀快速开始

## 🔥一、获取APIKEY

1、淘宝24小时自动秒发货，拍完，聊天窗口自动推送APIKE复制秘钥即可



2、除了APIKEY，中转API需要对应的转发URL，不同客户端配置稍有不同， 请逐个尝试下方地址：

**> https://api.baicaigpt.cn
> 
> https://api.baicaigpt.cn/v1
> 
> https://api.baicaigpt.cn/v1/chat/completions**

## 🔥二、使用APIKEY

### 🔥2.1 ChatGPT免费镜像开箱即用

1、LobeChat （35K+ star!即刻拥有你的私人 ChatGPT的项目）

> PC端/移动端，请访问 [https://lobechat.baicaigpt.com](https://lobechat.baicaigpt.com)

![image](https://github.com/user-attachments/assets/a96d97f1-ccf6-4494-b976-91963702fc98)

![image](https://github.com/user-attachments/assets/ac41a079-a828-4a2f-872e-4167310fb590)

![image](https://github.com/user-attachments/assets/9bbe4c2f-8963-405b-8780-35187a0a14f1)


2、NextChat（70K+ star！马上拥有跨平台 ChatGPT 应用：ChatGPT-Next-Web）

> PC端/移动端，请访问 [https://nextchat.baicaigpt.cn](https://nextchat.baicaigpt.cn)

**注意：仅需复制粘贴白菜API KEY即可，其他无需修改，详见下图
注意：仅需复制粘贴白菜API KEY即可，其他无需修改，详见下图
注意：仅需复制粘贴白菜API KEY即可，其他无需修改，详见下图**

可随时访问 https://baicaigpt.com 查询余额及消费明细

### 🔥2.2 其他三方客户端如何配置APIKEY

沉浸式翻译APIKEY配置

1、打开Chrome插件，点击设置

2、复制从淘宝购买的APIKEY，并选择所需模型（模型可默认，或从模型清单选择，推荐gpt-4o-mini）

3、点击“展开更多自定义选型按钮”

4、复制转发地址，切记不要输错，复制粘贴如下地址即可

https://api.baicaigpt.cn/v1/chat/completions

5、点击“测试服务”按钮，检查是否验证成功

6、完成配置，刷新网页可开始网页翻译！

### 🔥2.3 程序开发如何实现对话请求-Python示例代码

python代码Demo（复制粘贴，替换APIKEY即可调试通过）:

创建聊天

```
import http.client
import json

conn = http.client.HTTPSConnection("api.baicaigpt.cn")
payload = json.dumps({
   "model": "gpt-3.5-turbo",
   "messages": [
      {
         "role": "system",
         "content": "You are a helpful assistant."
      },
      {
         "role": "user",
         "content": "Hello!"
      }
   ]
})
headers = {
   'Authorization': 'Bearer sk-eyJhbGciO..........',
   'Content-Type': 'application/json'
}
conn.request("POST", "/v1/chat/completions", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```


## 🔥三、查询APIKEY可用余额

APIKEY余额及消费明细查询网址：[https://m.baicaigpt.com](https://m.baicaigpt.com) （拼音助记：白菜GPT）

使用说明：打开网址，输入APIKEY，即可查询可用余额及消费明细


## 🔥六、都支持哪些模型及价格

白菜GPT力争成为市面上性价比最高，最稳定的企业级中转API，以让AI普惠大众为使命。白菜GPT的定价策略简单明了，按照OpenAI官方倍率计费，官方价格美元×7.5固定汇率即为人民币价格，人民币汇率暂时按7.5计算。详情请点击下方链接。

点击查看 白菜GPT模型清单&定价

## 🔥七、其他常见问题

1.如何进行API接口调用？
请参考第五章节，示例代码。

2.支持哪些模型及价格多少？
点击查看模型清单：模型清单。

5.服务稳定性如何？
非常稳定，可用性监测请点击这里。

6.购买完是否需要兑换APIKEY？
无需兑换，淘宝自动发货即为APIKEY，配合中转URL直接用即可。

7.请问这个APIKEY能用多久？
有效期半年以上，具体参见APIKEY余额查询。

8.支持4o吗和流式请求么？
支持。

9.兑换密钥后需要充值吗？
无需充值，购买的APKEY即为预付金额，随时可查余额，用完可随时再买。

10.可以调用API吗？
可以，程序员绝对友好，上面有示例代码。

11.这是一个API吗？
是的，仅提供APIKEY，需自行选择镜像，白菜免费提供，详见第三章节。

12.有时间限制吗？
无时间限制，长期有效，用完为止。

13.网页无法打开？
请切换网络或，加客服微信BaiCai2568，在线咨询。
