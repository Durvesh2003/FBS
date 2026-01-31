# 1. Convert the time entered in hh,min and sec into seconds.
hh = int(input("Enter the number of hours : "))
min = int(input("Enter the time taken minutes : "))
sec = int(input("Enter the time in secods : "))

total_Time_in_seconds = hh * 3600 + min * 60 + sec

print("Total Time taken in seconds : ",total_Time_in_seconds)
