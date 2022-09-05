'''A python script to:
1. Generate canonical SMILES for each of the compounds in your SD/SDF compound library,
2. Detect redundant ligands/structural isomers in the library, 
3. Generate unique and redundant name lists and, optionally, 
4. Move redundant ligands/structural isomers to a separate file producing a library of unique compounds.

	Author: Abeeb A. YEKEEN

	Contact: yekeenaa@mail.ustc.edu.cn, abeeb.yekeen@hotmail.com

	Date: 2021.11.03
'''

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from builtins import round
from builtins import input
from builtins import open
from builtins import str
#from future import standard_library
#standard_library.install_aliases()
import os
from rdkit import Chem
import time


def track_status():
	print(status)
	log_file.write(status)

def citation():
	status='\nIf you use this program in your work, please cite the relevant paper:\n\n    "Yekeen et al. (2022). To be published..."\n'
	print(status)
	log_file.write(status)

def functn():
	purpose='\nThis program will help you\n *1. Generate canonical SMILES for each of the compounds in your SD/SDF compound library,\n *2. Detect redundant ligands/structural isomers from the compound library,\n *3. Generate unique and redundant name lists and, optionally,\n *4. Move redundant ligands/structural isomers to a separate file, generating a library of unique compounds'
	print(purpose)

functn()

status="\nGive a name to this job: "
job_name=str(input(status ))
record="log_"+job_name+".log"
print("\n")
status="Jobname: "+job_name+"\n"
print(status)
log_file=open(record, "w")
log_file.close()
log_file=open(record, "a")
log_file.write(status)
status="Please copy and paste here the name of the SD/SDF file from which you wish to detect redundant ligands/structural isomers: "
log_file.write(status)
filename=str(input(status ))
status="\nYou entered: "+str(filename)+"\n"
track_status()

ini1_time = time.time() #start time of check_duplicate

if filename[-4:]==".sdf":
	filename=filename[0:-4]
	status="    Filename has the extension .SDF!\n    Corrected file name is: "+filename+"\n"
	track_status()
elif filename[-3:]==".sd":
	filename=filename[0:-3]
	status="    Filename has the extension .SD!\n    Corrected file name is: "+filename+"\n"
	track_status()

sdfile=filename+".sdf"
time.sleep(2)
#opening the full SD/SDF file
status="Opening "+sdfile+" ...\n"
track_status()

library=open(sdfile, "r")

citation()

#reading the SDF files in the library
status="\nReading the contents of "+sdfile+" ...\n"
track_status()
time.sleep(2)
datalines=library.readlines()
status="Contents of "+sdfile+" have been read, now assigning variables...\n"
track_status()
time.sleep(2)
compd_no=0
milestone_factor=0
all_compds=0
liner=0
current_compd=[]
current_compd_line_no=0
smiles_generated=0
duplicate_count=0
dupli_list_list=[]
dataline_no=0
status="Reading structures from "+sdfile+" ...\n"
track_status()
uniq_name_list_list=[]
sdfile_plusSmiles=filename+"_smilesAdded.sdf"
sdfile_WithSmiles=open(sdfile_plusSmiles, "w")
sdfile_WithSmiles.close()

for data in datalines:
	data=str(data)
	dataline_no+=1
	current_compd.append(data)
	if " END" in data:
		with open('rdk_temp.sdf', 'w') as tempForRDK:
			for inf in current_compd:
				tempForRDK.write(inf)
		temp_lig = Chem.MolFromMolFile('rdk_temp.sdf')
		#current_compd_smi = Chem.MolToSmiles(temp_lig,isomericSmiles=False)
		current_compd_noH = Chem.RemoveHs(temp_lig)
		current_compd_smi = Chem.MolToSmiles(current_compd_noH,isomericSmiles=False)
		os.remove('rdk_temp.sdf')
		current_compd.append("\n")
		current_compd.append(">  <SMILES_canonical>")
		current_compd.append("\n")
		current_compd.append(current_compd_smi)
		current_compd.append("\n")
		smiles_generated+=1
		continue	
	if smiles_generated==1:
		if current_compd_smi in uniq_name_list_list:
			duplicate_count+=1
			if duplicate_count==1:
				status="    "+str(duplicate_count)+" redundant ligand/redundant structural isomer found...\n"
				track_status()
			if duplicate_count%250==0:
				status="    "+str(duplicate_count)+" redundant ligands/structural isomers found...\n"
				track_status()
			#adding duplicate compd name and smiles to the corresponding temp list
			dupli_smi_name=current_compd[0]
			dupli_list_list.append(dupli_smi_name)
			#dupli_list_list.append("\n")
			dupli_list_list.append(current_compd_smi)
			dupli_list_list.append("\n")
			smiles_generated=0
			continue
		else:
			#adding unique compd name and smiles to the corresponding temp list
			uniq_smi_name=current_compd[0]
			uniq_name_list_list.append(uniq_smi_name)
			uniq_name_list_list.append(current_compd_smi)
			uniq_name_list_list.append("\n")
			smiles_generated=0
	if "$$$$" in data:
		compd_no+=1
		with open(sdfile_plusSmiles, 'a') as sdfWTsmiles:
			for inf in current_compd:
				sdfWTsmiles.write(inf)
		current_compd=[]
		if compd_no%5000==0:
			milestone_factor+=1
			milestone_count=milestone_factor*5000
			status="    No of compounds processed so far: " +str(milestone_count)+"\n"
			track_status()
	if dataline_no==len(datalines):
		all_compds=compd_no
