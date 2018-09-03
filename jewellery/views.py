from django.shortcuts import render
import base64
import cv2
import numpy as np
from PIL import Image
from .models import Jewellery,color,dress
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from jewellery.forms import ProfileForm
from jewellery.dominant_color import * 
from jewellery.detect_dress_path import *
import csv
import urllib.request
from io import StringIO
from django.core.files import File
import os
import math
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
#from jewellery.color_balance2 import * 

def csv_dict_reader(request):
    """
    Read a CSV file using csv.DictReader
    """
    with open("/Users/rashmisahu/voylla/jewellery/product.csv") as file_obj:
        #csv_dict_reader(f_obj)
    	reader = csv.DictReader(file_obj, delimiter=',')
    	i=1
    	for line in reader:
        	#print(line["Product Code"]),
        	#print(line["Image link 2"])
        	#result = urllib.request.urlretrieve(line["Image link 2"])
        	#link1=os.path.basename(line["Image link 2"]),File(open(result[0]))
        	p=Jewellery(id1=line["Product Code"],name=i,img=line["Image link 2"])
        	i=i+1
        	p.save()	
        	

    return HttpResponse("product details saved")


def display_jew(request):
	info=color.objects.all()
	print (info)
	fields=Jewellery._meta.get_fields()
	print(fields)
	images=[]
	for x in info:
		print (getattr(x,'color_name'))
		hex_code=(getattr(x,'color_hex'))
		print (hex_code)
		hex_code=hex_code.lstrip('#')
		rgb=tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))
		#print('RGB =', tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4)))
		print (rgb)
		j=x.jewellery.all()
		for t in j:	
			print (t.img)
			images.append(t.img)

		break
	context={'images':images}
	return render(request, 'jewellery/image.html',context)
		

	return HttpResponse("product details saved")


def upload_form(request):
	return render(request, 'jewellery/upload.html')

def next(request,profile):
	a,percentage=colorz(profile.picture)
	k=0
	context={'saved':saved,
			'image1':profile,
			'colors':a,
			'percentage':percentage,
			'k':k}

	return render(request, 'jewellery/saved.html',context)

def webcam(request):
	return render(request, 'jewellery/cam.html')
def color_match(rgb_dress,rgb_color):
	color1_rgb = sRGBColor(rgb_dress[0], rgb_dress[1], rgb_dress[2]);
	color2_rgb = sRGBColor(rgb_color[0], rgb_color[1], rgb_color[2]);

	color1_lab = convert_color(color1_rgb, LabColor);

	color2_lab = convert_color(color2_rgb, LabColor);


	delta_e = delta_e_cie2000(color1_lab, color2_lab);

	print ("The difference between the 2 color = ", delta_e)
	return delta_e


def upload(request):
	saved = False
	
	profile=dress()
	if request.method == "POST":
		MyProfileForm = ProfileForm(request.POST, request.FILES)
		

		if MyProfileForm.is_valid():
			
			
			profile.picture = request.FILES['picture']
			#profile.landscape = request.FILES['canvas']
			profile.save()
			saved = True
			
			
		else:
			MyProfileForm = ProfileForm()

		data = profile.picture.read()
		#data = profile.landscape.read()
		image = base64.b64encode(data)
		img=Image.open(profile.picture)
		img = img.convert("RGBA")
		#img.show()
		#cv2.imwrite('1.jpg',np.asarray(profile.picture),cv2.cv2.CV_IMWRITE_PXM_BINARY)
		#img=cv2.imread('1.jpg')
		#img.save('1.jpg')
		#img=Image.open('1.jpg')
		#mime ="" 
		#img='/Users/rashmisahu/voylla/1.jpg'
		# img2_path='/Users/rashmisahu/voylla/2.jpg'
		# img2= Image.open("/Users/rashmisahu/voylla/2.jpg")
		# im2=mainfn(img2)
		#mime = mime + ";" if mime else ";"
	a,percentage=detect(profile.picture,image)
	#a,percentage=detect(profile.landscape,image)
	# a2,percentage2=detect(img2_path,im2)
	k=0
	print (a[0])
	hex_code=a[0]
	hex_code=hex_code.lstrip('#')
	rgb_dress=tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))
	print (rgb_dress)
	print (rgb_dress[0])
	min1_rgb=30000
	min1_color=""
	color_details=[]
	color_object=""
	info=color.objects.all()
	for x in info:
		color_nam= (getattr(x,'color_name'))
		hex_code=(getattr(x,'color_hex'))
		#print (hex_code)
		hex_code=hex_code.lstrip('#')
		rgb_color=tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))
		color_details.append((color_nam,rgb_color))
		#diff=math.sqrt(((rgb_color[0]-rgb_dress[0])*(rgb_color[0]-rgb_dress[0]))+((rgb_color[1]-rgb_dress[1])*(rgb_color[1]-rgb_dress[1]))+((rgb_color[2]-rgb_dress[2])*(rgb_color[2]-rgb_dress[2])))
		diff=color_match(rgb_dress,rgb_color);
		if diff<min1_rgb:
			min1_rgb=diff
			min1_color=color_nam
			color_object=x

	print (min1_color)
	print (min1_rgb)
	print (color_details)
	print (color_object.color_name )
	images=[]
	j=color_object.jewellery.all()
	for t in j:	
		print (t.img)
		images.append(t.img)
	
	context={'saved':saved,
			'image1':profile,
			
			'colors':a,
			'percentage':percentage,
			#'colors2':a2,
			#'percentage2':percentage2,
			'k':k,
			'images':images}

	
	#return HttpResponse("Upload an image file")
	#return HttpResponseRedirect('next',profile)
	return render(request, 'jewellery/saved.html',context)
