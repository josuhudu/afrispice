# Python program to validate an Email 

# import re module 

# re module provides support 
# for regular expressions 
import re 

# Make a regular expression 
# for validating an Email 
regex = r"^[A-Z][0-9]{2,2}/[0-9]{4,6}/[0-9]{4,4}$"
	
# Define a function for 
# for validating an Email 
def valid_registration(registration): 

	# pass the regualar expression 
	# and the string in search() method 
	if(re.search(regex,registration)): 
		return True
		
	else: 
		return False

def obtainDir(model):
	table = model._meta.model_name
	department = model.department.name
	year = model.year
	course = model.course.code
	category = models.category

	return f'/{table}/{department}/{year}/{course}/{category}'

	

"""		
import cv2

def image_compress(image):
	img=cv2.imread(image)

	#file / image object
	cv2.imwrite( f'{image.name} compressed', img, [cv2.IMWRITE_JPEG_QUALITY, 20] )
"""
# Driver Code 
if __name__ == '__main__' : 
	
	# Enter the email 
	registration = "F17/81926/2017"
	
	# calling run function 
	check(registration) 

	registration = "F1/81926/201"
	check(registration) 

	registration = "F1/819/2017"
	check(registration) 