# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:05:23 2016

@author: ceciliaLee
methodology for parsing websites typically goes by viewing the page itself,
finding the value I want, copying that value to clipboard, viewing the page 
source, searching for that value, and just seeing how the page is typically 
structured around those data points.
"""
import os ## interact with director ies
import time
from datetime import datetime

path ='/Users/ceciliaLee/Desktop/MachineLearningAlgorithm/SKlearn_py/intraQuarter'


## collect the Debt/Equity value.
def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)] # os.walk to list out all contents within a directory
    #print(stock_list)
    # cycling through every directory 
    for each_dir in stock_list[1:]: 
        each_file = os.listdir(each_dir) # each file within that stock's directory
        # each_fir output example: '.../intraQuarter/_KeyStats/znga'
        ticker = each_dir.split("/")[1]  #stores the current ticker being assessed     
        # ticker output: User
        
        if len(each_file) > 0:
            for file in each_file:
                #  pulls the date_stamp from each file.
                date_stamp=datetime.strptime(file,'%Y%m%d%H%M%S.html') # 格式化日期时间：由字符串转为日期型
                unix_time = time.mktime(date_stamp.timetuple()) #time.mktime()接收struct_time对象作为参数，返回用秒数来表示时间的浮点数。
   #             print 'date_stamp: ',date_stamp
    #            print 
    #            print 'unix_time: ',unix_time
                #time.sleep(15)
                
                full_file_path = each_dir+'/'+file
          #      print 'full_file_path: ' ,full_file_path
                # example output of dull_file_path:
                #full_file_path:  /Users/ceciliaLee/Desktop/MachineLearningAlgorithm/SKlearn_py/intraQuarter/_KeyStats/znga/20130510054327.html
               
                #access the file, and save the full source code HTML contents to the "source" variable. 
                source = open(full_file_path,'r').read()
         #       print 'source: ',source
                #split by the opening of the table data tag and the table data closing tag to find the value we're hunting fo
                value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                print ticker+":",value 
            time.sleep(15)
Key_Stats()