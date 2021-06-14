#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
import hashlib
import json
import os
import time
from random import randint as rdint

import requests
# 是個第三方庫。

def get_chapter(): #获取试题
    with open('test_chapter.txt', mode='r', encoding='utf-16') as f:
        data = f.read()
    data = data.split()
    llen = len(data)
    chapter = [] ; IPA = [] ; pinyin = []
    for i in range(0, llen, 3):
        chapter.append(data[i])
    for i in range(1, llen, 3):
        IPA.append(data[i])
    for i in range(2, llen, 3):
        pinyin.append(data[i])
    return chapter, IPA, pinyin

def test_data(chapter, IPA, pinyin): #抽取题目并写入测试文档
    llen = len(pinyin)
    n = rdint(0, llen//3 - 1)

    test_ch = str(chapter[n]) ; test_IPA = str(IPA[n]) ; test_pinyin = str(pinyin[n])
    with open('test.txt', mode='w', encoding='utf-8') as f:
        test_text = '<customizer: interphonic>\n' + test_ch + '\n' + test_pinyin
        f.write(test_text) #写入测试文档

    lst1 = [test_ch, test_IPA, test_pinyin]
    return lst1  #返回测试数据


def test_audio():
    
    x_appid = '5cf4fb46'  # 平台给的ID，验证用。
    api_key = '8a8cc3a4f8af7e840d7ca72e00a47a5f'  # 应该是平台会给的密钥，暂时还显示不出来，可能要实名认证。验证要用。
    curTime = str(int(time.time()))  # 取得当前时间，验证用。
    url = 'http://api.xfyun.cn/v1/service/v1/ise'  # 不懂，要用。
    with open('test.txt', mode = 'r', encoding = 'UTF-8') as f:
        text = f.read()
    # 看意思好像是要直接输在里面，应该可以另建txt，用文件操作读入。
    # 以下是音频部分，交给录音。
    AUDIO_PATH = os.getcwd() + r'\test_audio.wav'  # *****重要！*****这个交给录音，想办法弄进去。
    with open(AUDIO_PATH, 'rb') as f:  # 从这行开始完全看不懂，看官方说明只要原样保留就行了。
        file_content = f.read()
    base64_audio = base64.b64encode(file_content)
    body = {'audio': base64_audio, 'text': text}
    # 音频部分结束。
    # 下两行是配置使用的模式，已经改好了，不用动。
    param = json.dumps({"aue": "raw", "result_level": "entirety", "language": "zh_cn", "category": "read_syllable"})
    paramBase64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')
    # 从下一行开始都是在制作密钥。
    m2 = hashlib.md5()
    m2.update((api_key + curTime + paramBase64).encode('utf-8'))
    checkSum = m2.hexdigest()
    x_header = {
                'X-Appid': x_appid,
                'X-CurTime': curTime,
                'X-Param': paramBase64,
                'X-CheckSum': checkSum,
                'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                }
    # 密钥制作完毕。
    # 正式的上传计算。
    req = requests.post(url, data=body, headers=x_header)  
    result = req.content.decode('utf-8')
    text = str(result)
    if 'illegal' in text:
        return -1
    index = text.index('total_score')
    start = index + 15
    end = start + 8
    score = text[start:end]
    return score


# 最后两行记得注释掉。

