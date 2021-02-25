#The is a test program of students key webdriver
#coding=utf-8
#data:2021.1.1
#chrome version:87.0.4280.88
#selenium version:3.141.0
#Licence:Apache 2.0
#Chromedriver.exe version:87.0.4280.88_win32

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors') 
chrome_options.add_argument('--ignore-ssl-errors')
#引入keys包
from selenium.webdriver.common.keys import Keys 
#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
import time as t,os
import file_report as opt

class GanyiChrome:
	def setUp(self):
		#启动浏览器
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()	
		
	def test_clickButton(self):
		self.driver.get("http://192.168.253.57/")
		t.sleep(3)
		self.driver.get("http://192.168.253.57/Login.aspx?orgPrex=www")
		button1=self.driver.find_element_by_id("txt_user")
		button2=self.driver.find_element_by_id("txt_pwd")
		button1.clear()
		button1.send_keys("admin")
		button1.send_keys(Keys.TAB)
		t.sleep(1)
		button2.clear()
		button2.send_keys("123456")
		button2.send_keys(Keys.ENTER)
		t.sleep(2)
	
	def study_pass(self):
		#学员端入口
		Click=self.driver.find_element_by_xpath("//*[@id='div_new_top']/div[2]/div/div[1]/a[1]")
		Click.click()
		t.sleep(2)

	# def person(self):
	# 	Click=self.driver.find_element_by_xpath('//*[@id="divTop"]/div[3]/div[1]/ul/li[1]/a')
	# 	Click.click()
	# 	t.sleep(2)
		
	def firstpage(self):
		Click=self.driver.find_element_by_xpath('//*[@id="div_new_menu"]/li[1]/a')
		Click.click()
		t.sleep(2)
		
	"""
	def mouse(self):
		move=driver.find_element_by_xpath("")
	"""
	def qiyezs(self):
		driver=self.driver
		#/User/GGKT.aspx?m=qyzs?mId=100000&amp;mPId=10&amp;mpName=企业知识&amp;mName=企业知识
		move=driver.find_element_by_xpath('//*[@id="div_new_menu"]/li[2]/a')
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_10"]/dd[1]/a').click()
		t.sleep(2)

		#driver.find_element_by_xpath('//*[@id="Type_gsly"]').click()
		list1=['//*[@id="courseMenuList"]/div[1]/div','//*[@id="courseMenuList"]/div[2]/div[1]',\
		'//*[@id="courseMenuList"]/div[3]/div[1]','//*[@id="courseMenuList"]/div[4]/div[1]']
		for x in list1:
			move=driver.find_element_by_xpath(x)
			ActionChains(driver).move_to_element(move).perform()
			#Click=driver.find_element_by_xpath(x)
			#Click.click()
			t.sleep(1)

		ele=self.driver.find_element_by_xpath('//*[@id="MasterBox"]/div[3]/div/div[1]')
		report=ele.text
		info='热门课程'
		if info in report:
			print('热门课程检测成功！',file=opt.Write().test_report)
		else:
			print("热门课程检测失败！请重新检测！",file=opt.Write().test_report)

		"""
		driver.find_element_by_xpath('//*[@id="Type_ztlx"]').click()
		list2=['//*[@id="Type_ztlx"]/option[1]','//*[@id="Type_ztlx"]/option[2]','//*[@id="Type_ztlx"]/option[3]','//*[@id="Type_ztlx"]/option[4]','//*[@id="Type_ztlx"]/option[13]']
		for x in list2:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2)
		"""
		
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[2]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_10"]/dd[2]/a').click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[4]/div[1]')
		report=ele.text
		if '推荐课程'in report:
			print('推荐课检测成功！',file=opt.Write().test_report)
		else:
			print('推荐课检测失败！请检查系统！',file=opt.Write().test_report)
		
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[2]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_10"]/dd[3]/a').click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[2]/div[1]')
		report=ele.text
		if '专题课程' in report:
			print("专题课检测成功！",file=opt.Write().test_report)
		else:
			print('专题课检测失败！请检查系统！',file=opt.Write().test_report)
		"""
		qylist=["//*[@id='dl_10']/dd[1]/a","//*[@id='dl_10']/dd[2]/a","//*[@id='dl_10']/dd[3]/a"]
		for x in qylist:
			move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[2]/a")
			ActionChains(driver).move_to_element(move).perform()
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2)
			if x == "//*[@id='dl_10']/dd[3]/a":
				break
		"""
	def knowlg(self):
		driver=self.driver
		move=driver.find_element_by_xpath('//*[@id="div_new_menu"]/li[3]/a')
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_12"]/dd/a').click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="treeDemo_1_span"]')
		report=ele.text
		if '施工解决方案' in report:
			print('知识子库检测成功！',file=opt.Write().test_report)
		else:
			print('知识子库检测失败！请检查系统！',file=opt.Write().test_report)

	def renwucents(self):
		driver=self.driver
		#学习任务//*[@id="MasterBox"]/div[3]/div[2]/span[1]//*[@id="MasterBox"]/div[3]/div[2]/span[2]
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[4]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_1"]/dd[1]/a').click()
		t.sleep(2)
		Stulist=['//*[@id="MasterBox"]/div[3]/div[2]/span[1]','//*[@id="MasterBox"]/div[3]/div[2]/span[2]']
		for x in Stulist:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			#print(x+"检测成功！")
			t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[3]/div[1]')
		report=ele.text
		if '必修课' in report:
			print('学习任务检测成功！',file=opt.Write().test_report)
		else:
			print('学习任务检测失败！请检查系统！',file=opt.Write().test_report)

		#考试任务
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[4]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_1"]/dd[2]/a').click()
		t.sleep(2)
		Kslist=['//*[@id="wcy"]','//*[@id="ycy"]','//*[@id="MasterBox"]/div[4]/div[2]/span[4]']
		for x in Kslist:
			Click=driver.find_element_by_xpath(x)
			Click.click()
		t.sleep(2)

		driver.find_element_by_xpath('//*[@id="MasterBox"]/div[1]/div[1]/a').click()

		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[4]/div[1]')
		report=ele.text
		if '您有' in report:
			print('考试任务检测成功！',file=opt.Write().test_report)
		else:
			print('考试任务检测失败！请检查系统！',file=opt.Write().test_report)

		#评估任务
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[4]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_1"]/dd[3]/a').click()
		t.sleep(2)
		Pglist=['//*[@id="MasterBox"]/div[4]/div[2]/span[1]','//*[@id="MasterBox"]/div[4]/div[2]/span[2]']
		for x in Pglist:
			Click=driver.find_element_by_xpath(x)
			Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[4]/div[1]')
		report=ele.text
		if '评估待评' in report:
			print('评估任务检测成功！',file=opt.Write().test_report)
		else:
			print('评估任务检测失败！请检查系统！',file=opt.Write().test_report)

		"""
		#培训班
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[4]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_1"]/dd[4]/a').click()
		t.sleep(2)
		Pxlist=['//*[@id="MasterBox"]/div[2]/div[2]/span[2]','//*[@id="MasterBox"]/div[2]/div[2]/span[3]','//*[@id="MasterBox"]/div[2]/div[2]/span[4]','//*[@id="MasterBox"]/div[2]/div[2]/span[5]']
		for x in Pxlist:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2)
		"""

		#作业任务//*[@id="dl_1"]/dd[4]/a
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[4]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_1"]/dd[4]/a').click()
		t.sleep(2)
		Worklist=['//*[@id="MasterBox"]/div[1]/div[2]/span[1]','//*[@id="MasterBox"]/div[1]/div[2]/span[2]','//*[@id="MasterBox"]/div[1]/div[2]/span[3]','//*[@id="MasterBox"]/div[1]/div[2]/span[4]']
		for x in Worklist:
			Click=driver.find_element_by_xpath(x)
			Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[1]/div[1]')
		report=ele.text
		if '作业' in report:
			print('作业任务检测成功！',file=opt.Write().test_report)
		else:
			print('作业任务检测失败！请检查系统！',file=opt.Write().test_report)
		
		#学时排行//*[@id="MasterBox"]/div[1]/div[1]/input[2]
		move=driver.find_element_by_xpath('//*[@id="div_new_menu"]/li[4]/a')
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_1"]/dd[5]/a').click()
		t.sleep(2)
		# driver.find_element_by_xpath('//*[@id="MasterBox"]/div[1]/div[1]/input[2]').click()
		# t.sleep(1)
		# driver.find_element_by_xpath('//*[@id="btnScore"]').click()
		# t.sleep(2)
		Phlist=['//*[@id="btnScore"]','//*[@id="MasterBox"]/div[1]/div[1]/input[2]']
		for x in Phlist:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[3]/div[1]')
		report=ele.text
		if '姓名' in report:
			print('学时排行检测成功！',file=opt.Write().test_report)
		else:
			print('学时排行检测失败！请检查系统！',file=opt.Write().test_report)
		
		#培训计划//*[@id="pxb"]
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[4]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_1"]/dd[6]/a').click()
		t.sleep(2)
		Phblist=['//*[@id="pxb"]','//*[@id="MasterBox"]/div[3]/div[2]/span[1]',\
		'//*[@id="MasterBox"]/div[3]/div[2]/span[2]','//*[@id="MasterBox"]/div[3]/div[2]/span[3]',\
		'//*[@id="MasterBox"]/div[3]/div[2]/span[4]']
		for x in Phblist:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2)

		Phjhlist=['//*[@id="pxjh"]','//*[@id="MasterBox"]/div[2]/div[2]/span[1]','//*[@id="MasterBox"]/div[2]/div[2]/span[2]']
		for x in Phjhlist:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2)

		Key2=driver.find_element_by_id('txtSearch')
		Key2.clear()
		Key2.send_keys('123')
		Key2.send_keys(Keys.ENTER)

		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[2]/div[1]')
		report=ele.text
		if '培训计划' in report:
			print('培训计划检测成功！',file=opt.Write().test_report)
		else:
			print('培训计划检测失败！请检查系统！',file=opt.Write().test_report)

	def pxb(self):
		driver=self.driver
		# //*[@id="pxb"]
		Click=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[5]/a")
		ActionChains(driver).move_to_element(Click).perform()
		t.sleep(1)
		driver.find_element_by_xpath('//*[@id="dl_2"]/dd/a').click()
		t.sleep(2)
		px1=['//*[@id="MasterBox"]/div[3]/div[2]/span[1]','//*[@id="MasterBox"]/div[3]/div[2]/span[2]',\
		'//*[@id="MasterBox"]/div[3]/div[2]/span[3]','//*[@id="MasterBox"]/div[3]/div[2]/span[4]']
		for x in px1:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2)
		key1=driver.find_element_by_id("txtSearch")
		key1.clear()
		key1.send_keys('123')
		key1.send_keys(Keys.ENTER)
		t.sleep(2)

		px2=['//*[@id="pxjh"]','//*[@id="MasterBox"]/div[2]/div[2]/span[2]','//*[@id="MasterBox"]/div[2]/div[2]/span[1]']
		for x in px2:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2)
		key2=driver.find_element_by_xpath('//*[@id="txtSearch"]')
		key2.clear()
		key2.send_keys('456')
		key2.send_keys(Keys.ENTER)
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[2]/div[1]')
		report=ele.text
		if '培训计划' in report:
			print('培训班检测成功！',file=opt.Write().test_report)
		else:
			print('培训班检测失败！请检查系统！',file=opt.Write().test_report) 

		# 培训计划
		# Click=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[4]/a")
		# ActionChains(driver).move_to_element(Click).perform()
		# t.sleep(1)
		# driver.find_element_by_xpath("//*[@id='dl_2']/dd[2]/a").click()
		# t.sleep(2)
		# Pxjihua=['//*[@id="pxb"]','//*[@id="pxjh"]','//*[@id="MasterBox"]/div[3]/div[2]/span[1]',\
		# '//*[@id="MasterBox"]/div[3]/div[2]/span[2]','//*[@id="MasterBox"]/div[3]/div[2]/span[3]',\
		# '//*[@id="MasterBox"]/div[3]/div[2]/span[4]']
		# for x in Pxjihua:
		# 	Click=drivr.find_element_by_xpath(x)
		# 	Click.click()
		# 	t.sleep(2)
			
	# def ks(self):
	# 	driver=self.driver
	# 	move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[5]/a")
	# 	ActionChains(driver).move_to_element(move).perform()
	# 	t.sleep(1)
	# 	driver.find_element_by_xpath('//*[@id="dl_12"]/dd[1]/a').click()
	# 	t.sleep(2)
		
	# 	move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[5]/a")
	# 	ActionChains(driver).move_to_element(move).perform()
	# 	t.sleep(1)
	# 	driver.find_element_by_xpath('//*[@id="dl_12"]/dd[2]/a').click()
	# 	t.sleep(2)
		
	# 	move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[5]/a")
	# 	ActionChains(driver).move_to_element(move).perform()
	# 	t.sleep(1)
	# 	driver.find_element_by_xpath('//*[@id="dl_12"]/dd[3]/a').click()
	# 	t.sleep(2)
			
	def tzggao(self):
		driver=self.driver
		move=driver.find_element_by_xpath('//*[@id="div_new_menu"]/li[6]/a')
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_4"]/dd/a')
		Click.click()
		t.sleep(2)

		#//*[@id="Type_gsly"]///*[@id="MasterBox"]/div[1]/div[4]/span[1]
		Click=driver.find_element_by_xpath('//*[@id="Type_gsly"]')
		Click.click()
		t.sleep(1)

		Click=driver.find_element_by_xpath('//*[@id="Type_state"]')
		Click.click()
		t.sleep(1)
		list=['//*[@id="MasterBox"]/div[1]/div[4]/span[1]','//*[@id="MasterBox"]/div[1]/div[4]/span[2]']
		for x in list:
			Click=driver.find_element_by_xpath(x)	
			Click.click()
			t.sleep(2)

		Key=driver.find_element_by_xpath('//*[@id="txtSearch"]')
		Key.send_keys("123")
		Key.send_keys(Keys.ENTER)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[1]/div[2]')
		report=ele.text 
		if '通知公告类型' in report:
			print('通知公告检测成功！',file=opt.Write().test_report)
		else:
			print('通知公告检测失败！请检查系统！',file=opt.Write().test_report)

	def jfph(self):
		#//*[@id="MasterBox"]/div[1]/div[1]/input[5]
		driver=self.driver
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[7]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_5"]/dd[1]/a')
		Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[3]/div[1]')
		report=ele.text
		if '姓名' in report:
			print('积分排行检测成功！',file=opt.Write().test_report)
		else:
			print('积分排行检测失败！请检查系统!',file=opt.Write().test_report)

		Click=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[1]/div[1]/input[3]')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[1]/div[1]/input[4]')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[1]/div[1]/input[5]')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="btnScore"]')
		Click.click()
		t.sleep(1)
		
		"""
		jfqueue=['//*[@id="btnScore"]','//*[@id="MasterBox"]/div[1]/div[1]/input[3]'\
		'//*[@id="MasterBox"]/div[1]/div[1]/input[4]','//*[@id="MasterBox"]/div[1]/div[1]/input[5]']
		for x in jfqueue:
			Click=driver.find_element_by_xpath(x)
			Click.click()
		t.sleep(4)
		"""
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[7]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_5"]/dd[2]/a')
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[2]/div[1]')
		report=ele.text 
		if '当前积分' in report:
			print('我的积分检测成功！',file=opt.Write().test_report)
		else:
			print('我的积分检测失败！请检查系统！',file=opt.Write().test_report)
	
	def Jfmall(self):
		move=self.driver.find_element_by_xpath("//*[@id='div_new_menu']/li[8]/a")
		ActionChains(self.driver).move_to_element(move).perform()
		self.driver.find_element_by_xpath('//*[@id="dl_6"]/dd/a').click()
		t.sleep(2)
		#ActionChains(self.driver).move_to_element(move).perform()
		#ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
		#t.sleep(2)
		
	def Wenku(self):
		#//*[@id="dl_7"]/dd/a
		driver=self.driver
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[9]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_7"]/dd/a')
		Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="typeId"]')
		report=ele.text
		if '筛选类型' in report:
			print('文库中心检测成功！',file=opt.Write().test_report)
		else:
			print('文库中心检测失败,请检查系统！',file=opt.Write().test_report)

	def Gren(self):
		driver=self.driver
		#我的收藏
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[10]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_8"]/dd/a')
		Click.click()
		t.sleep(2)
		Click1=driver.find_element_by_xpath('//*[@id="collection"]')
		Click1.click()
		t.sleep(2)
		driver.find_element_by_xpath('//*[@id="MasterBox"]/div[3]').click()
		t.sleep(3)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[2]')
		report=ele.text
		if '课程' in report:
			print('我的收藏检测成功！',file=opt.Write().test_report)
		else:
			print('我的收藏检测失败,请检查系统！',file=opt.Write().test_report)

		#在线练习
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[10]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_8"]/dd/a')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="practice"]')
		Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="div_controller_fixed"]/div[3]')
		report=ele.text
		if '在线练习' in report:
			print('在线练习检测成功！',file=opt.Write().test_report)
		else:
			print('在线练习检测失败,请检查系统！',file=opt.Write().test_report)

		#我的错题库
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[10]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_8"]/dd/a')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="integral"]')
		Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="div_controller_fixed"]/div[3]')
		report=ele.text
		if '练习错题' in report:
			print('练习错题检测成功！',file=opt.Write().test_report)
		else:
			print('练习错题检测失败,请检查系统！',file=opt.Write().test_report)

		#模拟考试
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[10]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_8"]/dd/a')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="loding"]')
		Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[3]/div[1]')
		report=ele.text
		if '模拟考试' in report:
			print('模拟考试检测成功！',file=opt.Write().test_report)
		else:
			print('模拟考试检测失败,请检查系统！',file=opt.Write().test_report)

		#个人发展
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[10]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_8"]/dd/a')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="loding1"]')
		Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="div_controller_fixed"]/div[2]')
		report=ele.text
		if '个人中心' in report:
			print('个人发展检测成功！',file=opt.Write().test_report)
		else:
			print('个人发展检测失败,请检查系统！',file=opt.Write().test_report)

		#互动问答
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[10]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_8"]/dd/a')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="question"]')
		Click.click()
		t.sleep(2)
		lst=['//*[@id="MasterBox"]/div[4]/div[2]','//*[@id="MasterBox"]/div[4]/div[3]','//*[@id="MasterBox"]/div[4]/div[4]']
		for x in lst:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2)
		button=driver.find_element_by_id('txtSearch')
		button.clear()
		button.send_keys('789')
		button.send_keys(Keys.ENTER)
		t.sleep(2)
		btn=driver.find_element_by_xpath('//*[@id="add_question"]')
		btn.click()
		t.sleep(2)
		btn1=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[7]/div[1]/div[2]')
		btn1.click() 
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[5]/div[1]')
		report=ele.text
		if '综合排序' in report:
			print('互动问答检测成功！',file=opt.Write().test_report)
		else:
			print('互动问答检测失败,请检查系统！',file=opt.Write().test_report)

		#课程笔记//*[@id="loding3"]
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[10]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_8"]/dd/a')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="loding3"]')
		Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[2]/div[1]')
		report=ele.text
		if '笔记数量' in report:
			print('课程笔记检测成功！',file=opt.Write().test_report)
		else:
			print('课程笔记检测失败,请检查系统！',file=opt.Write().test_report)

		#学习记录//*[@id="loding4"]
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[10]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_8"]/dd/a')
		Click.click()
		t.sleep(2)
		Click=driver.find_element_by_xpath('//*[@id="loding4"]')
		Click.click()
		t.sleep(2)
		lst=['//*[@id="pxb"]','//*[@id="MasterBox"]/div[3]/div[2]/span[1]']
		for x in lst:
			btn3=driver.find_element_by_xpath(x)
			btn3.click()
			t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[3]/div[1]')
		report=ele.text
		if '您有学习' in report:
			print('学习记录检测成功！',file=opt.Write().test_report)
		else:
			print('学习记录检测失败,请检查系统！',file=opt.Write().test_report)

	def Wendan(self):
		driver=self.driver
		move=driver.find_element_by_xpath("//*[@id='div_new_menu']/li[11]/a")
		ActionChains(driver).move_to_element(move).perform()
		t.sleep(1)
		Click=driver.find_element_by_xpath('//*[@id="dl_9"]/dd/a')
		Click.click()
		t.sleep(2)
		ele=driver.find_element_by_xpath('//*[@id="MasterBox"]/div[4]/div/div[1]')
		report=ele.text 
		if '文件名' in report:
			print('文档中心检测成功！',file=opt.Write().test_report)
		else:
			print('文档中心检测失败，请检查系统！',file=opt.Write().test_report)
	
	def Htai(self):
		# driver=self.driver 
		#move=self.driver.find_element_by_xpath("//*[@id='div_new_menu']/li[12]/a")
		#ActionChains(self.driver).move_to_element(move).perform()
		Click=self.driver.find_element_by_xpath('//*[@id="div_new_menu"]/li[12]/a')
		Click.click()
		t.sleep(2)
		# ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
		# report=ele.text
		# if '所在的位置' in report:
		# 	print('后台管理跳转成功！')
		# else:
		# 	print('后台管理跳转失败，请检查系统！')
		
