import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.google.com")
except urllib.error.URLError:
    print("Error connection.")
else:
    print("Connection OK.")
    
