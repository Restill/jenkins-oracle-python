# -*- coding: utf-8 -*-
"""
@author: liuyw
"""
from splinter.browser import Browser
from time import sleep
import traceback
import time,sys
class huoche(object):
    """docstring for huoche"""
executable_path = ''
username = u"xxx@qq.com"
passwd = u"xxxx"
# cookies值得自己去找, 下面两个分别是上海, 太原南
starts = u"%u4E0A%u6D77%2CSHH"
ends = u"%u592A%u539F%2CTYV"
# 时间格式2018-01-19
dtime = u"2018-01-19"
# 车次，选择第几趟，0则从上之下依次点击
order = 0
###乘客名
users = [u"xxx", u"xxx"]
##席位
xb = ("二等座")
pz = "成人票"
"""网址"""
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
buy = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
login_url = "https://kyfw.12306.cn/otn/login/init"

def __init__(self):
    self.driver_name = 'chrome'
    self.executable_path = "/usr/local/bin/chromedriver"

def login(self):
    self.driver.visit(self.login_url)
    self.driver.fill("loginUserDTO.user_name", self.username)

# sleep(1)
#self.driver.fill("userDTO.password", self.passwd)
print("等待验证码，自行输入...")
while True:
    if self.driver.url != self.initmy_url:
        sleep(1)
    else:
        break

def start(self):
    global hutch
    self.driver = Browser( driver_name=self.driver_name, executable_path=self.executable_path )
    self.driver.driver.set_window_size( 1400, 1000 )
    self.login()
    # sleep(1)
    self.driver.visit( self.ticket_url )
    try:
        print( "购票页面开始..." )
        # sleep(1)
        self.driver.cookies.add( {"_jc_save_fromStation": self.starts} )
        self.driver.cookies.add( {"_jc_save_toStation": self.ends} )
        self.driver.cookies.add( {"_jc_save_fromDate": self.dtime} )

        self.driver.reload()
        count = 0
    finally:
        if self.order != 0:
            while self.driver.url == self.ticket_url:
                self.driver.find_by_text( u"查询" ).click()
                count += 1
                print( "循环点击查询... 第 %s 次" % count )
                # sleep(1)
                try:
                    self.driver.find_by_text( u"预订" )[self.order - 1].click()
                except Exception as e:
                    print( "e" )
                    print( "还没开始预订" )
                else:
                    while self.driver.url == self.ticket_url:
                        self.driver.find_by_text( u"查询" ).click()
            count += 1
            print( "循环点击查询... 第 %s 次" % count )
            # sleep(0.8)
            try:
                for i in self.driver.find_by_text( u"预订" ):
                    i.click()
                    sleep( 1 )
            except Exception as e:
                print( "e" )
                print( "还没开始预订 %s" % count )
                'continue'
                print( "开始预订..." )
                # sleep(3)
                self.driver.reload()
                sleep( 1 )
                print( '开始选择用户...' )
                for user in self.users:
                    self.driver.find_by_text( user ).last.click()
                    print( "提交订单..." )
                    sleep( 1 )
                    self.driver.find_by_text( self.pz ).click()
                    self.driver.find_by_id( '' ).select( self.pz )
                    sleep( 1 )
                    self.driver.find_by_text( self.xb ).click()
                    sleep( 1 )
                    self.driver.find_by_id( 'submitOrder_id' ).click()
                    print( "开始选座..." )
                    self.driver.find_by_id( '1D' ).last.click()
                    self.driver.find_by_id( '1F' ).last.click()
                    sleep( 1.5 )
                    print( "确认选座..." )
                    self.driver.find_by_id( 'qr_submit_id' ).click()
            except Exception as e:
                print( "e" )
            finally:
                if __name__ == '__main__':
                    hutch = hutch()
                    hutch.start()
