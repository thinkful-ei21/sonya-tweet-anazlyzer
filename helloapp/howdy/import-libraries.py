import urllib.request

files = ["negative.txt", "positive.txt"]
path = "http://www.unc.edu/~ncaren/haphazard/"
for file_name in files:
    urllib.request.urlretrieve(path+file_name, file_name)
