seconds = int(input("enter the seconds: "))
hour = seconds // 3600
seconds = seconds % 3600
minute = seconds // 60
seconds = seconds % 60
sec = "%d:%02d:%02d" % (hour,minute,seconds)
print(sec)