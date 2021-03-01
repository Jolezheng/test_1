#The is a test program of students key webdriver
#coding=utf-8
#data:2021.1.15
#chrome version:87.0.4280.88
#selenium version:3.141.0
#Licence:Apache 2.0
#Chromedriver.exe version:87.0.4280.88_win32

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors') 
chrome_options.add_argument('--ignore-ssl-errors')
#引入Keys包
from selenium.webdriver.common.keys import Keys
#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
import time as t,os 
from selenium.common.exceptions import NoSuchElementException
import file_report as opt

current_time =t.strftime("%Y-%m-%d-%H_%M_%S", t.localtime(t.time()))

class Frameset(object):
	"""docstring for ClassName"""
	def frame1(self):
		driver=self.driver
		driver.find_element_by_xpath('//*[@id="frm_menu"]')
		driver.switch_to.frame('contents')

	def frame2(self):
		driver=self.driver
		driver.find_element_by_xpath('//*[@id="frm_menu"]')
		driver.switch_to.frame('midFrame')

	def frame_default(self):
		self.driver.switch_to.default_content()

class Jfmall_test(object):
	"""docstring for Jfmall_test"""
		#启动浏览器
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()

	def screen(self):
		#截图保存
        # 新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
		pic_path = ("E:\\Test\\" + current_time + ".png")
		print(pic_path)
		t.sleep(3)
		print(self.driver)
		self.driver.save_screenshot(pic_path)

	def Clickload(self):
		# self.driver.get('http://192.168.253.57')
		# t.sleep(3) 
		self.driver.get('http://jf.farcollege.com/Management/Admin/frame/HomePage.aspx')
		btn1=self.driver.find_element_by_xpath('//*[@id="textName"]')
		btn2=self.driver.find_element_by_xpath('//*[@id="textpass"]')
		# self.driver.switch_to_frame('top')
		btn1.clear()
		btn1.send_keys('admin')
		btn1.send_keys(Keys.TAB)
		t.sleep(2)
		btn2.clear()
		btn2.send_keys('123456')
		btn2.send_keys(Keys.ENTER)
		t.sleep(2)
		self.driver.switch_to.frame('top')
		# self.driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]')
		ele=self.driver.find_element_by_xpath('//*[@id="nopng"]/span')
		report=ele.text
		if '积分商城' in report:
			print("登录成功！")
		else:
			print("登录 失败！请重新登录！")
		# self.driver.switch_to.default_content()
		Frameset.frame_default(self)

	def banner(self):
		driver=self.driver
		# driver.switch_to.frame(0)
		# t.sleep(1.0)
		# driver.switch_to.frame(iframe)
		# driver.switch_to.frame('frm_menu')
		# t.sleep(1.0)
		Frameset.frame1(self)
		Click=driver.find_element_by_xpath('//*[@id="ss1"]')
		Click.click()
		t.sleep(2.0)
		lst=['//*[@id="bs1"]/ul/li[1]/a','//*[@id="bs1"]/ul/li[2]/a']
		btn=driver.find_element_by_xpath(lst[0])
		btn.click()
		t.sleep(2.0)
		driver.switch_to.default_content()
		driver.switch_to.frame('midFrame')
		ele=driver.find_element_by_xpath('//*[@id="form1"]/div[3]/table/tbody/tr[1]/td[1]')
		report=ele.text
		if '图片标题' in report:
			print('banner>>新增图片管理检测成功！',file=opt.Write().text_report)
		else:
			print('banner>>新增图片管理检测失败！请检查系统！',file=opt.Write().test_report)
		driver.switch_to.default_content()
		t.sleep(2.0)
		# for x in lst:
		# 	btn=driver.find_element_by_xpath(x)
		# 	btn.click()
		# 	t.sleep(2.0)
		Frameset.frame1(self)
		# driver.switch_to.frame('contents')
		btn=driver.find_element_by_xpath(lst[1])
		btn.click()
		t.sleep(2.0)
		# driver.switch_to.default_content()
		driver.switch_to.default_content()
		t.sleep(2.0)
		driver.switch_to.frame('midFrame')
		ele=driver.find_element_by_xpath('//*[@id="divPreview"]')
		report=ele.text
		if '点击图片' in report:
			print('banner>>首页图片管理检测成功！',file=opt.Write().text_report)
		else:
			print("banner>>首页图片检测失败！请检查系统！"file=opt.Write.text_report)
		t.sleep(2.0)
		driver.switch_to.default_content()

		# i=0
		# while i<2:
		# 	for x in lst:
		# 		btn=driver.find_element_by_xpath(x)
		# 		btn.click()
		# 		t.sleep(2.0)
		# 		if i==1:
		# 			# driver.find_element_by_xpath('//*[@id="frm_menu"]')
		# 			driver.switch_to.frame('midFrame')
		# 			ele=driver.find_element_by_xpath('//*[@id="form1"]/div[3]/table/tbody/tr[1]/td[1]')
		# 			report=ele.text
		# 			if '图片标题' in report:
		# 				print('banner>>新增图片管理检测成功！')
		# 			else:
		# 				print('banner>>新增图片管理检测失败！请检查系统！')
		# 		else:
		# 			ele=driver.find_element_by_xpath('//*[@id="divPreview"]')
		# 			report=ele.text
		# 			if '点击图片' in report:
		# 				print('banner>>首页图片管理检测成功！')
		# 			else:
		# 				print("banner>>首页图片检测失败！请检查系统！")
		# 	i+=1

	def commodity(self):
		driver=self.driver
		Frameset.frame1(self)
		Click=driver.find_element_by_xpath('//*[@id="ss88"]')
		Click.click()
		t.sleep(2.0)
		lst=['//*[@id="bs88"]/ul/li[1]/a','//*[@id="bs88"]/ul/li[2]/a','//*[@id="bs88"]/ul/li[3]/a',\
		'//*[@id="bs88"]/ul/li[4]/a','//*[@id="bs88"]/ul/li[5]/a']
		btn=driver.find_element_by_xpath(lst[0])
		btn.click()
		t.sleep(2.0)
		
		#邮费管理
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="tableAdd"]/tbody/tr[2]/td[1]')
		report=drop.text
		if '邮费金额' in report:
			print("邮费管理检测成功！",file=opt.Write().test_report)
		else:
			print('邮费管理检测失败！请检查系统！'file=opt.Write().test_report)
		t.sleep(1)

		#商品分类
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		btn=driver.find_element_by_xpath(lst[1])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[2]/div[1]')
		report=drop.text
		if '当前分类' in report:
			print("商品分类检测成功！"file=opt.Write().test_report)
		else:
			print('商品分类检测失败！请检查系统！'file=opt.Write().test_report)
		t.sleep(1)

		#商品管理
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		btn=driver.find_element_by_xpath(lst[2])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[2]/div')
		report=drop.text
		if '是否出售' in report:
			print("商品管理检测成功！"file=opt.Write().test_report)
		else:
			print('商品管理检测失败！请检查系统！'file=opt.Write().test_report)
		t.sleep(1)

		#库存统计
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		btn=driver.find_element_by_xpath(lst[3])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="list"]/table/tbody/tr[1]/th[5]')
		report=drop.text
		if '当前库存' in report:
			print("库存统计检测成功！"file=opt.Write().test_report)
		else:
			print('库存统计检测失败！请检查系统！'file=opt.Write().test_report)
		t.sleep(1)

		#购物车管理
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		btn=driver.find_element_by_xpath(lst[4])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="list"]/table/tbody/tr[1]/th[4]')
		report=drop.text
		if '添加数量' in report:
			print("购物车检测成功！"file=opt.Write().test_report)
		else:
			print('购物车检测失败！请检查系统！'file=opt.Write().test_report)
		t.sleep(1)

		# //*[@id="tableAdd"]/tbody/tr[2]/td[1]
		# i=1
		# while i<5:
		# 	for x in lst:
		# 		btn=driver.find_element_by_xpath(x)
		# 		btn.click()
		# 		t.sleep(2.0)
		# 		if i==0:
 
		# i+=1 

	def orders(self):
		driver=self.driver
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		Click=driver.find_element_by_xpath('//*[@id="ss108"]')
		Click.click()
		t.sleep(2.0)
		lst3=['//*[@id="bs108"]/ul/li[1]/a','//*[@id="bs108"]/ul/li[2]/a','//*[@id="bs108"]/ul/li[3]/a',\
		'//*[@id="bs108"]/ul/li[4]/a','//*[@id="bs108"]/ul/li[5]/a','//*[@id="bs108"]/ul/li[6]/a']
		btn=driver.find_element_by_xpath(lst3[0])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="list"]/table/tbody/tr[1]/th[4]')
		report=drop.text
		if '添加数量' in report:
			print("购物车检测成功！"file=opt.Write().test_report)
		else:
			print('购物车检测失败！请检查系统！'file=opt.Write.test_report)
		t.sleep(1)

		#订单信息
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		btn=driver.find_element_by_xpath(lst3[1])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="list"]/table/tbody/tr[1]/th[2]')
		report=drop.text
		if '定单号' in report:
			print("订单信息检测成功！",file=opt.Write().test_report)
		else:
			print('订单信息检测失败！请检查系统！',file=opt.Write().test_report)
		t.sleep(1)

		#兑换统计
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		btn=driver.find_element_by_xpath(lst3[2])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[1]/div[1]')
		report=drop.text
		if '统计方式' in report:
			print("兑换统计检测成功！",file=opt.Write().test_report)
		else:
			print('兑换统计检测失败！请检查系统！'file=opt.Write().test_report)
		t.sleep(1)

		#商品明细查询
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		btn=driver.find_element_by_xpath(lst3[3])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/div[1]')
		report=drop.text
		if '用户名称' in report:
			print("商品明细查询检测成功！",file=opt.Write().test_report)
		else:
			print('商品明细查询检测失败！请检查系统！'file=opt.Write().test_report)
		t.sleep(1)

		#自购发货管理
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		btn=driver.find_element_by_xpath(lst3[4])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="list"]/table/tbody/tr[1]/th[2]')
		report=drop.text
		if '发货单号' in report:
			print("自购发货管理检测成功！",file=opt.Write().test_report)
		else:
			print('自购发货管理检测失败！请检查系统！'file=opt.Write().test_report)
		t.sleep(1)

		#退货查询
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame1(self)
		btn=driver.find_element_by_xpath(lst3[5])
		btn.click()
		t.sleep(2.0)
		Frameset.frame_default(self)
		t.sleep(1)
		Frameset.frame2(self)
		drop=driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/div[1]')
		report=drop.text
		if '退货日期' in report:
			print("退货查询检测成功！",file=opt.Write().test_report)
		else:
			print('退货查询检测失败！请检查系统！',file=opt.Write().test_report)
		t.sleep(1)

	# 	for x in lst3:
	# 		btn=driver.find_element_by_xpath(x)
	# 		btn.click()
	# 		t.sleep(2.0)
	def finall(self):
		print("检测继续......")

if __name__ == '__main__':
	# ts=Jfmall_test()
	# ts.setUp()
	# ts.Clickload()
	# ts.banner()
	# print('-'*3,'banner&logo检测完毕，已输出报告','-'*3)
	# ts.commodity()
	# print('-'*3,'订单管理检测完毕，已输出报告','-'*3)
	# ts.orders()
	# print('-'*3,'订单管理检测完毕，已输出报告','-'*3)
	try:
		ts.setUp()
		print('程序初始化成功，开始检测......')
		ts.Clickload()
		ts.banner()
		print('-'*3,'banner&logo检测完毕，已输出报告','-'*3,file=opt.Write().test_report)
		ts.commodity()
		print('-'*3,'订单管理检测完毕，已输出报告','-'*3,file=opt.Write().test_report)
		ts.orders()
		print('-'*3,'订单管理检测完毕，已输出报告','-'*3,file=opt.Write().test_report)
		print('检测结束')
		ts.finall()
	except:
		ts.screen()
		print('检测进程异常！请检查系统！',file=opt.Write().test_report)
		t.sleep(2.0)

	

		
