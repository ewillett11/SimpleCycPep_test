import sys
import os

#Enter nstruct of docking
nstruct = 5

count = 0
AA_string = []
AA_list = []
score = []
score_str = []
Name_all = []
AA_all = []

CBLcombined_name = 'Mutate_MCnative_CBLcombined.pdb'
MC_PDBname = ''.join(['hNSP4_14mer_align','.pdb'])
MC_PDBname2 = ''.join(['0_hNSP4_14mer_align_0001','.pdb'])
CBL_name = 'hNSP4_crystal_chainA.pdb'
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