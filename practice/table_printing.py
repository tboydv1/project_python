#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 23:31:13 2019

@author: tboydev
"""
from time import ctime as current_time

HELP_COMMAND = ['help', 'h']

QUIT_COMMANDS = ['q', 'quit']

##Program state
IS_RUNNING  = True

SHOW_COMMAND = 'showlogs'

CUSTOMER_NAME = PRODUCT_NAME =  TIME_OF_PURCHASE = ''

QTY = PRICE = TOTAL_COST = 0.00

def trim(var):
	return var.strip()

def getInput():
	global IS_RUNNING
	try:
		##this is the input to prompt the user 
		prompt = 'Type Info here: '

		##collect info from user and assigns to respective variables
		info = input(prompt)

		if info.lower() in HELP_COMMAND:
			displayHelpMessage()
			return False, None

		if info.lower() in QUIT_COMMANDS:
			IS_RUNNING = False
			return True, None

		info = info.split(',')

		if len(info) != 4:
			displayErrorMessage()
			return False, None

		if info.lower() == SHOW_COMMAND:
			show_log()
			return False, None

		return True, info

	except Exception as e:
		displayErrorMessage()
		return False, None


		

def getUserInput():
	status = False
	while status == False:
		status, info = getInput()
	return info

def main():
	#shows how to use program
	displayHelpMessage()

	while IS_RUNNING:
		#COLLECTS the neccessary 
		info = getUserInput()


		if IS_RUNNING == False:
			print("Program is shutting down...")
			print('Program Shut down Successfully!')

		##trim var spaces
		CUSTOMER_NAME, PRODUCT_NAME, QTY, PRICE = list(map(trim, info))


		##cast to number
		PRICE = float(PRICE)
		QTY = float(QTY)

		##total cost of purchase is 
		TOTAL_COST = PRICE * QTY

		##time of purchase
		TIME_OF_PURCHASE = current_time()



def displayHelpMessage():
	print('Here are the working commands')
	print('-----------------------------')
	print('showLogs: to see all registered information')
	print('Help: to see the help message')
	print('Customer Name, Product, Quantity, PRICE: seperated by comma to register information')

def displayErrorMessage(d):
    print('Invalid Input!!!\n')



def showLogs():
	print("{:<5}{:<17}{:<15}{:<10}{:<12}{:<15}{:<10}".format("s/n","Customer Name","Product Name",\
	      "PRICE", "Quantity", "Total Cost", "Time"))
	print("{:<5}{:<17}{:<15}{:<10.2f}{:<12}{:<15.2f}{:<10}".format(1, CUSTOMER_NAME.capitalize(),\
	      PRODUCT_NAME.capitalize(), PRICE, quantity,PRICE * quantity, "10:23:48"))

if __name__ == '__main__':
	main()







