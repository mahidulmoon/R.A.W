from datetime import datetime
from time import mktime


# coredata_timestamp = 651572654
coredata_timestamp = int(input("Insert Apple Cocoa Core Data timestamp:  "))

coredata_start_date = datetime(2001, 1, 1, 0, 0, 0, 0, tzinfo=None)

coredata_start_unix = int(mktime(coredata_start_date.timetuple()))

unix_timestamp = coredata_start_unix + coredata_timestamp

#print(unix_timestamp) #unix timestamp

ts = unix_timestamp

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case

final_result = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#print(final_result) 

x = datetime(int(final_result[0:4]), int(final_result[5:7]), int(final_result[8:10]),int(final_result[11:13]),int(final_result[14:16]),int(final_result[17:]))
print("Human-readable date: ",x.strftime("%b %d %Y %H:%M:%S"))