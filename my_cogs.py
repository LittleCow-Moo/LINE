from linelib import Client, Long
import random
import time

cmd = Client.Commands.cmd
hahalist = [
    '冰塊最想做什麼事? 退伍 因為他當冰很久了', '有一天,我去吉野家,可是 吉野不在家',
    '我走進眼科診所跟醫生抱怨說:「最近視力變差了,我需要配一副新眼鏡。」他 嘆了一口氣回說:「你真的病得不輕，我這裡可是甜甜圈店啊!」',
    '有一隻狼寶寶不吃肉只吃素,狼媽媽、狼爸爸看得很擔心,某天,狼寶寶終於追著一隻兔子跑,牠們感到很欣慰,狼寶寶抓到兔子後說: 快把紅蘿蔔交出來!',
    '天上的星星有多重? 8克,因為星巴克',
    '有一天,小明去醫院量血壓,血壓計的語音說:血壓升高中，請注意...小明問醫生:為什麼會這樣?醫生回:這表示你的血壓... 國中畢業了。',
    '第一個進船的要說什麼? 要說online,因為仙境傳說online',
    '小魚問大魚說:你-喜-歡-吃-怎-樣-的-魚?大魚回:我喜歡吃講話慢的魚!小魚說: 醬紫先走',
    '小明每次開可樂,瓶蓋都寫銘謝惠顧,有一天,他在考試,突然忘記銘要怎麼寫了,於是他打開桌上的可樂, 結果寫:再來一瓶',
    '有一天,我和牛弟弟在吃草,弟弟問我:草是什麼味道?我回:草莓味。弟弟吃了一口草,生氣的說:這草明明沒有味道!我回:我沒有說錯啊... 我剛剛說草沒有味道,草沒味啊!',
    '你知道學校的警衛每天早上都在笑什麼嗎? 校門口', '什麼情況下人會有四隻眼睛? 兩個人的時候',
    '愚公臨死前召集兒子來到床邊虛弱的說:移山…移山……\n兒子:  亮晶晶? \n愚公卒。'
]
balllist = [["哞!我接到球了!",{
  "type": "flex",
  "altText": "我接到球的樣子",
  "contents": 
    {"type": "carousel","contents": 
     [
       {
         "type": "bubble",
         "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://cowlinecdn.kiwichang.repl.co/ball/cow_catch.png",
            "aspectMode": "cover",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}}],["唉呦!好痛!",{
  "type": "flex",
  "altText": "我很痛的樣子",
  "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://cowlinecdn.kiwichang.repl.co/ball/cow_ko.png",
            "aspectMode": "cover",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}}],["哞!我接到球了!","我把球丟給你\n你沒接到,你看起來很痛的樣子",{
  "type": "flex",
  "altText": "你看起來很痛的樣子",
  "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://cowlinecdn.kiwichang.repl.co/ball/didi_ko.png",
            "aspectMode": "cover",
            "size": "full"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}}]]
grasslist = ["謝謝!","哞!我吃飽了!"]


class Main(Client.Commands, prefix="/cow "):
    @cmd(name="help")
    def help(ctx):
        ctx.reply({
            "type": "flex",
            "altText": "指令清單",
            "contents": {
                "type": "bubble",
                "header": {
                    "type":
                    "box",
                    "layout":
                    "vertical",
                    "contents": [{
                        "type":
                        "image",
                        "url":
                        "https://cdn.discordapp.com/attachments/858984158620286998/1046048715686817842/ec51f3aed0943f79239a05124e863dd5.webp"
                    }, {
                        "type": "text",
                        "text": "哞!我是牛牛,一隻很簡單的機器牛。"
                    }, {
                        "type": "text",
                        "text": "目前有下列功能:"
                    }, {
                        "type": "separator",
                        "margin": "5px",
                        "color": "#FFFFFF"
                    }, {
                        "type": "text",
                        "text": "/cow haha: 為你說一句笑話!",
                        "action": {
                            "type": "message",
                            "label": "/cow haha",
                            "text": "/cow haha"
                        }
                    }, {
                        "type": "text",
                        "text": "/cow say: 讓我一字不差的學你說話!",
                        "action": {
                            "type": "message",
                            "label": "/cow say",
                            "text": "/cow say 測試"
                        }
                    }, {
                        "type": "text",
                        "text": "/cow delay: 測測看我的延遲!",
                        "action": {
                            "type": "message",
                            "label": "/cow delay",
                            "text": "/cow delay"
                        }
                    }]
                }
            }
        })

    @cmd(name="haha")
    def haha(ctx):
        ctx.reply(random.choice(hahalist))

    @cmd(name="say")
    def say(ctx, toSay: Long << str):
        ctx.reply(toSay)

    @say.error()
    def on_error(ctx, error):
      ctx.reply("哞! 正確用法是: /cow say 文字")

    @cmd(name="delay")
    def delay(ctx):
        ctx.reply(
            f"哞!機器人延遲是:{time.time()*1000-ctx.time}ms | API延遲是:{ctx.client.ping}ms"
        )

    #@cmd(name="botinfo")
    #def botinfo(ctx):
    #    f = open("readytime.txt", "r")
    #    ctx.reply(f"牛牛Line v0.0.1\n於{f.read()}上線")
    #    f.close()


class EasterEgg(Client.Commands, prefix=""):
    @cmd(name="🍀")
    def grass(ctx):
        ctx.reply(random.choice(grasslist))

    @cmd(name="🏀")
    def ball(ctx):
      ctx.reply(random.choice(balllist))

    @cmd(name="never")
    def rickroll(ctx):
        ctx.reply("gonna give you up")
      
    @cmd(name="🍰")
    def cake(ctx):
        ctx.reply("真好吃")
