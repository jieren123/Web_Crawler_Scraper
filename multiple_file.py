import os
import glob 
import pandas as pd 
import file_clear


def struct_file(path_1, path_2):
	file_fail = []
	for file in os.listdir(path_1):
		filename_1 = os.path.join(path_1, file)
		filename_2 = os.path.join(path_2, file) 

		try:
			file_clear.structured_file(filename_1, filename_2)
		except:
			file_fail.append(file)

	print file_fail
 

#combine all files together
# path_1 and path_2 are common used

def combine_file_all(path_1, path_2):

	filelist = []
	df_list = []
	for file in os.listdir(path_1):
		filename_1 = os.path.join(path_1,file)
		try:
			df_list.append(pd.read_csv(filename_1,encoding='utf-16', header=None, sep = '\t'))
		except:
			print (filename_1)  

	full_df = pd.concat(df_list)
	names = [ 
			'account_name',	
			'fullname',
			'firstname',
			'lastname',
			'title',
			'email',
			'contact_phone',
			'work_address',
			'work_city',
			'work_state',
			'work_ZIP'
			]

	full_df.to_csv(path_2 + 'file_name' +'.csv', index = False, header = names, encoding='utf-16', sep = '\t')


#
 
def combine_file_part(num_of_file,path_1, path_2):

	filelist = []
	df_list = []
	for file in os.listdir(path_1):
		filename_1 = os.path.join(path_1,file)
		filelist.append(filename_1)

	# define how many file you want to combine here
	filelist_1 = filelist[:num_of_file]

	names = [ 
			'company',	
			'firstname',
			'lastname',
			'title',
			'email',
			'contact_phone',
			'work_address',
			'work_city',
			'work_state',
			'work_ZIP'
			]

	for singe_file in filelist_1:
		try:
			df_list.append(pd.read_csv(singe_file, encoding='utf-16', header=None, sep = '\t'))
		except:
			print (filename_1)  

	full_df = pd.concat(df_list)

	full_df.to_csv(path_2 + 'Fed_Gov' +'_1.csv', index = False, header = names, encoding='utf-16', sep = '\t')
	full_df.shape



