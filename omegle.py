#!/usr/bin/python

from selenium import webdriver
import time
driver = webdriver.Chrome("/home/Shanks/Documents/Archives/chromedriver")
try:
	driver.get("http://www.omegle.com");
	driver.find_element_by_id("textbtn").click()
	time.sleep(5)
	for i in range(0,25):
	    time.sleep(3)
	    disconnectbtn=driver.find_element_by_class_name("disconnectbtn")
	    chatmsg=driver.find_element_by_class_name("chatmsg")
	    sendbtn=driver.find_element_by_class_name("sendbtn")
	    chatmsg.send_keys("indian f?")
	    sendbtn.click()
	    time.sleep(8)
	    disconnectbtn.click()
	    disconnectbtn=driver.find_element_by_class_name("disconnectbtn")
	    disconnectbtn.click()
	    disconnectbtn=driver.find_element_by_class_name("disconnectbtn")
	    disconnectbtn.click()
except:
	driver.close()
	raise
