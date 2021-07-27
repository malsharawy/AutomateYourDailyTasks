# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():
#	Change directory
	os.chdir('E:/SFTW/ansys')
#	Ensure the dir
	# print(os.getcwd())
#	Print files names 		
	for count, file in enumerate(os.listdir()):
		file_name, file_ext = os.path.splitext(file)
		p,x,year,ver,w,part = file_name.split('.')
		f_num = part.strip()[4:]
		print(file_name)
		new_name = '{}-{}{}-{}{}'.format(f_num,p,year,ver,file_ext)
		os.rename(file, new_name)

if __name__ == '__main__':
	
	# Calling main() function
	main()

'''
you can use the next line for adding zero in the begining 
f_num = f_num.zfill(3)

# 	for count, filename in enumerate(os.listdir("ansys")):
# 		dst ="ansys" + str(count) + ".rar"
# 		src = 'ansys' + filename	
# 		dst = 'change with file name' + dst
# 		# print(src)
# 		# print(dst)
		
# 		# rename() function will
# 		# rename all the files
# 		os.rename(src, dst)
'''

