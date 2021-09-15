import Hikvision
import datetime
import time
while True:
   f = open('out.log', 'r')
   line=f.read()
   f.close()
   print ('line',line)
   print(Hikvision.StartDateTime )
   print('a',Hikvision.UserName,Hikvision.IpAddress)
   time.sleep(5)
