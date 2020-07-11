#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/7/8 11:29
@Author  : jiangliming
@File    : chromedriver.py
"""
import os
import time
from selenium import webdriver
while True:
    time_now = time.strftime("%H:%M", time.localtime())  # 刷新
    if time_now == "00:02" or time_now == "00:05" or time_now == "00:07" or time_now == "01:15":
       '''此处设置每天定时的时间，每天在这几个时间点打开webdriver去进行点击进行打卡
       我这里edge已经保存登录了，所以没有登陆输入用户名密码的过程，没有的可以自己加一下
       或者自己手动登陆一次
       '''
       try:
           '''注意一定要配置对MicrosoftWebDriver.exe的版本和位置，不然运行不成功'''
           browser = webdriver.Edge('E:\\webdriver\\MicrosoftWebDriver.exe')
           browser.get('https://app.bupt.edu.cn/ncov/wap/default/index')

           #如果要登录的话的
           '''
           login = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input')
           login.send_keys("账号")
           login=browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/input")
           login.send_keys("密码")
           login=browser.find_element_by_xpath("/html/body/div[1]/div[3]")
           login.click()
           '''

           location = browser.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[8]/div/input")
           location.click()
           time.sleep((5))
           login = browser.find_element_by_xpath("/html/body/div[1]/div/div/section/div[5]/div/a")
           login.click()
           time.sleep((10))
           submit = browser.find_element_by_xpath("//*[@id=\"wapcf\"]/div/div[2]/div[2]")
           submit.click()
           browser.close()
           time.sleep(60)
       except:
           browser.close()
    continue









