from selenium import webdriver
import requests
import time
import pickle

def main():
	chromePath=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'#chromedriver的路径
	wd = webdriver.Chrome(executable_path= chromePath)#构建浏览器
	url=r'https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2F'
	wd.get(url)
	iframe = wd.find_element_by_xpath('//*[@id="J_login_container"]/div/iframe')#切换到登陆模块
	wd.switch_to_frame(iframe)
	icon_pc = wd.find_element_by_xpath('/html/body/div/div[2]/div[5]/span')#选择账户登录
	icon_pc.click()
	time.sleep(2)
	name_login = wd.find_element_by_xpath('//*[@id="tab-account"]')#选择手机密码登录登录
	name_login.click()
	time.sleep(2)

	wd.find_element_by_id('account-textbox').send_keys('***********')#输入手机号
	wd.find_element_by_xpath('//input[@id="password-textbox"]').send_keys('*********')#输入密码
	wd.find_element_by_xpath('//button[@id="login-button-account"]').click()#点击登录

	cookies=wd.get_cookies()#cookies存储了登录后的cookie
	print(cookies)
	time.sleep(5)
	wd.quit()#退出浏览器

	with open('D:/cookie.ini','wb') as f:#使用pickle序列化存储cookie
		pickle.dump(cookies,f)

if __name__=='__main__':
	main()

