import Algorithmia
#import urllib, cStringIO
from PIL import Image
import base64
from jewellery.dominant_color_copy import *

#provide image path as an input 
def detect(filename,image):
	print (filename)
	#img = Image.open(filename)
	#img.show()

#provide image path as an input 
#convert it into base 64 
	#buffer = StringIO.StringIO()
	#buffer.write(_content)
	#file_data = buffer.getvalue()
	#print (file_data)
	
	#image = base64.b64encode( open( filename.url, "rb").read())
	input = {"image": 'data:image/jpg;base64,' + image.decode('ascii')}

	client = Algorithmia.client('simb+HoZt1y2rsh4qvaHZ4pGbdy1')
	algo = client.algo('algorithmiahq/DeepFashion/1.2.2')

#here c contains type of dress and its boundind box in a list of dictionaries
	c=(algo.pipe(input).result)
#print c

	b= c['articles']
	print (b)
	a,percentage=colorz(filename,b)
	

		
	#break;
	return a,percentage

#detect('/Users/rashmisahu/Desktop/rashmi/internship/3.jpg')