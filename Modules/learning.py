# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:25:30 2020

@author: 15025

studying program
"""

import os
import time


class AccompanyStudy:
    """
    This program is aiming at supervising myself
    """
    def __init__(self): 
        print("Please choose the corresponding serial number: ")
        print("1. study for 45 minutes.")
        print("2. study for 50 minutes.")
        print("3. study for 10 minutes.")
        print("4. study for 20 minutes.")
        # selection set
        # self.selection_set = ["1", "2", "3", "4"]
        # choose total time of learning
        self.selection = input("Please choose learning time: ")
        # 1 for 45 minutes
        # 2 for 50 minutes
        # 3 for 10 minutes
        # 4 for 20 minutes
        
        if self.selection == "1":
            self.time = 45 * 60
        elif self.selection == "2":
            self.time = 50 * 60
        elif self.selection == "3":
            self.time = 10 * 60
        elif self.selection == "4":
            self.time = 20 * 60
        else:
            print("The input value is not correct, Please input a new value again!")
        
        # after choosing studying time, we recored the time point of starting studying
        self.start_time = time.time()
        
        # txt file for saving data
        if not os.path.exists("C:/Users/15025/Desktop/data.txt"):
            # the value of inteligence +1 after studying successfilly
            self.inteligence = 0
        else:
            with open("C:/Users/15025/Desktop/data.txt", 'r') as f:
                data_list = f.readlines()
                new_data_list = []
                for data in data_list:
                    new_data_list.append(int(data.rstrip()))
                self.inteligence = new_data_list[0]
        
    def mainSystem(self):  
        self.startLearning()
        self.displayData()
        self.saveData()
    
    # start learning progress
    def startLearning(self):
        while round(time.time() - self.start_time) != self.time:
            pass
        
        self.updateData()
    
    # update data
    def updateData(self):
        self.inteligence += 1
    
    # display data in program
    def displayData(self):
        print('-'*18+'Current Data ' + '-' * 18)
        print('Inteligence:'.ljust(20)+ '{0}' + '|'.format(self.inteligence).rjust(28))

    # save data
    def saveData(self):
        with open("C:/Users/15025/Desktop/data.txt", "w+") as f:
            f.write(str(self.inteligence) + '\n')
            

if __name__ == "__main__":
    main = AccompanyStudy()
    main.mainSystem()