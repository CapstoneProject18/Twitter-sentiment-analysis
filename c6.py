import matplotlib.pyplot as plt
import csv
import numpy as np
import math
 
x = []
y_stars_f1 = []
y_text_round_f1 = []
y_mean_round_f1 = []
 
i = 0
with open('result3-blog.csv') as myfile:    
    reader = csv.DictReader(myfile, delimiter=',')    
    for line in reader:    
        i += 1
        x.append(i)
                
        y_stars_f1.append(float(line['f1-user-rating']))
        y_text_round_f1.append(float(line['f1-review-rating']))
        y_mean_round_f1.append(float(line['f1-combined-rating']))
 
max_value = max([max(y_stars_f1), max(y_mean_round_f1), max(y_text_round_f1)])
 
fig = plt.figure()
 
ax = fig.add_subplot(111)
 
## the data (can be the number of rows in csv file)
N = 3
 
## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.25                      # the width of the bars
 
## the bars
rects1 = ax.bar(ind, y_stars_f1, width,
                color='lightblue',
                hatch="//"
                )
 
rects2 = ax.bar(ind+width, y_text_round_f1, width,
                    color='lightgreen',
                    hatch="-"
                    )
                    
rects3 = ax.bar(ind+width+width, y_mean_round_f1, width,
                    color='lightgrey',
                    hatch="x"
                    )
                    
# axes and labels
ax.set_xlim(-width,len(ind)+width+(width/2))
ax.set_ylim(0,max_value+0.1)
ax.set_ylabel('F1 measure')
ax.set_title('F1 Measure', color="black", weight="bold", size="large")
xTickMarks = ['Dataset '+str(i) for i in range(1,6)]
ax.set_xticks(ind+width+(width/2))
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0)
 
## add a legend
ax.legend( (rects1[0], rects2[0], rects3[0]), ('User ratings', 'Review ratings', 'Combined ratings'), loc='upper right', fancybox=True, shadow=True )
 
#ax.grid()
plt.show()
