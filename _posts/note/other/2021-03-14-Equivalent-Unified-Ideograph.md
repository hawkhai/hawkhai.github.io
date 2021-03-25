---
layout: post
title: "编程 -- 康熙部首替换字典"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

Unicode 中文字符集中存在两个极为相似的汉字但编码不同的情况，主要是因为康熙部首和扩展部首中存在和基本汉字相似的汉字。
看起来一样，实际编码是不一样的，而康熙部首很容易呈现乱码的情况（Chrome 能正常显示，Notepad++ 就显示乱码）。

{% include image.html url="/assets/images/210314-equivalent-unified-ideo~d1/20210317110836.png"
url2="/assets/images/210314-equivalent-unified-ideo~d1/20210317111809.png" %}


## 前因后果

Nôm Studies ▪ Nôm Radical List
[NÔM RADICAL LIST](http://mlp.cs.nyu.edu/chunom/xradicals.html)
Source: Unicode 6.0 Standard CJKV Unified Ideographs (UniHan)

This table includes URN (Unicode Radical Number), 214 KangXi radicals [codes U+2F00-2FD5],
110 Supplement CJKV Radicals [codes U+2E80-2EF3], with their variants and simplified forms.

找了很多文章，始终不完整或者存在错误，甚至自相矛盾的地方。

* [Unicode 基本汉字、部首扩展、康熙部首对照字典 {% include relref_csdn.html %}](https://blog.csdn.net/qq_40734108/article/details/105104412)
* [这“⼀⼝”和那“一口”有什么不同，关于 unicode 一个小知识 {% include relref_csdn.html %}](https://blog.csdn.net/gstianfu/article/details/84643320)

最后在 Unicode 官网找到了最终的准确答案，完美解决。13.0.0 2019-09-09 14:10 最新发布。

* <https://www.unicode.org/Public/13.0.0/ucd/EquivalentUnifiedIdeograph.txt>
* <https://www.unicode.org/Public/13.0.0/ucd/CJKRadicals.txt>


## Equivalent UnifiedIdeograph 13.0.0 json

翻译成了 JSON 方便直接使用（UTF8 编码）：

```json
{
  "⺁": "厂",
  "⺂": "乛",
  "⺃": "乚",
  "⺄": "乙",
  "⺅": "亻",
  "⺆": "冂",
  "⺇": "𠘨",
  "⺈": "刀",
  "⺉": "刂",
  "⺊": "卜",
  "⺋": "㔾",
  "⺌": "小",
  "⺍": "小",
  "⺎": "兀",
  "⺏": "尣",
  "⺐": "尢",
  "⺑": "𡯂",
  "⺒": "巳",
  "⺓": "幺",
  "⺔": "彑",
  "⺕": "彐",
  "⺖": "忄",
  "⺗": "心",
  "⺘": "扌",
  "⺙": "攵",
  "⺛": "旡",
  "⺜": "日",
  "⺝": "月",
  "⺞": "歺",
  "⺟": "母",
  "⺠": "民",
  "⺡": "氵",
  "⺢": "氺",
  "⺣": "灬",
  "⺤": "爫",
  "⺥": "爫",
  "⺦": "丬",
  "⺧": "牛",
  "⺨": "犭",
  "⺩": "王",
  "⺪": "𤴔",
  "⺫": "目",
  "⺬": "示",
  "⺭": "礻",
  "⺮": "𥫗",
  "⺯": "糹",
  "⺰": "纟",
  "⺱": "罓",
  "⺲": "罒",
  "⺳": "㓁",
  "⺴": "冗",
  "⺵": "𦉫",
  "⺶": "羊",
  "⺷": "𦍌",
  "⺸": "𦍋",
  "⺹": "耂",
  "⺺": "肀",
  "⺻": "聿",
  "⺼": "肉",
  "⺽": "𦥑",
  "⺾": "艹",
  "⺿": "艹",
  "⻀": "艹",
  "⻁": "虎",
  "⻂": "衤",
  "⻃": "覀",
  "⻄": "西",
  "⻅": "见",
  "⻆": "角",
  "⻇": "𧢲",
  "⻈": "讠",
  "⻉": "贝",
  "⻊": "𧾷",
  "⻋": "车",
  "⻌": "辶",
  "⻍": "辶",
  "⻎": "辶",
  "⻏": "邑",
  "⻐": "钅",
  "⻑": "長",
  "⻒": "镸",
  "⻓": "长",
  "⻔": "门",
  "⻕": "𨸏",
  "⻖": "阝",
  "⻗": "雨",
  "⻘": "青",
  "⻙": "韦",
  "⻚": "页",
  "⻛": "风",
  "⻜": "飞",
  "⻝": "食",
  "⻞": "𩙿",
  "⻟": "飠",
  "⻠": "饣",
  "⻡": "𩠐",
  "⻢": "马",
  "⻣": "骨",
  "⻤": "鬼",
  "⻥": "鱼",
  "⻦": "鸟",
  "⻧": "卤",
  "⻨": "麦",
  "⻩": "黄",
  "⻪": "黾",
  "⻫": "斉",
  "⻬": "齐",
  "⻭": "歯",
  "⻮": "齿",
  "⻯": "竜",
  "⻰": "龙",
  "⻱": "龜",
  "⻲": "亀",
  "⻳": "龟",
  "⼀": "一",
  "⼁": "丨",
  "⼂": "丶",
  "⼃": "丿",
  "⼄": "乙",
  "⼅": "亅",
  "⼆": "二",
  "⼇": "亠",
  "⼈": "人",
  "⼉": "儿",
  "⼊": "入",
  "⼋": "八",
  "⼌": "冂",
  "⼍": "冖",
  "⼎": "冫",
  "⼏": "几",
  "⼐": "凵",
  "⼑": "刀",
  "⼒": "力",
  "⼓": "勹",
  "⼔": "匕",
  "⼕": "匚",
  "⼖": "匸",
  "⼗": "十",
  "⼘": "卜",
  "⼙": "卩",
  "⼚": "厂",
  "⼛": "厶",
  "⼜": "又",
  "⼝": "口",
  "⼞": "囗",
  "⼟": "土",
  "⼠": "士",
  "⼡": "夂",
  "⼢": "夊",
  "⼣": "夕",
  "⼤": "大",
  "⼥": "女",
  "⼦": "子",
  "⼧": "宀",
  "⼨": "寸",
  "⼩": "小",
  "⼪": "尢",
  "⼫": "尸",
  "⼬": "屮",
  "⼭": "山",
  "⼮": "巛",
  "⼯": "工",
  "⼰": "己",
  "⼱": "巾",
  "⼲": "干",
  "⼳": "幺",
  "⼴": "广",
  "⼵": "廴",
  "⼶": "廾",
  "⼷": "弋",
  "⼸": "弓",
  "⼹": "彐",
  "⼺": "彡",
  "⼻": "彳",
  "⼼": "心",
  "⼽": "戈",
  "⼾": "戶",
  "⼿": "手",
  "⽀": "支",
  "⽁": "攴",
  "⽂": "文",
  "⽃": "斗",
  "⽄": "斤",
  "⽅": "方",
  "⽆": "无",
  "⽇": "日",
  "⽈": "曰",
  "⽉": "月",
  "⽊": "木",
  "⽋": "欠",
  "⽌": "止",
  "⽍": "歹",
  "⽎": "殳",
  "⽏": "毋",
  "⽐": "比",
  "⽑": "毛",
  "⽒": "氏",
  "⽓": "气",
  "⽔": "水",
  "⽕": "火",
  "⽖": "爪",
  "⽗": "父",
  "⽘": "爻",
  "⽙": "爿",
  "⽚": "片",
  "⽛": "牙",
  "⽜": "牛",
  "⽝": "犬",
  "⽞": "玄",
  "⽟": "玉",
  "⽠": "瓜",
  "⽡": "瓦",
  "⽢": "甘",
  "⽣": "生",
  "⽤": "用",
  "⽥": "田",
  "⽦": "疋",
  "⽧": "疒",
  "⽨": "癶",
  "⽩": "白",
  "⽪": "皮",
  "⽫": "皿",
  "⽬": "目",
  "⽭": "矛",
  "⽮": "矢",
  "⽯": "石",
  "⽰": "示",
  "⽱": "禸",
  "⽲": "禾",
  "⽳": "穴",
  "⽴": "立",
  "⽵": "竹",
  "⽶": "米",
  "⽷": "糸",
  "⽸": "缶",
  "⽹": "网",
  "⽺": "羊",
  "⽻": "羽",
  "⽼": "老",
  "⽽": "而",
  "⽾": "耒",
  "⽿": "耳",
  "⾀": "聿",
  "⾁": "肉",
  "⾂": "臣",
  "⾃": "自",
  "⾄": "至",
  "⾅": "臼",
  "⾆": "舌",
  "⾇": "舛",
  "⾈": "舟",
  "⾉": "艮",
  "⾊": "色",
  "⾋": "艸",
  "⾌": "虍",
  "⾍": "虫",
  "⾎": "血",
  "⾏": "行",
  "⾐": "衣",
  "⾑": "襾",
  "⾒": "見",
  "⾓": "角",
  "⾔": "言",
  "⾕": "谷",
  "⾖": "豆",
  "⾗": "豕",
  "⾘": "豸",
  "⾙": "貝",
  "⾚": "赤",
  "⾛": "走",
  "⾜": "足",
  "⾝": "身",
  "⾞": "車",
  "⾟": "辛",
  "⾠": "辰",
  "⾡": "辵",
  "⾢": "邑",
  "⾣": "酉",
  "⾤": "釆",
  "⾥": "里",
  "⾦": "金",
  "⾧": "長",
  "⾨": "門",
  "⾩": "阜",
  "⾪": "隶",
  "⾫": "隹",
  "⾬": "雨",
  "⾭": "靑",
  "⾮": "非",
  "⾯": "面",
  "⾰": "革",
  "⾱": "韋",
  "⾲": "韭",
  "⾳": "音",
  "⾴": "頁",
  "⾵": "風",
  "⾶": "飛",
  "⾷": "食",
  "⾸": "首",
  "⾹": "香",
  "⾺": "馬",
  "⾻": "骨",
  "⾼": "高",
  "⾽": "髟",
  "⾾": "鬥",
  "⾿": "鬯",
  "⿀": "鬲",
  "⿁": "鬼",
  "⿂": "魚",
  "⿃": "鳥",
  "⿄": "鹵",
  "⿅": "鹿",
  "⿆": "麥",
  "⿇": "麻",
  "⿈": "黃",
  "⿉": "黍",
  "⿊": "黑",
  "⿋": "黹",
  "⿌": "黽",
  "⿍": "鼎",
  "⿎": "鼓",
  "⿏": "鼠",
  "⿐": "鼻",
  "⿑": "齊",
  "⿒": "齒",
  "⿓": "龍",
  "⿔": "龜",
  "⿕": "龠",
  "㇆": "𠃌",
  "㇏": "乀",
  "㇐": "一",
  "㇑": "丨",
  "㇒": "丿",
  "㇓": "丿",
  "㇔": "丶",
  "㇕": "𠃍",
  "㇖": "乛",
  "㇗": "𠃊",
  "㇘": "𠃎",
  "㇙": "𠄌",
  "㇚": "亅",
  "㇛": "𡿨",
  "㇜": "𠃋",
  "㇝": "乀",
  "㇞": "𠃑",
  "㇟": "乚",
  "㇠": "乙",
  "㇡": "𠄎"
}
```


## Equivalent UnifiedIdeograph 13.0.0 txt

```ini
# EquivalentUnifiedIdeograph-13.0.0.txt
# Date: 2019-09-09, 19:41:00 GMT [KL, KW]
# © 2019 Unicode®, Inc.
# Unicode and the Unicode Logo are registered trademarks of Unicode, Inc. in the U.S. and other countries.
# For terms of use, see http://www.unicode.org/terms_of_use.html
#
# For documentation, see UAX #44: Unicode Character Database,
# at http://www.unicode.org/reports/tr44/
#
# This file defines the following property:
#
# Equivalent_Unified_Ideograph
#
# This data file lists CJK radicals and CJK strokes (aka characters
# that have the Radical=Yes property or are in the CJK Strokes block)
# for which there are reasonably equivalent CJK unified ideographs in
# that they are visually identical or near-identical.
#
# The file contains a list of lines with mappings from one code point
# or code point range to an equivalent CJK unified ideograph.
#
# Each mapping line contains two fields, separated by a semicolon (';').
# The first field contains a code point or code point range represented
# as a variable-length hexadecimal value with 4 to 6 digits. The second
# field contains a code point represented as a variable-length
# hexadecimal value with 4 to 6 digits.
#
# CJK radicals and CJK strokes for which no reasonably equivalent CJK
# unified ideographs exist are listed as comments at the end of the file.
#
# Formally, the default value of the Equivalent_Unified_Ideograph
# property for each code point is <none>, unless a mapping to some
# other character is specified in this data file. When a code point
# has the default value for the Equivalent_Unified_Ideograph property,
# that means that no other character exists whose representative glyph
# is a reasonably equivalent CJK unified ideograph.
#
# This file was originally created by Ken Lunde.
#
# ############################################################
#
# Property: Equivalent_Unified_Ideograph
#
# @missing: 0000..10FFFF; <none>

2E81       ; 5382  #     CJK RADICAL CLIFF
2E82       ; 4E5B  #     CJK RADICAL SECOND ONE
2E83       ; 4E5A  #     CJK RADICAL SECOND TWO
2E84       ; 4E59  #     CJK RADICAL SECOND THREE
2E85       ; 4EBB  #     CJK RADICAL PERSON
2E86       ; 5182  #     CJK RADICAL BOX
2E87       ; 20628 #     CJK RADICAL TABLE
2E88       ; 5200  #     CJK RADICAL KNIFE ONE
2E89       ; 5202  #     CJK RADICAL KNIFE TWO
2E8A       ; 535C  #     CJK RADICAL DIVINATION
2E8B       ; 353E  #     CJK RADICAL SEAL
2E8C..2E8D ; 5C0F  # [2] CJK RADICAL SMALL ONE..CJK RADICAL SMALL TWO
2E8E       ; 5140  #     CJK RADICAL LAME ONE
2E8F       ; 5C23  #     CJK RADICAL LAME TWO
2E90       ; 5C22  #     CJK RADICAL LAME THREE
2E91       ; 21BC2 #     CJK RADICAL LAME FOUR
2E92       ; 5DF3  #     CJK RADICAL SNAKE
2E93       ; 5E7A  #     CJK RADICAL THREAD
2E94       ; 5F51  #     CJK RADICAL SNOUT ONE
2E95       ; 5F50  #     CJK RADICAL SNOUT TWO
2E96       ; 5FC4  #     CJK RADICAL HEART ONE
2E97       ; 5FC3  #     CJK RADICAL HEART TWO
2E98       ; 624C  #     CJK RADICAL HAND
2E99       ; 6535  #     CJK RADICAL RAP
2E9B       ; 65E1  #     CJK RADICAL CHOKE
2E9C       ; 65E5  #     CJK RADICAL SUN
2E9D       ; 6708  #     CJK RADICAL MOON
2E9E       ; 6B7A  #     CJK RADICAL DEATH
2E9F       ; 6BCD  #     CJK RADICAL MOTHER
2EA0       ; 6C11  #     CJK RADICAL CIVILIAN
2EA1       ; 6C35  #     CJK RADICAL WATER ONE
2EA2       ; 6C3A  #     CJK RADICAL WATER TWO
2EA3       ; 706C  #     CJK RADICAL FIRE
2EA4..2EA5 ; 722B  # [2] CJK RADICAL PAW ONE..CJK RADICAL PAW TWO
2EA6       ; 4E2C  #     CJK RADICAL SIMPLIFIED HALF TREE TRUNK
2EA7       ; 725B  #     CJK RADICAL COW
2EA8       ; 72AD  #     CJK RADICAL DOG
2EA9       ; 738B  #     CJK RADICAL JADE
2EAA       ; 24D14 #     CJK RADICAL BOLT OF CLOTH
2EAB       ; 76EE  #     CJK RADICAL EYE
2EAC       ; 793A  #     CJK RADICAL SPIRIT ONE
2EAD       ; 793B  #     CJK RADICAL SPIRIT TWO
2EAE       ; 25AD7 #     CJK RADICAL BAMBOO
2EAF       ; 7CF9  #     CJK RADICAL SILK
2EB0       ; 7E9F  #     CJK RADICAL C-SIMPLIFIED SILK
2EB1       ; 7F53  #     CJK RADICAL NET ONE
2EB2       ; 7F52  #     CJK RADICAL NET TWO
2EB3       ; 34C1  #     CJK RADICAL NET THREE
2EB4       ; 5197  #     CJK RADICAL NET FOUR
2EB5       ; 2626B #     CJK RADICAL MESH
2EB6       ; 7F8A  #     CJK RADICAL SHEEP
2EB7       ; 2634C #     CJK RADICAL RAM
2EB8       ; 2634B #     CJK RADICAL EWE
2EB9       ; 8002  #     CJK RADICAL OLD
2EBA       ; 8080  #     CJK RADICAL BRUSH ONE
2EBB       ; 807F  #     CJK RADICAL BRUSH TWO
2EBC       ; 8089  #     CJK RADICAL MEAT
2EBD       ; 26951 #     CJK RADICAL MORTAR
2EBE..2EC0 ; 8279  # [3] CJK RADICAL GRASS ONE..CJK RADICAL GRASS THREE
2EC1       ; 864E  #     CJK RADICAL TIGER
2EC2       ; 8864  #     CJK RADICAL CLOTHES
2EC3       ; 8980  #     CJK RADICAL WEST ONE
2EC4       ; 897F  #     CJK RADICAL WEST TWO
2EC5       ; 89C1  #     CJK RADICAL C-SIMPLIFIED SEE
2EC6       ; 89D2  #     CJK RADICAL SIMPLIFIED HORN
2EC7       ; 278B2 #     CJK RADICAL HORN
2EC8       ; 8BA0  #     CJK RADICAL C-SIMPLIFIED SPEECH
2EC9       ; 8D1D  #     CJK RADICAL C-SIMPLIFIED SHELL
2ECA       ; 27FB7 #     CJK RADICAL FOOT
2ECB       ; 8F66  #     CJK RADICAL C-SIMPLIFIED CART
2ECC..2ECE ; 8FB6  # [3] CJK RADICAL SIMPLIFIED WALK..CJK RADICAL WALK TWO
2ECF       ; 9091  #     CJK RADICAL CITY
2ED0       ; 9485  #     CJK RADICAL C-SIMPLIFIED GOLD
2ED1       ; 9577  #     CJK RADICAL LONG ONE
2ED2       ; 9578  #     CJK RADICAL LONG TWO
2ED3       ; 957F  #     CJK RADICAL C-SIMPLIFIED LONG
2ED4       ; 95E8  #     CJK RADICAL C-SIMPLIFIED GATE
2ED5       ; 28E0F #     CJK RADICAL MOUND ONE
2ED6       ; 961D  #     CJK RADICAL MOUND TWO
2ED7       ; 96E8  #     CJK RADICAL RAIN
2ED8       ; 9752  #     CJK RADICAL BLUE
2ED9       ; 97E6  #     CJK RADICAL C-SIMPLIFIED TANNED LEATHER
2EDA       ; 9875  #     CJK RADICAL C-SIMPLIFIED LEAF
2EDB       ; 98CE  #     CJK RADICAL C-SIMPLIFIED WIND
2EDC       ; 98DE  #     CJK RADICAL C-SIMPLIFIED FLY
2EDD       ; 98DF  #     CJK RADICAL EAT ONE
2EDE       ; 2967F #     CJK RADICAL EAT TWO
2EDF       ; 98E0  #     CJK RADICAL EAT THREE
2EE0       ; 9963  #     CJK RADICAL C-SIMPLIFIED EAT
2EE1       ; 29810 #     CJK RADICAL HEAD
2EE2       ; 9A6C  #     CJK RADICAL C-SIMPLIFIED HORSE
2EE3       ; 9AA8  #     CJK RADICAL BONE
2EE4       ; 9B3C  #     CJK RADICAL GHOST
2EE5       ; 9C7C  #     CJK RADICAL C-SIMPLIFIED FISH
2EE6       ; 9E1F  #     CJK RADICAL C-SIMPLIFIED BIRD
2EE7       ; 5364  #     CJK RADICAL C-SIMPLIFIED SALT
2EE8       ; 9EA6  #     CJK RADICAL SIMPLIFIED WHEAT
2EE9       ; 9EC4  #     CJK RADICAL SIMPLIFIED YELLOW
2EEA       ; 9EFE  #     CJK RADICAL C-SIMPLIFIED FROG
2EEB       ; 6589  #     CJK RADICAL J-SIMPLIFIED EVEN
2EEC       ; 9F50  #     CJK RADICAL C-SIMPLIFIED EVEN
2EED       ; 6B6F  #     CJK RADICAL J-SIMPLIFIED TOOTH
2EEE       ; 9F7F  #     CJK RADICAL C-SIMPLIFIED TOOTH
2EEF       ; 7ADC  #     CJK RADICAL J-SIMPLIFIED DRAGON
2EF0       ; 9F99  #     CJK RADICAL C-SIMPLIFIED DRAGON
2EF1       ; 9F9C  #     CJK RADICAL TURTLE
2EF2       ; 4E80  #     CJK RADICAL J-SIMPLIFIED TURTLE
2EF3       ; 9F9F  #     CJK RADICAL C-SIMPLIFIED TURTLE
2F00       ; 4E00  #     KANGXI RADICAL ONE
2F01       ; 4E28  #     KANGXI RADICAL LINE
2F02       ; 4E36  #     KANGXI RADICAL DOT
2F03       ; 4E3F  #     KANGXI RADICAL SLASH
2F04       ; 4E59  #     KANGXI RADICAL SECOND
2F05       ; 4E85  #     KANGXI RADICAL HOOK
2F06       ; 4E8C  #     KANGXI RADICAL TWO
2F07       ; 4EA0  #     KANGXI RADICAL LID
2F08       ; 4EBA  #     KANGXI RADICAL MAN
2F09       ; 513F  #     KANGXI RADICAL LEGS
2F0A       ; 5165  #     KANGXI RADICAL ENTER
2F0B       ; 516B  #     KANGXI RADICAL EIGHT
2F0C       ; 5182  #     KANGXI RADICAL DOWN BOX
2F0D       ; 5196  #     KANGXI RADICAL COVER
2F0E       ; 51AB  #     KANGXI RADICAL ICE
2F0F       ; 51E0  #     KANGXI RADICAL TABLE
2F10       ; 51F5  #     KANGXI RADICAL OPEN BOX
2F11       ; 5200  #     KANGXI RADICAL KNIFE
2F12       ; 529B  #     KANGXI RADICAL POWER
2F13       ; 52F9  #     KANGXI RADICAL WRAP
2F14       ; 5315  #     KANGXI RADICAL SPOON
2F15       ; 531A  #     KANGXI RADICAL RIGHT OPEN BOX
2F16       ; 5338  #     KANGXI RADICAL HIDING ENCLOSURE
2F17       ; 5341  #     KANGXI RADICAL TEN
2F18       ; 535C  #     KANGXI RADICAL DIVINATION
2F19       ; 5369  #     KANGXI RADICAL SEAL
2F1A       ; 5382  #     KANGXI RADICAL CLIFF
2F1B       ; 53B6  #     KANGXI RADICAL PRIVATE
2F1C       ; 53C8  #     KANGXI RADICAL AGAIN
2F1D       ; 53E3  #     KANGXI RADICAL MOUTH
2F1E       ; 56D7  #     KANGXI RADICAL ENCLOSURE
2F1F       ; 571F  #     KANGXI RADICAL EARTH
2F20       ; 58EB  #     KANGXI RADICAL SCHOLAR
2F21       ; 5902  #     KANGXI RADICAL GO
2F22       ; 590A  #     KANGXI RADICAL GO SLOWLY
2F23       ; 5915  #     KANGXI RADICAL EVENING
2F24       ; 5927  #     KANGXI RADICAL BIG
2F25       ; 5973  #     KANGXI RADICAL WOMAN
2F26       ; 5B50  #     KANGXI RADICAL CHILD
2F27       ; 5B80  #     KANGXI RADICAL ROOF
2F28       ; 5BF8  #     KANGXI RADICAL INCH
2F29       ; 5C0F  #     KANGXI RADICAL SMALL
2F2A       ; 5C22  #     KANGXI RADICAL LAME
2F2B       ; 5C38  #     KANGXI RADICAL CORPSE
2F2C       ; 5C6E  #     KANGXI RADICAL SPROUT
2F2D       ; 5C71  #     KANGXI RADICAL MOUNTAIN
2F2E       ; 5DDB  #     KANGXI RADICAL RIVER
2F2F       ; 5DE5  #     KANGXI RADICAL WORK
2F30       ; 5DF1  #     KANGXI RADICAL ONESELF
2F31       ; 5DFE  #     KANGXI RADICAL TURBAN
2F32       ; 5E72  #     KANGXI RADICAL DRY
2F33       ; 5E7A  #     KANGXI RADICAL SHORT THREAD
2F34       ; 5E7F  #     KANGXI RADICAL DOTTED CLIFF
2F35       ; 5EF4  #     KANGXI RADICAL LONG STRIDE
2F36       ; 5EFE  #     KANGXI RADICAL TWO HANDS
2F37       ; 5F0B  #     KANGXI RADICAL SHOOT
2F38       ; 5F13  #     KANGXI RADICAL BOW
2F39       ; 5F50  #     KANGXI RADICAL SNOUT
2F3A       ; 5F61  #     KANGXI RADICAL BRISTLE
2F3B       ; 5F73  #     KANGXI RADICAL STEP
2F3C       ; 5FC3  #     KANGXI RADICAL HEART
2F3D       ; 6208  #     KANGXI RADICAL HALBERD
2F3E       ; 6236  #     KANGXI RADICAL DOOR
2F3F       ; 624B  #     KANGXI RADICAL HAND
2F40       ; 652F  #     KANGXI RADICAL BRANCH
2F41       ; 6534  #     KANGXI RADICAL RAP
2F42       ; 6587  #     KANGXI RADICAL SCRIPT
2F43       ; 6597  #     KANGXI RADICAL DIPPER
2F44       ; 65A4  #     KANGXI RADICAL AXE
2F45       ; 65B9  #     KANGXI RADICAL SQUARE
2F46       ; 65E0  #     KANGXI RADICAL NOT
2F47       ; 65E5  #     KANGXI RADICAL SUN
2F48       ; 66F0  #     KANGXI RADICAL SAY
2F49       ; 6708  #     KANGXI RADICAL MOON
2F4A       ; 6728  #     KANGXI RADICAL TREE
2F4B       ; 6B20  #     KANGXI RADICAL LACK
2F4C       ; 6B62  #     KANGXI RADICAL STOP
2F4D       ; 6B79  #     KANGXI RADICAL DEATH
2F4E       ; 6BB3  #     KANGXI RADICAL WEAPON
2F4F       ; 6BCB  #     KANGXI RADICAL DO NOT
2F50       ; 6BD4  #     KANGXI RADICAL COMPARE
2F51       ; 6BDB  #     KANGXI RADICAL FUR
2F52       ; 6C0F  #     KANGXI RADICAL CLAN
2F53       ; 6C14  #     KANGXI RADICAL STEAM
2F54       ; 6C34  #     KANGXI RADICAL WATER
2F55       ; 706B  #     KANGXI RADICAL FIRE
2F56       ; 722A  #     KANGXI RADICAL CLAW
2F57       ; 7236  #     KANGXI RADICAL FATHER
2F58       ; 723B  #     KANGXI RADICAL DOUBLE X
2F59       ; 723F  #     KANGXI RADICAL HALF TREE TRUNK
2F5A       ; 7247  #     KANGXI RADICAL SLICE
2F5B       ; 7259  #     KANGXI RADICAL FANG
2F5C       ; 725B  #     KANGXI RADICAL COW
2F5D       ; 72AC  #     KANGXI RADICAL DOG
2F5E       ; 7384  #     KANGXI RADICAL PROFOUND
2F5F       ; 7389  #     KANGXI RADICAL JADE
2F60       ; 74DC  #     KANGXI RADICAL MELON
2F61       ; 74E6  #     KANGXI RADICAL TILE
2F62       ; 7518  #     KANGXI RADICAL SWEET
2F63       ; 751F  #     KANGXI RADICAL LIFE
2F64       ; 7528  #     KANGXI RADICAL USE
2F65       ; 7530  #     KANGXI RADICAL FIELD
2F66       ; 758B  #     KANGXI RADICAL BOLT OF CLOTH
2F67       ; 7592  #     KANGXI RADICAL SICKNESS
2F68       ; 7676  #     KANGXI RADICAL DOTTED TENT
2F69       ; 767D  #     KANGXI RADICAL WHITE
2F6A       ; 76AE  #     KANGXI RADICAL SKIN
2F6B       ; 76BF  #     KANGXI RADICAL DISH
2F6C       ; 76EE  #     KANGXI RADICAL EYE
2F6D       ; 77DB  #     KANGXI RADICAL SPEAR
2F6E       ; 77E2  #     KANGXI RADICAL ARROW
2F6F       ; 77F3  #     KANGXI RADICAL STONE
2F70       ; 793A  #     KANGXI RADICAL SPIRIT
2F71       ; 79B8  #     KANGXI RADICAL TRACK
2F72       ; 79BE  #     KANGXI RADICAL GRAIN
2F73       ; 7A74  #     KANGXI RADICAL CAVE
2F74       ; 7ACB  #     KANGXI RADICAL STAND
2F75       ; 7AF9  #     KANGXI RADICAL BAMBOO
2F76       ; 7C73  #     KANGXI RADICAL RICE
2F77       ; 7CF8  #     KANGXI RADICAL SILK
2F78       ; 7F36  #     KANGXI RADICAL JAR
2F79       ; 7F51  #     KANGXI RADICAL NET
2F7A       ; 7F8A  #     KANGXI RADICAL SHEEP
2F7B       ; 7FBD  #     KANGXI RADICAL FEATHER
2F7C       ; 8001  #     KANGXI RADICAL OLD
2F7D       ; 800C  #     KANGXI RADICAL AND
2F7E       ; 8012  #     KANGXI RADICAL PLOW
2F7F       ; 8033  #     KANGXI RADICAL EAR
2F80       ; 807F  #     KANGXI RADICAL BRUSH
2F81       ; 8089  #     KANGXI RADICAL MEAT
2F82       ; 81E3  #     KANGXI RADICAL MINISTER
2F83       ; 81EA  #     KANGXI RADICAL SELF
2F84       ; 81F3  #     KANGXI RADICAL ARRIVE
2F85       ; 81FC  #     KANGXI RADICAL MORTAR
2F86       ; 820C  #     KANGXI RADICAL TONGUE
2F87       ; 821B  #     KANGXI RADICAL OPPOSE
2F88       ; 821F  #     KANGXI RADICAL BOAT
2F89       ; 826E  #     KANGXI RADICAL STOPPING
2F8A       ; 8272  #     KANGXI RADICAL COLOR
2F8B       ; 8278  #     KANGXI RADICAL GRASS
2F8C       ; 864D  #     KANGXI RADICAL TIGER
2F8D       ; 866B  #     KANGXI RADICAL INSECT
2F8E       ; 8840  #     KANGXI RADICAL BLOOD
2F8F       ; 884C  #     KANGXI RADICAL WALK ENCLOSURE
2F90       ; 8863  #     KANGXI RADICAL CLOTHES
2F91       ; 897E  #     KANGXI RADICAL WEST
2F92       ; 898B  #     KANGXI RADICAL SEE
2F93       ; 89D2  #     KANGXI RADICAL HORN
2F94       ; 8A00  #     KANGXI RADICAL SPEECH
2F95       ; 8C37  #     KANGXI RADICAL VALLEY
2F96       ; 8C46  #     KANGXI RADICAL BEAN
2F97       ; 8C55  #     KANGXI RADICAL PIG
2F98       ; 8C78  #     KANGXI RADICAL BADGER
2F99       ; 8C9D  #     KANGXI RADICAL SHELL
2F9A       ; 8D64  #     KANGXI RADICAL RED
2F9B       ; 8D70  #     KANGXI RADICAL RUN
2F9C       ; 8DB3  #     KANGXI RADICAL FOOT
2F9D       ; 8EAB  #     KANGXI RADICAL BODY
2F9E       ; 8ECA  #     KANGXI RADICAL CART
2F9F       ; 8F9B  #     KANGXI RADICAL BITTER
2FA0       ; 8FB0  #     KANGXI RADICAL MORNING
2FA1       ; 8FB5  #     KANGXI RADICAL WALK
2FA2       ; 9091  #     KANGXI RADICAL CITY
2FA3       ; 9149  #     KANGXI RADICAL WINE
2FA4       ; 91C6  #     KANGXI RADICAL DISTINGUISH
2FA5       ; 91CC  #     KANGXI RADICAL VILLAGE
2FA6       ; 91D1  #     KANGXI RADICAL GOLD
2FA7       ; 9577  #     KANGXI RADICAL LONG
2FA8       ; 9580  #     KANGXI RADICAL GATE
2FA9       ; 961C  #     KANGXI RADICAL MOUND
2FAA       ; 96B6  #     KANGXI RADICAL SLAVE
2FAB       ; 96B9  #     KANGXI RADICAL SHORT TAILED BIRD
2FAC       ; 96E8  #     KANGXI RADICAL RAIN
2FAD       ; 9751  #     KANGXI RADICAL BLUE
2FAE       ; 975E  #     KANGXI RADICAL WRONG
2FAF       ; 9762  #     KANGXI RADICAL FACE
2FB0       ; 9769  #     KANGXI RADICAL LEATHER
2FB1       ; 97CB  #     KANGXI RADICAL TANNED LEATHER
2FB2       ; 97ED  #     KANGXI RADICAL LEEK
2FB3       ; 97F3  #     KANGXI RADICAL SOUND
2FB4       ; 9801  #     KANGXI RADICAL LEAF
2FB5       ; 98A8  #     KANGXI RADICAL WIND
2FB6       ; 98DB  #     KANGXI RADICAL FLY
2FB7       ; 98DF  #     KANGXI RADICAL EAT
2FB8       ; 9996  #     KANGXI RADICAL HEAD
2FB9       ; 9999  #     KANGXI RADICAL FRAGRANT
2FBA       ; 99AC  #     KANGXI RADICAL HORSE
2FBB       ; 9AA8  #     KANGXI RADICAL BONE
2FBC       ; 9AD8  #     KANGXI RADICAL TALL
2FBD       ; 9ADF  #     KANGXI RADICAL HAIR
2FBE       ; 9B25  #     KANGXI RADICAL FIGHT
2FBF       ; 9B2F  #     KANGXI RADICAL SACRIFICIAL WINE
2FC0       ; 9B32  #     KANGXI RADICAL CAULDRON
2FC1       ; 9B3C  #     KANGXI RADICAL GHOST
2FC2       ; 9B5A  #     KANGXI RADICAL FISH
2FC3       ; 9CE5  #     KANGXI RADICAL BIRD
2FC4       ; 9E75  #     KANGXI RADICAL SALT
2FC5       ; 9E7F  #     KANGXI RADICAL DEER
2FC6       ; 9EA5  #     KANGXI RADICAL WHEAT
2FC7       ; 9EBB  #     KANGXI RADICAL HEMP
2FC8       ; 9EC3  #     KANGXI RADICAL YELLOW
2FC9       ; 9ECD  #     KANGXI RADICAL MILLET
2FCA       ; 9ED1  #     KANGXI RADICAL BLACK
2FCB       ; 9EF9  #     KANGXI RADICAL EMBROIDERY
2FCC       ; 9EFD  #     KANGXI RADICAL FROG
2FCD       ; 9F0E  #     KANGXI RADICAL TRIPOD
2FCE       ; 9F13  #     KANGXI RADICAL DRUM
2FCF       ; 9F20  #     KANGXI RADICAL RAT
2FD0       ; 9F3B  #     KANGXI RADICAL NOSE
2FD1       ; 9F4A  #     KANGXI RADICAL EVEN
2FD2       ; 9F52  #     KANGXI RADICAL TOOTH
2FD3       ; 9F8D  #     KANGXI RADICAL DRAGON
2FD4       ; 9F9C  #     KANGXI RADICAL TURTLE
2FD5       ; 9FA0  #     KANGXI RADICAL FLUTE
31C6       ; 200CC #     CJK STROKE HZG
31CF       ; 4E40  #     CJK STROKE N
31D0       ; 4E00  #     CJK STROKE H
31D1       ; 4E28  #     CJK STROKE S
31D2..31D3 ; 4E3F  # [2] CJK STROKE P..CJK STROKE SP
31D4       ; 4E36  #     CJK STROKE D
31D5       ; 200CD #     CJK STROKE HZ
31D6       ; 4E5B  #     CJK STROKE HG
31D7       ; 200CA #     CJK STROKE SZ
31D8       ; 200CE #     CJK STROKE SWZ
31D9       ; 2010C #     CJK STROKE ST
31DA       ; 4E85  #     CJK STROKE SG
31DB       ; 21FE8 #     CJK STROKE PD
31DC       ; 200CB #     CJK STROKE PZ
31DD       ; 4E40  #     CJK STROKE TN
31DE       ; 200D1 #     CJK STROKE SZZ
31DF       ; 4E5A  #     CJK STROKE SWG
31E0       ; 4E59  #     CJK STROKE HXWG
31E1       ; 2010E #     CJK STROKE HZZZG

# The following characters have no equivalent CJK unified ideograph.

# 2E80; CJK RADICAL REPEAT
# 31C0; CJK STROKE T
# 31C1; CJK STROKE WG
# 31C2; CJK STROKE XG
# 31C3; CJK STROKE BXG
# 31C4; CJK STROKE SW
# 31C5; CJK STROKE HZZ
# 31C7; CJK STROKE HP
# 31C8; CJK STROKE HZWG
# 31C9; CJK STROKE SZWG
# 31CA; CJK STROKE HZT
# 31CB; CJK STROKE HZZP
# 31CC; CJK STROKE HPWG
# 31CD; CJK STROKE HZW
# 31CE; CJK STROKE HZZZ
# 31E2; CJK STROKE PG
# 31E3; CJK STROKE Q

# EOF
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-14-Equivalent-Unified-Ideograph.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://mlp.cs.nyu.edu/chunom/xradicals.html]({% include relref.html url="/backup/2021-03-14-Equivalent-Unified-Ideograph.md/mlp.cs.nyu.edu/d3b59c9f.html" %})
- [https://blog.csdn.net/qq_40734108/article/details/105104412]({% include relref.html url="/backup/2021-03-14-Equivalent-Unified-Ideograph.md/blog.csdn.net/049c4a4b.html" %})
- [https://blog.csdn.net/gstianfu/article/details/84643320]({% include relref.html url="/backup/2021-03-14-Equivalent-Unified-Ideograph.md/blog.csdn.net/1e7a41ac.html" %})
- [https://www.unicode.org/Public/13.0.0/ucd/EquivalentUnifiedIdeograph.txt]({% include relref.html url="/backup/2021-03-14-Equivalent-Unified-Ideograph.md/www.unicode.org/cd98bbe9.txt" %})
- [https://www.unicode.org/Public/13.0.0/ucd/CJKRadicals.txt]({% include relref.html url="/backup/2021-03-14-Equivalent-Unified-Ideograph.md/www.unicode.org/0ebeb802.txt" %})
- [http://www.unicode.org/terms_of_use.html]({% include relref.html url="/backup/2021-03-14-Equivalent-Unified-Ideograph.md/www.unicode.org/ab3c7f65.html" %})
- [http://www.unicode.org/reports/tr44/]({% include relref.html url="/backup/2021-03-14-Equivalent-Unified-Ideograph.md/www.unicode.org/24de9f24.html" %})