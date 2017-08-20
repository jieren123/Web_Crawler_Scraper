import os
import glob 
import pandas as pd 
import file_clear

#path_1 = '/Users/JieREN/Desktop/ihope/web_scraping/Non_profit_2/'
#path_2 = '/Users/JieREN/Desktop/ihope/web_scraping/Non_profit_2_s/'

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
path_1 = '/Users/JieREN/Desktop/ihope/web_scraping/congress_data_structured/'
path_2 = '/Users/JieREN/Desktop/ihope/web_scraping/salesforce_data/'

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
path_1 = '/Users/JieREN/Desktop/ihope/web_scraping/Federal_Governments_data_structured'
path_2 = '/Users/JieREN/Desktop/ihope/web_scraping/salesforce_data/'

def combine_file_part(num,path_1, path_2):

	filelist = []
	df_list = []
	for file in os.listdir(path_1):
		filename_1 = os.path.join(path_1,file)
		filelist.append(filename_1)

	# define how many file you want to combine here
	filelist_1 = filelist[:num]

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


file_1 = '/Users/JieREN/Desktop/ihope/web_scraping/Federal_Governments_data_structured/Fed_Gov_Data_1.cvs'
df = pd.read_csv(file_1, encoding='utf-16', header=None, sep = '\t')

df.to_csv(file_1, index = False, header = names, encoding='utf-16', sep = '\t')

