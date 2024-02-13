import sys
import os
import statistics

count = 0
IS_all = []
IS_all_str = []
Score = []
Score_str = []

with open('score_MutDock_native', "r") as file:
    readoutput = file.readlines()
    phrase_SCORE = 'SCORE'
    for line in readoutput:
        if phrase_SCORE in line:
            count = count + 1
            if count == 1:
                print(line[6:20])
            #elif count == 2:
                #print(line[6:20])
            else:
                sc = float(line[6:20])
                Score.append(sc)
                Score_str.append(str(sc))
                IS = float(line[503:513])
                IS_all.append(IS)
                IS_all_str.append(str(IS))

print('IS: ',IS_all)
print('Score: ',Score)
IS_total = 0
Score_total = 0

for x in range(0,len(IS_all)):
    IS_total = IS_total + IS_all[x]
    Score_total = Score_total + Score[x]

score_avg = Score_total/len(Score)
score_stdev = statistics.stdev(Score)
IS_avg = IS_total/len(IS_all)
IS_stdev = statistics.stdev(IS_all)

print('\n\n')
print('Score avg: ',score_avg)
print('Score STDEV: ',score_stdev)
print('Interface score avg: ',IS_avg)
print('Interface score STDEV: ',IS_stdev)
print('\n')