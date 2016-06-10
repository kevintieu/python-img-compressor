import shutil
import os
import math
from PIL import Image

def convert(size):
	if (size == 0):
		return '0B'
	size_name = ("B", "KB", "MB", "GB", "TB")
	i = int(math.floor(math.log(size, 1024)))
	p = math.pow(1024, i)
	s = round(size / p, 2)
	return '%s %s' % (s, size_name[i])

def converttime(secs):
	mins, secs = divmod(secs, 60)
	return '%02d:%02d' % (mins, secs)

def validimage(fn):
	try:
		Image.open(fn)
		return True
	except:
		return False

def resize(fn):
	basewidth = 1024
	wpercent = (basewidth / float(fn.size[0]))
	hsize = int((float(fn.size[1] * float(wpercent))))
	try:
		fn.resize((basewidth, hsize), Image.ANTIALIAS)
		return True
	except IOError:
		return False

def runagain():
	print("\nOptimize another folder? (y/n)")
	choice = input().lower()
	if (choice == 'y' or choice == 'yes'):
		run()

def run():
	import time
	print("\nEnter a directory: ")
	user_dir = input()
	if os.path.exists(user_dir):
		print("\nCompressing...\n")

		start = time.time()
		total_size = 0
		compressed_size = 0
		total_imgs = 0
		compressed_imgs = 0
		min_width = 1024
		min_height = 768
		basewidth = 1024

		for subdir, dirs, files in os.walk(user_dir):
			for file in files:
				if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
					filepath = subdir + os.sep + file
					fail = subdir + os.sep + 'fail'
					if (validimage(filepath) == False):
						if not os.path.exists(fail):
							os.makedirs(fail)
						shutil.move(filepath, fail + os.sep + file)
						continue
					img = Image.open(filepath)
					wpercent = (basewidth / float(img.size[0]))
					hsize = int((float(img.size[1] * float(wpercent))))
					img_size = os.path.getsize(filepath)
					img_width = img.size[0]
					img_height = img.size[1]
					total_imgs += 1
					if img_width > min_width and img_height > min_height:
						temp = subdir + os.sep + '\\temp'
						if not os.path.exists(temp):
							os.makedirs(temp)
						if (resize(img) == False):
							if not os.path.exists(fail):
								os.makedirs(fail)
							shutil.move(filepath, fail + os.sep + file)
							continue
						img_c = img.resize((basewidth, hsize), Image.ANTIALIAS)
						img_c.save(temp + "\\" + file)
						filepath_c = temp + "\\" + file
						compressed_imgs += 1
						compressed_size += os.path.getsize(filepath_c)
						total_size += img_size
						img.close()

		end = time.time()
		time = round(end - start, 2)

		print("Compressed " + str(compressed_imgs) + " out of " + str(total_imgs) + " images")
		print("Raw size: " + convert(total_size) + "\nCompressed size: " + convert(compressed_size))
		print("\nTime elapsed: " + converttime(time))
		runagain()

	else:
		print("\nThis path does not exist")
		run()

run()