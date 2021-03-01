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
import file_report as opt

class Gybackstage():
	#启动浏览器
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()

	def Clickload(self):
		self.driver.get('http://192.168.253.57')
		t.sleep(3)
		self.driver.get('http://192.168.253.57/Login_QY.aspx?orgprex=www&qynx=0')
		btn1=self.driver.find_element_by_xpath('//*[@id="txt_user"]')
		btn2=self.driver.find_element_by_xpath('//*[@id="txt_pwd"]')
		btn1.clear()
		btn1.send_keys('admin')
		btn1.send_keys(Keys.TAB)
		t.sleep(2)
		btn2.clear()
		btn2.send_keys('123456')
		btn2.send_keys(Keys.ENTER)
		t.sleep(2)
		ele=self.driver.find_element_by_xpath('//*[@id="div_new_top"]/div[1]')
		report=ele.text
		if '首钢长治钢铁有限公司' in report:
			print("登录成功！",file=opt.Write().test_report)
		else:
			print("登录失败,请重新登录！",file=opt.Write().test_report)

		#组织管理
	def Organize(self):
		# lst0=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[1]/div[3]','//*[@id="div_new_menu_2"]/div[1]/div[2]']
		# lst1=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[1]/div[3]','//*[@id="div_new_menu_2"]/div[2]/div[2]']
		# lst2=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[1]/div[3]','//*[@id="div_new_menu_2"]/div[3]/div[2]']
		# lst3=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[1]/div[3]','//*[@id="div_new_menu_2"]/div[4]/div[2]']
		# lst4=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[1]/div[3]','//*[@id="div_new_menu_2"]/div[5]/div[2]']	
		lst0=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[1]/div[3]']
		lst1=['//*[@id="div_new_menu_2"]/div[1]/div[2]','//*[@id="div_new_menu_2"]/div[2]/div[2]','//*[@id="div_new_menu_2"]/div[3]/div[2]',\
		'//*[@id="div_new_menu_2"]/div[4]/div[2]','//*[@id="div_new_menu_2"]/div[5]/div[2]']
		lst2=['//*[@id="treeDemo_2_switch"]','//*[@id="treeDemo_3_switch"]','//*[@id="treeDemo_5_span"]']
		lst3=['//*[@id="treeDemo_2_switch"]','//*[@id="treeDemo_3_switch"]','//*[@id="treeDemo_3_ul"]']
		lst4=['//*[@id="div_contents"]/div[5]/div[5]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div','//*[@id="div_contents"]/div[5]/div[5]/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div',\
		'//*[@id="div_contents"]/div[5]/div[5]/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[1]/div']
		y=0
		while y<5:
			for x in lst0:
				Click=self.driver.find_element_by_xpath(x)
				Click.click()
				t.sleep(2.0)
			btn=self.driver.find_element_by_xpath(lst1[y])
			btn.click()
			if y==0:
				for x in lst2:
					self.driver.find_element_by_xpath(x).click()
					t.sleep(2.0)
				ele=self.driver.find_element_by_xpath('//*[@id="treeDemo_1_span"]')
				report=ele.text
				if '组织架构' in report:
					print('部门管理检测成功！',file=opt.Write().test_report)
				else:
					print('部门管理检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==1:
				for x in lst4:
					self.driver.find_element_by_xpath(x).click()
					t.sleep(2.0)
				ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '角色管理' in report:
					print('角色管理检测成功！',file=opt.Write().test_report)
				else:
					print('角色管理检测失败,请检查系统！',file=opt.Write().test_report)

			elif y==2:
				for x in lst3:
					self.driver.find_element_by_xpath(x).click()
					t.sleep(2.0)
				ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '岗位管理' in report:
					print('岗位管理检测成功！',file=opt.Write().test_report)
				else:
					print('岗位管理检测失败,请检查系统！',file=opt.Write().test_report)

			elif y==3:
				btn=self.driver.find_element_by_xpath('//*[@id="txtSearch"]')
				btn.clear()
				btn.send_keys('123')
				btn.send_keys(Keys.ENTER)
				t.sleep(2.0)
				ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '专家管理' in report:
					print('专家管理检测成功！',file=opt.Write().test_report)
				else:
					print('专家管理检测失败,请检查系统',file=opt.Write().test_report)

			else :
				btn=self.driver.find_element_by_xpath('//*[@id="txtSearch"]')
				btn.clear()
				btn.send_keys('123')
				btn.send_keys(Keys.ENTER)
				t.sleep(2.0)
				ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '讲师管理' in report:
					print('讲师管理检测成功！',file=opt.Write().test_report)
				else:
					print('讲师管理检测失败,请检查系统！',file=opt.Write().test_report)
				self.driver.find_element_by_xpath('//*[@id="div_btn_fh"]').click()
				t.sleep(1)	
			y+=1
			if y>5:
				print("ERROR!",file=opt.Write().test_report)
				break

		#培训管理
	def Train(self):
		driver=self.driver
		# lst0=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[2]/div[3]','//*[@id="div_new_menu_2"]/div[1]/div[2]']
		# lst1=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[2]/div[3]','//*[@id="div_new_menu_2"]/div[2]/div[2]']
		# lst2=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[2]/div[3]','//*[@id="div_new_menu_2"]/div[3]/div[2]']
		# lst3=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[2]/div[3]','//*[@id="div_new_menu_2"]/div[4]/div[2]']
		# lst4=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[2]/div[3]','//*[@id="div_new_menu_2"]/div[5]/div[2]']	
		lst0=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[2]/div[3]']
		lst1=['//*[@id="div_new_menu_2"]/div[1]/div[2]','//*[@id="div_new_menu_2"]/div[2]/div[2]','//*[@id="div_new_menu_2"]/div[3]/div[2]',\
		'//*[@id="div_new_menu_2"]/div[4]/div[2]','//*[@id="div_new_menu_2"]/div[5]/div[2]']
		lst2=['//*[@id="treeDemo_2"]','//*[@id="treeDemo_63_switch"]','//*[@id="treeDemo_135_switch"]',\
		'//*[@id="treeDemo_236_switch"]','//*[@id="treeDemo_343_switch"]','//*[@id="treeDemo_428_switch"]','//*[@id="treeDemo_458_switch"]',\
		'//*[@id="treeDemo_614_switch"]']
		lst3=['//*[@id="btn_btn_add"]','//*[@id="div_step_1_show"]/div/div[2]']
		lst4=['//*[@id="div_btn_MustInfo"]','//*[@id="div_btn_task"]','//*[@id="div_btn_examine_approve"]','//*[@id="div_btn_statistical"]']
		lst5=['//*[@id="div_main"]/div[1]/div[1]/div[1]','//*[@id="div_main"]/div[1]/div[1]/div[2]','//*[@id="div_main"]/div[1]/div[1]/div[3]',\
		'//*[@id="div_main"]/div[1]/div[1]/div[4]']
		lst6=['//*[@id="div_main_top_controler"]/div[1]/span[2]','//*[@id="div_main_top_controler"]/div[1]/span[3]']
		lst7=['//*[@id="div_main_top_controler"]/div[2]/span[2]','//*[@id="div_main_top_controler"]/div[2]/span[3]']
		y=0
		while y < 5:
			for x in lst0:
				Click=driver.find_element_by_xpath(x)
				Click.click()
				t.sleep(2.0)
			btn=driver.find_element_by_xpath(lst1[y])
			btn.click()
			t.sleep(2.0)
			if y==0:
				for x in lst2:
					driver.find_element_by_xpath(x).click()
					t.sleep(2.0)
				ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '课程管理' in report:
					print("课程管理检测成功！",file=opt.Write().test_report)
				else:
					print("课程管理检测失败,请检查系统！",file=opt.Write().test_report)

			elif y==1:
				for x in lst3:
					driver.find_element_by_xpath(x).click()
					t.sleep(2.0)
				ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '培训计划' in report:
					print("培训计划检测成功！",file=opt.Write().test_report)
				else:
					print("培训计划检测失败,请检查系统！",file=opt.Write().test_report)

			elif y==2:
				try:
					driver.find_element_by_xpath('//*[@id="div_btn_MustInfo"]').click()
					t.sleep(2)
				except:
					print('error！存在异常！',file=opt.Write().test_report)
				else:
					driver.back()
				list=['//*[@id="div_btn_task"]','//*[@id="div_btn_back"]','//*[@id="div_btn_examine_approve"]',\
				'//*[@id="div_btn_return"]','//*[@id="div_btn_statistical"]','//*[@id="div_btn_fh"]']
				k=0
				for x in list:
					driver.find_element_by_xpath(x).click()
					t.sleep(2)

				ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '培训班' in report:
					print("培训班检测成功！",file=opt.Write().test_report)
				else:
					print("培训班检测失败！请检查系统！",file=opt.Write().test_report)
				# try:
				# 	list=['//*[@id="div_btn_task"]','//*[@id="div_btn_back"]','//*[@id="div_btn_examine_approve"]',\
				# 	'//*[@id="div_btn_return"]','//*[@id="div_btn_statistical"]','//*[@id="div_btn_fh"]',\
				# 	'//*[@id="div_btn_MustInfo"]']
				# 	k=0
				# 	for x in list:
				# 		driver.find_element_by_xpath(x).click()
				# 		t.sleep(2)
				# 		k +=1
				# except:
				# 	driver.back()
				# 	print('异常！位置在:',list[k])
				# else:
				# 	pass
			elif y==3:
				for x in lst7:
					driver.find_element_by_xpath(x).click()
					t.sleep(1.0)
					for i in lst6:
						driver.find_element_by_xpath(i).click()
						t.sleep(1.0)
				ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '培训监控' in report:
					print('培训监控检测成功！',file=opt.Write().test_report)
				else:
					print("培训监控检测失败，请检查系统！",file=opt.Write().test_report)

			elif y==4:
				for x in lst5:
					driver.find_element_by_xpath(x).click()
					t.sleep(2.0)
				ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '培训评估' in report:
					print("培训评估检测成功！",file=opt.Write().test_report)
				else:
					print("培训评估检测失败，请检查系统！",file=opt.Write().test_report)
			y+=1
			if y > 5 :
				print("ERROR!",file=opt.Write().test_report)
				break

		#考试管理
	def Ks(self):
		driver=self.driver
		lst0=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[3]/div[3]']
		lst1=['//*[@id="div_new_menu_2"]/div[1]/div[2]','//*[@id="div_new_menu_2"]/div[2]/div[2]',\
		'//*[@id="div_new_menu_2"]/div[3]/div[2]','//*[@id="div_new_menu_2"]/div[4]/div[2]']
		lst2=['//*[@id="treeDemo_2_switch"]','//*[@id="treeDemo_3_switch"]','//*[@id="treeDemo_4_span"]']
		lst3=['//*[@id="treeDemo_63_switch"]','//*[@id="treeDemo_135_switch"]','//*[@id="treeDemo_236_switch"]',\
		'//*[@id="treeDemo_299_switch"]','//*[@id="treeDemo_343_switch"]','//*[@id="treeDemo_428_switch"]','//*[@id="treeDemo_458_switch"]',\
		'//*[@id="treeDemo_458_switch"]','//*[@id="treeDemo_537_switch"]','//*[@id="treeDemo_614_switch"]']
		y=0
		while y < 4:
			for x in lst0:
				Click=driver.find_element_by_xpath(x)
				Click.click()
				t.sleep(2.0)
			btn=driver.find_element_by_xpath(lst1[y])
			btn.click()
			t.sleep(2.0)
			if y==0:
				for x in lst2:
					driver.find_element_by_xpath(x).click()
					t.sleep(2.0)
				for x in lst3:
					aaa=driver.find_element_by_xpath(x)
					ActionChains(driver).click(aaa).perform()
					t.sleep(2.0)
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '题库管理' in report:
					print("题库管理检测成功！",file=opt.Write().test_report)
				else:
					print("题库管理检测失败,请检查系统！",file=opt.Write().test_report)
			elif y==1:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '试卷管理' in report:
					print("试卷管理检测成功！",file=opt.Write().test_report)
				else:
					print('试卷管理检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==2:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '考试安排' in report:
					print("考试安排检测成功！",file=opt.Write().test_report)
				else:
					print('考试安排检测失败,请检查系统！',file=opt.Write().test_report)
			else :
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '考试管理' in report:
					print("考试管理检测成功！",file=opt.Write().test_report)
				else:
					print('考试管理检测失败,请检查系统！',file=opt.Write().test_report)	
			y+=1
			if y > 4 :
				print('ERROR!',file=opt.Write().test_report)
				break
		
		#文库管理
	def Article(self):
		lst1=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[4]/div[3]','//*[@id="div_new_menu_2"]/div[1]/div[2]']
		lst2=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[4]/div[3]','//*[@id="div_new_menu_2"]/div[2]/div[2]']
		for x in lst1:
			button=self.driver.find_element_by_xpath(x)
			button.click()
			t.sleep(2)	
		ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
		report=ele.text
		if '文库分类' in report:
			print("文库分类检测成功！",file=opt.Write().test_report)
		else:
			print('文库分类检测失败,请检查系统！',file=opt.Write().test_report)
		for x in lst2:
			button=self.driver.find_element_by_xpath(x)
			button.click()
			t.sleep(2)
		ele=self.driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
		report=ele.text
		if '文库审核' in report:
			print("文库审核检测成功！",file=opt.Write().test_report)
		else:
			print('文库审核检测失败,请检查系统！',file=opt.Write().test_report)

		#互动管理
	def Each_other(self):
		driver=self.driver
		lst0=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[5]/div[3]']
		lst1=['//*[@id="div_new_menu_2"]/div[1]/div[2]','//*[@id="div_new_menu_2"]/div[2]/div[2]','//*[@id="div_new_menu_2"]/div[3]/div[2]']
		#lst2=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[5]/div[3]','//*[@id="div_new_menu_2"]/div[3]/div[2]']
		y=0
		while y < 3:
			for x in lst0:
				Click=driver.find_element_by_xpath(x)
				Click.click()
				t.sleep(2.0)
			btn=driver.find_element_by_xpath(lst1[y])
			btn.click()
			t.sleep(2.0)
			ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
			report=ele.text
			if y==0 :
				if '提问审核' in report:
					print("提问审核检测成功！",file=opt.Write().test_report)
				else:
					print("提问审核检测失败,请检查系统!",file=opt.Write().test_report)
			elif y==1:
				if '回答审核' in report:
					print('回答审核检测成功！',file=opt.Write().test_report)
				else:
					print("回答审核检测失败,请检查系统！",file=opt.Write().test_report)
			else :
				if "提问标签" in report: 
					print('提问标签检测成功！',file=opt.Write().test_report)
				else:
					print("提问标签检测失败,请检查系统！",file=opt.Write().test_report)	
			t.sleep(2.0)
			y+=1

		#运营管理//*[@id="div_new_menu_2"]/div[12]/div[2]
	def Operation(self):
		driver=self.driver
		lst0=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[6]/div[3]']
		lst1=['//*[@id="div_new_menu_2"]/div[1]/div[2]','//*[@id="div_new_menu_2"]/div[2]/div[2]','//*[@id="div_new_menu_2"]/div[3]/div[2]',\
		'//*[@id="div_new_menu_2"]/div[4]/div[2]','//*[@id="div_new_menu_2"]/div[5]/div[2]','//*[@id="div_new_menu_2"]/div[6]/div[2]',\
		'//*[@id="div_new_menu_2"]/div[7]/div[2]','//*[@id="div_new_menu_2"]/div[8]/div[2]','//*[@id="div_new_menu_2"]/div[9]/div[2]',\
		'//*[@id="div_new_menu_2"]/div[10]/div[2]','//*[@id="div_new_menu_2"]/div[11]/div[2]','//*[@id="div_new_menu_2"]/div[12]/div[2]']
		lst2=['//*[@id="layui-laypage-1"]/a[1]','//*[@id="layui-laypage-1"]/a[2]','//*[@id="layui-laypage-1"]/a[3]',\
		'//*[@id="layui-laypage-1"]/a[4]','//*[@id="layui-laypage-1"]/a[5]']
		lst3=['//*[@id="div_contents"]/div[5]/div[4]/div/div[3]/div/div','//*[@id="div_contents"]/div[5]/div[4]/div/div[3]/div/dl/dd']
		y=0
		while y < 12:
			for x in lst0:
				Click=driver.find_element_by_xpath(x)
				Click.click()
				t.sleep(2.0)
			btn=driver.find_element_by_xpath(lst1[y])
			btn.click()
			t.sleep(2.0)
			if y==0:
				for x in lst2:
					Click=driver.find_element_by_xpath(x)
					Click.click()
					t.sleep(2.0)
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '账户管理' in report:
					print('账户管理检测成功！',file=opt.Write().test_report)
				else:
					print('账户管理检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==1:
				for x in lst3:
					Click=driver.find_element_by_xpath(x)
					Click.click()
					t.sleep(2)
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '公告管理' in report:
					print('公告管理检测成功！',file=opt.Write().test_report)
				else:
					print('公告管理检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==2:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if 'Banner' in report:
					print('Banner检测成功！',file=opt.Write().test_report)
				else:
					print('Banner检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==3:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if 'LOGO' in report:
					print('LOGO检测成功！',file=opt.Write().test_report)
				else:
					print('LOGO检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==4:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '积分管理' in report:
					print('积分管理检测成功！',file=opt.Write().test_report)
				else:
					print('积分管理检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==5:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '开关管理' in report:
					print('开关管理检测成功！',file=opt.Write().test_report)
				else:
					print('开关管理检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==6:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '首页定制' in report:
					print('首页定制检测成功！',file=opt.Write().test_report)
				else:
					print('首页定制检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==7:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '登入背景' in report:
					print('登入背景检测成功！',file=opt.Write().test_report)
				else:
					print('登入背景检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==8:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '邮件设置' in report:
					print('邮件设置检测成功！',file=opt.Write().test_report)
				else:
					print('邮件设置检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==9:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '分类管理' in report:
					print('分类管理检测成功！',file=opt.Write().test_report)
				else:
					print('分类管理检测失败,请检查系统！',file=opt.Write().test_report)
			elif y==10:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '意见箱' in report:
					print('意见箱检测成功！',file=opt.Write().test_report)
				else:
					print('意见箱检测失败,请检查系统！',file=opt.Write().test_report)
			else:
				ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
				report=ele.text
				if '证书管理' in report:
					print('证书管理检测成功！',file=opt.Write().test_report)
				else:
					print('证书管理检测失败,请检查系统！',file=opt.Write().test_report)
			y+=1 
			if y > 12:
				print("ERROR!",file=opt.Write().test_report)
				break

		#统计分析
	def count(self):
		driver=self.driver
		Zy_lst=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[7]/div[3]','//*[@id="div_new_menu_2"]/div[1]/div[2]']
		Look_lst=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[7]/div[3]','//*[@id="div_new_menu_2"]/div[2]/div[2]']
		Data_lst=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[7]/div[3]','//*[@id="div_new_menu_2"]/div[3]/div[2]']
		# for x in Zy_lst:
		# 	Click=driver.find_element_by_xpath(x)
		# 	Click.click()
		# t.sleep(50)	
		# ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')  
		# report=ele.text
		# if '资源概况' in report:
		# 	print('资源概况检测成功！')
		# else:
		# 	print('资源概况检测失败！请检查系统！')
		# t.sleep(30)
		for x in Look_lst:
			Click=driver.find_element_by_xpath(x)
			Click.click()
		t.sleep(2.0)
		ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
		report=ele.text
		if "统计看板" in report:
			print('统计看板检测成功！',file=opt.Write().test_report)
		else:
			print('统计看板检测失败！请检查系统！',file=opt.Write().test)
		t.sleep(2.0)
		for x in Data_lst:
			Click=driver.find_element_by_xpath(x)
			Click.click()
		t.sleep(2.0)
		ele=driver.find_element_by_xpath('//*[@id="div_new_menu_content_right"]')
		report=ele.text
		if '统计数据' in report:
			print("统计数据检测成功！",file=opt.Write().test_report)
		else:
			print("统计数据检测失败！请检查系统！",file=opt.Write().test_report)

		#知识竞赛
	def knowledge(self):
		driver=self.driver
		list=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[8]/div[3]','//*[@id="div_new_menu_2"]/div/div[2]']
		for x in list:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2.0)
		driver.back()
		#fc.switch_to_window(fc.window_handles[1])
		# sreach_window=driver.current_window_handle
		# driver.find_element_by_xpath('/html/body/div/div[2]/div/ul/li[1]/a/text()').click()

	def jfmall(self):
		driver=self.driver
		#print('当前浏览地址为：.{0}'.format(driver.current_url))
		lst0=['//*[@id="div_new_menu"]','//*[@id="div_new_menu"]/div[9]/div[3]','//*[@id="div_new_menu_2"]/div/div[2]']
		for x in lst0:
			Click=driver.find_element_by_xpath(x)
			Click.click()
			t.sleep(2.0)
		#print('当前浏览地址为：.{0}'.format(driver.current_url))
		#driver.switch_to.window(driver.current_url)
		#driver.get(driver.current_url)
		driver.back() 
		#driver.find_element_by_xpath('//*[@id="ss1"]').click()
		# ele=driver.find_element_by_xpath('//*[@id="nopng"]/span')
		# report=ele.text
		# if '积分商城' in report:
		# 	print("积分商城检测成功！")
		# else:
		# 	print("积分商城检测失败！请检查系统！")
		# lst1=[['//*[@id="frm_menu"]/frame[2]','/html/body/span','//*[@id="ss1"]','//*[@id="bs1"]/ul/li[1]/a','//*[@id="bs1"]/ul/li[2]/a'],\
		# ['//*[@id="ss88"]','//*[@id="bs88"]/ul/li[1]/a','//*[@id="bs88"]/ul/li[2]/a','//*[@id="bs88"]/ul/li[3]/a',\
		# '//*[@id="bs88"]/ul/li[4]/a','//*[@id="bs88"]/ul/li[4]/a'],\
		# ['//*[@id="ss108"]','//*[@id="bs108"]/ul/li[1]/a','//*[@id="bs108"]/ul/li[2]/a','//*[@id="bs108"]/ul/li[3]/a',\
		# '//*[@id="bs108"]/ul/li[4]/a','//*[@id="bs108"]/ul/li[5]/a','//*[@id="bs108"]/ul/li[6]/a']]
		# for y in lst1[0]:
		# 	Click=driver.find_element_by_xpath(y)
		# 	Click.click()
		# 	t.sleep(2.0)
		# for z in lst1[1]:
		# 	Click=driver.find_element_by_xpath(z)
		# 	Click.click()
		# 	t.sleep(2.0)
		# for k in lst1[2]:
		# 	Click=driver.find_element_by_xpath(k)
		# 	Click.click()
		# 	t.sleep(2.0)

if __name__ == "__main__":
	ts=Gybackstage()
	ts.setUp()
	print("浏览器启动成功！，开始检测......")
	ts.Clickload()
	ts.Organize()
	print('-'*3,"组织管理检测完毕，已输出报告！",'-'*3)
	print('-'*3,'组织管理检测完毕，已输出报告！','-'*3,file=opt.Write().test_report)
	ts.Train()
	print('-'*3,'培训管理检测完毕，已输出报告！','-'*3)
	print('-'*3,'培训管理检测完毕，已输出报告！','-'*3,file=opt.Write().test_report)
	ts.Ks()
	print('-'*3,"考试管理检测完毕，已输出报告！",'-'*3)
	print('-'*3,'考试管理检测完毕，已输出报告！','-'*3,file=opt.Write().test_report)
	ts.Article()
	print('-'*3,"文库管理检测完毕，已输出报告！",'-'*3)
	print('-'*3,'文库管理检测完毕，已输出报告！','-'*3,file=opt.Write().test_report)
	ts.Each_other()
	print('-'*3,"互动管理检测完毕，已输出报告！",'-'*3)
	print('-'*3,'互动管理检测完毕，已输出报告！','-'*3,file=opt.Write().test_report)
	ts.Operation()
	print('-'*3,'运营管理检测完毕，已输出报告！','-'*3)
	print('-'*3,'运营管理检测完毕，已输出报告！','-'*3,file=opt.Write().test_report)
	ts.count()
	print('-'*3,"统计分析检测完毕，已输出报告！",'-'*3)
	print('-'*3,'统计分析检测完毕，已输出报告！','-'*3,file=opt.Write().test_report)
	# ts.knowledge()
	# print('知识竞赛检测...')
	ts.jfmall()
	print("积分商城检测...")
	print('系统检测结束，已输出检测报告...')



