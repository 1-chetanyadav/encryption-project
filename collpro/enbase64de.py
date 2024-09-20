import base64

from saver import base64saver

def mybaseisud(sample_string):
 sample_string 
 print(sample_string)

 base64_bytes=sample_string.encode("ascii")
 sample_string_bytes=base64.b64decode(base64_bytes)
 message64=sample_string_bytes.decode("ascii")
 print(message64)


#  sample_string_bytes = sample_string.encode("ascii")

#  base64_bytes = base64.b64encode(sample_string_bytes)
#  base64_string = base64_bytes.decode("ascii")
#  base64saver(base64_string)
#  print(f"Encoded string: {base64_string}")
#  print(f"Encoded string: {base64_string}")