if __name__=="__main__":
	test1=GanyiChrome()	
	test1.setUp()
	print("初始化检测成功！检测中......")
	test1.test_clickButton()
	print("click检测成功！",file=opt.Write().test_report)
	test1.study_pass()
	print("学员端入口检测成功！",file=opt.Write().test_report)
	test1.firstpage()
	print("首页检测成功！",file=opt.Write().test_report)
	test1.qiyezs()
	print('-'*3,"企业知识检测完成！已输出报告！",'-'*3,file=opt.Write().test_report)
	test1.knowlg()
	print('-'*3,"知识子库检测成功！",'-'*3,file=opt.Write().test_report)
	test1.renwucents()
	print('-'*3,"任务中心检测成功！",'-'*3,file=opt.Write().test_report)
	test1.pxb()
	print("培训检测成功！",file=opt.Write().test_report)
	# test1.ks()
	# print("考试检测成功！",file=opt.Write().test_report)
	test1.tzggao()
	print("通知公告检测成功！",file=opt.Write().test_report)
	test1.jfph()
	print('-'*3,"积分排行检测完成，已输出报告！",'-'*3,file=opt.Write().test_report)
	# test1.Jfmall()
	# print("积分mall检测成功！")
	test1.Wenku()
	print('-'*3,"文库中心检测完成！已输出报告！",'-'*3,file=opt.Write().test_report)
	test1.Gren()
	print('*'*3,"个人中心检测完成，已输出报告！",'*'*3,file=opt.Write().test_report)
	test1.Wendan()
	print('-'*3,"文档中心检测完成！已输出报告！",'-'*3,file=opt.Write().test_report)
	test1.Htai()
	print("检测结束，报告已输出！")

	
	
		
		
		
		
		
		
	
