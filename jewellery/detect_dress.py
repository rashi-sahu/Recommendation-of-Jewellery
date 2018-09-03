import Algorithmia
import urllib, cStringIO
from PIL import Image

#getting an image from image url
file = cStringIO.StringIO(urllib.urlopen("http://i67.tinypic.com/mkvhiq.jpg").read())
img = Image.open(file)

#img.show()

#give image url as an input to client
input = {"image": "http://i67.tinypic.com/mkvhiq.jpg"}

#input=bytearray(open("/Users/rashmisahu/Desktop/am1.jpg", "rb").read())

client = Algorithmia.client('simb+HoZt1y2rsh4qvaHZ4pGbdy1')
algo = client.algo('algorithmiahq/DeepFashion/1.2.2')

b= (algo.pipe(input).result)['articles']
print b

len1=len(b)

for i in range(0,len1):
	print b[i]['bounding_box']
	x=b[i]['bounding_box']
	img1=img.crop((x['x0'],x['y0'],x['x1'],x['y1']))
	img1.show()
	#break;



