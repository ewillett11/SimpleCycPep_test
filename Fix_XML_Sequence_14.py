import sys
import os
#import numpy as np
#import random

#Enter nstruct of docking
nstruct = 5

#Enter sequence
sequence = 'SGFDATRERQIIPFL'
new_name = 'binder2_MC'
new_name_pdb = ''.join([new_name,'.pdb'])
MCnative = '14mer_MC_align13mer'
CBL_name = 'hNSP4_crystal_chainA_mutS.pdb'

#change sequence
sequence_len = len(sequence)-1
sequence_long_rev = []
AA_mut_number = []
count_dash = 0
sequence_long_rev.append('CYS')
count_AA = 0
count_AA = count_AA + 1
AA_mut_number.append(str(count_AA))
for x in range(0,sequence_len-1):
    if sequence[sequence_len-x] == "-":
        count_dash = 1
    elif sequence[sequence_len-x] == " ":
        print('ignore')
    elif count_dash == 1:
        NCAA_name = input('Enter NCAA name (in reverse order): ')
        count_dash = 0
        sequence_long_rev.append(NCAA_name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "A":
        name = 'ALA'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "C":
        name = 'CYS'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "D":
        name = 'ASP'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "E":
        name = 'GLU'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "F":
        name = 'PHE'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "G":
        name = 'GLY'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "H":
        name = 'HIS'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "I":
        name = 'ILE'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "K":
        name = 'LYS'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "L":
        name = 'LEU'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "M":
        name = 'MET'
        count_AA = count_AA + 1
        sequence_long_rev.append(name)
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "N":
        name = 'ASN'
        count_AA = count_AA + 1
        sequence_long_rev.append(name)
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "P":
        name = 'PRO'
        count_AA = count_AA + 1
        sequence_long_rev.append(name)
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "Q":
        name = 'GLN'
        count_AA = count_AA + 1
        sequence_long_rev.append(name)
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "R":
        name = 'ARG'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "S":
        name = 'SER'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "T":
        name = 'THR'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "V":
        name = 'VAL'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "W":
        name = 'TRP'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    elif sequence[sequence_len-x] == "Y":
        name = 'TYR'
        sequence_long_rev.append(name)
        count_AA = count_AA + 1
        AA_mut_number.append(str(count_AA))
    else:
        print('fix amino acids')

sequence_long = sequence_long_rev[::-1]
print('sequence long: ',sequence_long)
AAmer = len(AA_mut_number)
print('AA mut num: ',AA_mut_number,AAmer)
AAmer = len(AA_mut_number)

count = 0
AA_string = []
AA_list = []
score = []
score_str = []
IntScore = []
IntScore_str = []
Name_all = []
AA_all = []
XML_mutate = 'MutateAF.xml'
XML_mutate_change = 'MutateAF_Fix.xml'
CBLcombined_name = 'Mutate_MCnative_CBLcombined.pdb'
#score_low = 426.337
#IntScore_low = -0.715
AA_translate = []
AA_translate_all = []
AA_string_translate = []
count_stop = 0
count_remove = 0
count_low = 0

# delete contents of file2
with open(CBLcombined_name, "w") as file_xml_change:
    file_xml_change.truncate(0)

# delete contents of file xmlchange
    with open(XML_mutate_change, "w") as file_xml_change:
        file_xml_change.truncate(0)

MC_PDBname = ''.join([MCnative, '.pdb'])
with open(XML_mutate, "r") as file_xml:
    readoutput_xml = file_xml.readlines()
    phraseROSETTASCRIPTS = 'ROSETTASCRIPTS'
    phraseSCOREFXNS = 'SCOREFXNS'
    phraseScoreFunction = 'ScoreFunction'
    phraseRESIDUE = 'RESIDUE_SELECTORS'
    phraseIndex = 'Index name="residue'
    phraseIndex_keep = 'Index name="select_cterm"'
    phraseTASKOPERATIONS = 'TASKOPERATIONS'
    phraseRestrict = 'Restrict'
    phraseFILTERS = 'FILTERS'
    phraseMOVERS = 'MOVERS'
    phraseMUTATE = '<MutateResidue'
    phraseDECLAREBOND = 'DeclareBond'
    phraseMODIFY = 'ModifyVariantType'
    phraseRotamerTrialsMinMover = 'RotamerTrialsMinMover'
    phraseFastRelax = 'FastRelax'
    phrasePROTOCOLS = 'PROTOCOLS'
    phraseMut = 'Add mover="mut'
    phraseVar = 'Add mover="var'
    phraseRot = 'Add mover="rot'
    phraseRel= 'Add mover="rel'
    with open(XML_mutate_change, "w") as file_xml_change:
        for line_xml in readoutput_xml:
            if phraseROSETTASCRIPTS in line_xml:
                file_xml_change.write(line_xml)
            if phraseSCOREFXNS in line_xml:
                file_xml_change.write(line_xml)
            if phraseScoreFunction in line_xml:
                file_xml_change.write(line_xml)
            if phraseRESIDUE in line_xml:
                file_xml_change.write(line_xml)
            if phraseIndex_keep in line_xml:
                new_line_xml_I = ''.join([line_xml[0:44], str(AAmer),line_xml[46:60]])
                file_xml_change.write(new_line_xml_I)
            if phraseIndex in line_xml:
                for x in range(1,AAmer-1):
                    print(line_xml)
                    index_AA = line_xml[38:40]
                    print(index_AA)
                    line_xml_beforeI1 = line_xml[0:28]
                    line_xml_beforeI2 = line_xml[28:38]
                    line_xml_afterI = line_xml[41:100]
                    new_line_xml_I = ''.join([line_xml_beforeI1, str(x+1),line_xml_beforeI2,'"',str(x+1),'"', line_xml_afterI])
                    file_xml_change.write(new_line_xml_I)
            if phraseTASKOPERATIONS in line_xml:
                file_xml_change.write(line_xml)
            if phraseRestrict in line_xml:
                file_xml_change.write(line_xml)
            if phraseFILTERS in line_xml:
                file_xml_change.write(line_xml)
            if phraseMOVERS in line_xml:
                file_xml_change.write(line_xml)
            if phraseMUTATE in line_xml:
                for x in range(1,AAmer-1):
                    print(line_xml)
                    mutate_AA = line_xml[69:82]
                    print(mutate_AA)
                    line_xml_beforeM1 = line_xml[0:36]
                    line_xml_beforeM2 = line_xml[37:64]
                    line_xml_afterM = line_xml[81:135]
                    new_line_xml = ''.join([line_xml_beforeM1,str(x+1),line_xml_beforeM2,str(x+1), '" new_res="',sequence_long[x], '" ', line_xml_afterM])
                    file_xml_change.write(new_line_xml)
            if phraseDECLAREBOND in line_xml:
                file_xml_change.write(line_xml)
            if phraseMODIFY in line_xml:
                file_xml_change.write(line_xml)
            if phraseRotamerTrialsMinMover in line_xml:
                file_xml_change.write(line_xml)
            if phraseFastRelax in line_xml:
                file_xml_change.write(line_xml)
            if phrasePROTOCOLS in line_xml:
                file_xml_change.write(line_xml)
            if phraseMut in line_xml:
                for x in range(1,AAmer-1):
                    change = ''.join([line_xml[0:27],str(x+1),'" />\n'])
                    file_xml_change.write(change)
            if phraseRot in line_xml:
                file_xml_change.write(line_xml)
            if phraseRel in line_xml:
                file_xml_change.write(line_xml)
    basic_flag = ''.join(['-in:file:s ',MC_PDBname])
    basic_command = ''.join(['~/rosetta.binary.mac.release-351/main/source/bin/rosetta_scripts.static.macosclangrelease @mutateNCAA.flags ',basic_flag])
    print(basic_command)
    os.system(basic_command)

with open('score_MutatePACK', "r") as file_score:
    readoutput_score = file_score.readlines()
    SCOREphrase = 'SCORE: '
    count1 = 0
    score = []
    score_str = []
    state_str = []
    state = []
    for line in readoutput_score:
        if SCOREphrase in line:
            count1 = count1 + 1
            if count1 == 1:
                print('IGNORE')
            else:
                SCOREnum_str = line[8:20]
                SCOREnum = float(line[8:20])
                score.append(SCOREnum)
                score_str.append(SCOREnum_str)
                stateNUM_str = line[292:296]
                print(stateNUM_str)
                stateNUM = round(float(line[292:296]))
                state.append(stateNUM)
                state_str.append(stateNUM_str)

# Check to make sure number of scores = number of RMSD = number of states
print(score)
length_score = len(score)

score.sort()
print(score)
# score_sort_nodup = list(set(score,reverse =True))
# print(score_sort_nodup)
score_sort_str = []
length_score_nodup = len(score)
print(length_score_nodup)
for x in range(0, length_score_nodup):
    score_sort_str.append(str(score[x]))

score_list = []
for i in range(0,length_score_nodup):
    for z in range(0,length_score):
        score_index = score_str[z].find(score_sort_str[i])
        if score_index != -1:
            print(i)
            score_list.append(state_str[z])
            score_list.append(score_sort_str[i])
print(score_list)

output_name = ''.join(['MDOCK_',MCnative,'_',score_list[0],'.pdb'])
print('output name: ',output_name,'changed to :',new_name_pdb)
os.rename(output_name,new_name_pdb)

count = 0
AA_string = []
AA_list = []
score = []
score_str = []
Name_all = []
AA_all = []

CBLcombined_name = 'Mutate_MCnative_CBLcombined.pdb'
MC_PDBname = ''.join([new_name,'.pdb'])
MC_PDBname2 = ''.join(['0_',new_name,'_0001','.pdb'])
infileflag = ''.join(['-in:file:s ',MC_PDBname])
packflag = ''.join(['-out:prefix ', str(count), '_'])
packcommand = ''.join(['~/rosetta.binary.mac.release-351/main/source/bin/rosetta_scripts.static.macosclangrelease @mutatePACK.flags ',packflag,' ',infileflag])
os.system(packcommand)
with open(CBLcombined_name, "r+") as file2:
    readoutput2 = file2.readlines()
    with open(CBL_name, "r") as file1:
        readoutput1 = file1.readlines()
        phraseHETATM = 'HETATM'
        phraseATOM = 'ATOM'
        countHETATM = 0
        for line1 in readoutput1:
            if phraseATOM in line1:
                countHETATM = countHETATM + 1
                print(line1)
                file2.write(line1)
            if phraseHETATM in line1:
                countHETATM = countHETATM + 1
                print(line1)
                file2.write(line1)
    file2.write('TER \n')
    with open(MC_PDBname2, "r") as file3:
        readoutput3 = file3.readlines()
        phraseHETATM = 'HETATM'
        phraseATOM = 'ATOM'
        phraseLINK = 'LINK'
        phraseCA = 'CA '
        countHETATM = 0
        for line3 in readoutput3:
            if phraseLINK in line3:
                file2.write(line3)
                print(line3)
            if phraseATOM in line3:
                countHETATM = countHETATM + 1
                file2.write(line3)
                print(line3)
            if phraseHETATM in line3:
                countHETATM = countHETATM + 1
                file2.write(line3)
                print(line3)
            if phraseCA in line3:
                AA_name = line3[17:21]
                AA_string.append(AA_name)
                print(line3)
        file2.write('TER \n')
        file2.write('END \n')
        AA_seq = ''.join(AA_string)
        AA_list.append(AA_seq)

print(AA_seq)
print(AA_list)

#setting up docking flags
flag1 = '-out:pdb '
flag2 = ''.join(['-out:prefix ','Mutate_Dock_',str(count),'_'])
command_dock = ''.join(['~/rosetta.binary.mac.release-351/main/source/bin/rosetta_scripts.static.macosclangrelease @mutatedock.flags ',flag1,flag2])
print(command_dock)
os.system(command_dock)

#delete contents of file2
with open(CBLcombined_name, "w") as file2:
    file2.truncate(0)