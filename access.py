from threading import Thread

import code as c



c.create("janvi",22)
# to create a key with key_name,value given and with no time-to-live property


c.create("src", 70, 60)
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


c.read("janvi")

t1=Thread(target=(c.create or c.read or c.delete), args=(c.key_name, c.value, c.timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(c.create or c.read or c.delete),args=(c.key_name,c.value,c.timeout)) #as per the operation
t2.start()
t2.sleep()




