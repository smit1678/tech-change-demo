import csv, sys, json, time, datetime, traceback
from itertools import groupby
from operator import itemgetter
import nltk
import numpy

t0 = time.time()
row_count = 0

raw_data = csv.DictReader(open('tech-change-drc-data_out.csv', 'rU'), delimiter = ',', quotechar = '"')
data_sort = sorted(raw_data, key = lambda x: x['province'])

data_output = []
for province,data in groupby(data_sort, itemgetter('province')):
	if province == "":
		pass
	else:
		row_count = 0
		elec_count = 0
		school_count = 0
		bin = [province]
		q1bin = []
		q2bin = []
		q3bin = []
		q4bin = []
		q5bin = []
		q6bin = []
		q7bin = []
		q8bin = []
		q9bin = []
		q10bin = []
		latbin = []
		lonbin = []
		for d in data:
			row_count = row_count + 1
			q1bin.append(d['q1'])
			q2bin.append(d['q2'])
			q3bin.append(d['q3'])
			q4bin.append(d['q4'])
			q5bin.append(d['q5'])
			q6bin.append(d['q6'])
			q7bin.append(d['q7'])
			q8bin.append(d['q8'])
			q9bin.append(d['q9'])
			q10bin.append(d['q10'])
			latbin.append(float(d['latitude']))
			lonbin.append(float(d['longitude']))
		fdist1 = nltk.FreqDist(q1bin)
		fdist2 = nltk.FreqDist(q2bin)
		fdist3 = nltk.FreqDist(q3bin)
		fdist4 = nltk.FreqDist(q4bin)
		fdist5 = nltk.FreqDist(q5bin)
		fdist6 = nltk.FreqDist(q6bin)
		fdist7 = nltk.FreqDist(q7bin)
		fdist8 = nltk.FreqDist(q8bin)
		fdist9 = nltk.FreqDist(q9bin)
		fdist10 = nltk.FreqDist(q10bin)
		bin.append(fdist1.max())
		bin.append(fdist2.max())
		bin.append(fdist3.max())
		bin.append(fdist4.max())
		bin.append(fdist5.max())
		bin.append(fdist6.max())
		bin.append(fdist7.max())
		bin.append(fdist8.max())
		bin.append(fdist9.max())
		bin.append(fdist10.max())
		bin.append(round(fdist1.freq(fdist1.max())*100,2))
		bin.append(round(fdist2.freq(fdist2.max())*100,2))
		bin.append(round(fdist3.freq(fdist3.max())*100,2))
		bin.append(round(fdist4.freq(fdist4.max())*100,2))
		bin.append(round(fdist5.freq(fdist5.max())*100,2))
		bin.append(round(fdist6.freq(fdist6.max())*100,2))
		bin.append(round(fdist7.freq(fdist7.max())*100,2))
		bin.append(round(fdist8.freq(fdist8.max())*100,2))
		bin.append(round(fdist9.freq(fdist9.max())*100,2))
		bin.append(round(fdist10.freq(fdist10.max())*100,2))
		bin.append(numpy.mean(latbin))
		bin.append(numpy.mean(lonbin))
		data_output.append(bin)

header = ['province','q3_mostcommon','q4_mostcommon','q5_mostcommon','q6_mostcommon','q7_mostcommon','q8_mostcommon','q9_mostcommon','q10_mostcommon','q11_mostcommon','q12_mostcommon','q3_mostcommon_pct','q4_mostcommon_pct','q5_mostcommon_pct','q6_mostcommon_pct','q7_mostcommon_pct','q8_mostcommon_pct','q9_mostcommon_pct','q10_mostcommon_pct','q11_mostcommon_pct','q12_mostcommon_pct','lat','lon']
out = open('tech-change-process-output.csv', 'wb')
writer = csv.writer(out)
writer.writerow(header)
for row in data_output:
    writer.writerow(row)
out.close()