status="    The last compound has been successfully processed\n"
track_status()
time.sleep(2)
status="Writing out the compound names and smiles...\n"
time.sleep(1)
track_status()
name_smi_LIST="non-redundant_isounique_list_"+filename+".txt"
name_smi_L=open(name_smi_LIST, "w")
for comp in uniq_name_list_list:
	name_smi_L.write(comp)
if duplicate_count==0:
	status="    All "+str(all_compds)+" compounds have been processed.\n\nNo redundant ligands/structural isomers were found.\n"
	track_status()
	time.sleep(2)
	status="\nRecord of this job can be found in the file "+'"'+record+'"'
	track_status()
	time.sleep(1)
	end1_time = time.time() #end time of check_duplicate
	runtime1_sec = (end1_time-ini1_time)
	if runtime1_sec>60.0:
		runtime1_sec_2d = float("{:.2f}".format(runtime1_sec%60))
	elif runtime1_sec<60.0:
		runtime1_sec_2d = float("{:.2f}".format(runtime1_sec))
	runtime1_min = round(runtime1_sec//60)
	runtime1_hr = round(runtime1_sec//3600)
	status="Time elapsed for duplicate check: "+str(runtime1_hr)+" hr "+str(runtime1_min)+" min "+str(runtime1_sec_2d)+" sec\n"
	track_status()
	
elif duplicate_count>0:
	dupli_LIST="duplicate_list_"+filename+".txt"
	dupli_L=open(dupli_LIST, "w")
	for dup in dupli_list_list:
		dupli_L.write(dup)
	status="    All "+str(all_compds)+" compounds have been processed.\n"
	track_status()
	time.sleep(2)
	status="    A total of "+str(duplicate_count)+" redundant ligands were found and will be saved to "+'"'+dupli_LIST+'"'
	track_status()
	time.sleep(2)
	status="\n    A new compound library "+'"'+sdfile_plusSmiles+'"'+" will be written"
	track_status()
	time.sleep(2)
	status="\n    "+'"'+sdfile_plusSmiles+'"'+" will contain the generated canonical SMILES"
	track_status()
	time.sleep(2)
	end1_time = time.time() #end time of check_duplicate
	runtime1_sec = (end1_time-ini1_time)
	if runtime1_sec>60.0:
		runtime1_sec_2d = float("{:.2f}".format(runtime1_sec%60))
	elif runtime1_sec<60.0:
		runtime1_sec_2d = float("{:.2f}".format(runtime1_sec))
	runtime1_min = round(runtime1_sec//60)
	runtime1_hr = round(runtime1_sec//3600)
	status="Time elapsed for duplicate check: "+str(runtime1_hr)+" hr "+str(runtime1_min)+" min "+str(runtime1_sec_2d)+" sec\n"
	track_status()
	
	citation()
	
	status="\nDo you want to move the redundant ligands/structural isomers to a new file and reduce your compound library to a set of isounique ligands?\n"
	log_file.write(status)
	track_status()
	time.sleep(1)
	status="\n    Please enter a response here (yes/no): "
	log_file.write(status)
	response=str(input(status ))
	while response != "yes" and response != "no":
		status="\nYou entered: "+str(response)+"\n"
		track_status()
		status="ENTRY REJECTED!\nPLEASE PROVIDE A VALID RESPONSE (yes/no)!\n"
		track_status()
		status="\nDo you want to move the redundant ligands/structural isomers to a new file and reduce your compound library to a set of isounique ligands?\n    Please enter a response here (yes/no): "
		response=str(input(status ))
	
	ini2_time = time.time() #start time of move_duplicate
	
	status="\nYou entered: "+str(response)+"\n"
	track_status()
	library.close()
	if response=="yes":
		#opening the newly written SD/SDF file containing the generated smiles
		status="Opening "+sdfile_plusSmiles+" ...\n"
		track_status()
		
		library=open(sdfile_plusSmiles, "r")
		
		citation()
		#reading the SDF files in the new SMILES-containing library
		status="\nReading the contents of "+sdfile+" ...\n"
		track_status()
		time.sleep(1)
		datalines=library.readlines()
		status="Contents of "+sdfile_plusSmiles+" have been read, now assigning variables...\n"
		track_status()
		time.sleep(2)
		isounique_lib="isounique_"+filename+".sdf"
		uniqueL=open(isounique_lib, "w")
		uniqueL.close()
		moved_dupli_lib="struct_isos_from_"+filename+".sdf"
		moved_dupli=open(moved_dupli_lib, "w")
		moved_dupli.close()
		x_all_compds=0
		x_uniq_name_list_list=[]
		x_dupli_list_list=[]
		x_dataline_no=0
		x_compd_no=0
		x_duplicate_count=0
		x_milestone_factor=0
		x_duplicate_count=0
		x_smi_detect=0
		x_current_compd=[]
		caught=0
		status="\nReading structures from "+sdfile_plusSmiles+", preparing to move redundant ligands/structural isomers to a new file...\n"
		
		track_status()
		for x_datar in datalines:
			x_datar=str(x_datar)
			x_dataline_no+=1
			x_current_compd.append(x_datar) #appending data for current lig
			if ">  <SMILES_canonical>" in x_datar:
				x_smi_detect+=1 #detected smiles header for current lig in sdf library
				continue
			if x_smi_detect==1:
				if x_datar in x_uniq_name_list_list:
					caught=1
					x_dupli_smi_name=x_current_compd[0] #fetch name of current lig
					x_dupli_list_list.append(x_dupli_smi_name)
					x_dupli_list_list.append(x_datar)
					x_smi_detect=0
					continue
				else:
					x_uniq_smi_name=x_current_compd[0]
					x_uniq_name_list_list.append(x_uniq_smi_name)
					x_uniq_name_list_list.append(x_datar)
					caught=0
					x_smi_detect=0
			if "$$$$" in x_datar:
				x_compd_no+=1
				#current_compd=[]
				if x_compd_no%5000==0:
					x_milestone_factor+=1
					x_milestone_count=x_milestone_factor*5000
					status="    No of compounds processed: " +str(x_milestone_count)+"\n"
					track_status()
				if caught==1:
					moved_dupli_lib="struct_isos_from_"+filename+".sdf"
					moved_dupli=open(moved_dupli_lib, "a")
					for inf in x_current_compd:
						moved_dupli.write(inf)
					x_duplicate_count+=1
					if x_duplicate_count==1:
						status="    "+str(x_duplicate_count)+" redundant ligand has been moved to "+"struct_isos_from_"+filename+".sdf\n"
						track_status()
					elif x_duplicate_count%250==0:
						status="    "+str(x_duplicate_count)+" redundant ligands have been moved to "+"struct_isos_from_"+filename+".sdf\n"
						track_status()
					x_current_compd=[]
					caught=0
					continue
				if caught==0:
					isounique_lib="isounique_"+filename+".sdf"
					uniqueL=open(isounique_lib, "a")
					for inf in x_current_compd:
						uniqueL.write(inf)
					x_current_compd=[]
					continue
		if x_dataline_no==len(datalines):
			x_all_compds=x_compd_no
			isounique_compounds=x_all_compds-x_duplicate_count
			status='    All '+str(x_all_compds)+' compounds have been successfully processed.\n\nYour library "isounique_'+filename+'.sdf" now contains '+str(isounique_compounds)+' isounique ligands.\n\nA total of '+str(x_duplicate_count)+' redundant ligands were found and have been moved to '+'"struct_isos_from_'+filename+'.sdf"\n'
			track_status()
		moved_dupli.close()
		uniqueL.close()
	elif response=="no":
		print()
status="Job completed\n\nRecord of this job can be found in the file "+'"'+record+'"\n'
track_status()
name_smi_L.close
library.close()

end2_time = time.time() #end time of move_duplicate
runtime2_sec = (end2_time-ini2_time)
if runtime2_sec>60.0:
	runtime2_sec_2d = float("{:.2f}".format(runtime2_sec%60))
elif runtime2_sec<60.0:
	runtime2_sec_2d = float("{:.2f}".format(runtime2_sec))
runtime2_min = round(runtime2_sec//60)
runtime2_hr = round(runtime2_sec//3600)
status="Time elapsed for processing of duplicates: "+str(runtime2_hr)+" hr "+str(runtime2_min)+" min "+str(runtime2_sec_2d)+" sec"
track_status()

total_runtime_sec=runtime1_sec+runtime2_sec #for both check_duplicate and move_duplicate
if total_runtime_sec>60.0:
	total_runtime_sec_2d = float("{:.2f}".format(total_runtime_sec%60))
elif total_runtime_sec<60.0:
	total_runtime_sec_2d = float("{:.2f}".format(total_runtime_sec))
total_runtime_min = round(total_runtime_sec//60)
total_runtime_hr = round(total_runtime_sec//3600)
status="\nTotal time elapsed: "+str(total_runtime_hr)+" hr "+str(total_runtime_min)+" min "+str(total_runtime_sec_2d)+" sec\n"
track_status()
citation()
log_file.close()			
