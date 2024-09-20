import base64
from saver import base64saver
# from result import waitscreen

def mybaseisu(sample_string):
 sample_string 
 sample_string_bytes = sample_string.encode("ascii")

 base64_bytes = base64.b64encode(sample_string_bytes)
 base64_string = base64_bytes.decode("ascii")
 base64saver(base64_string)
 print(f"Encoded string: {base64_string}")
#  waitscreen()
