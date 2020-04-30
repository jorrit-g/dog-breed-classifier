def format_time(time_val):
    return str(int((time_val/3600)))+":"+str(int((time_val%3600)/60))+ ":" +str(int((time_val%3600)%60))

def format_time_millis(time_val):
    return "{:02d}:{:02d}:{:06.3f}".format(int((time_val/3600)), int((time_val%3600)/60), time_val)