import nltk
import codecs
import gensim
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from sklearn import svm
import pdb
brown_ic = wordnet_ic.ic('ic-brown.dat')
modelHuang = gensim.models.Word2Vec.load('E:\\HuangModel')
inFile = codecs.open("E:\\Homework1\\afterCompute\\set2.csv", 'r',"utf-8")
outFile = open("C:\\Users\\Aaron_Huang\\Desktop\\outSVMset2.csv","w")
line = inFile.readline()
X = []
y = []
while line:
	line = line.strip()
	list = line.split(",")
	word1 = wn.synsets(list[0])
	word2 = wn.synsets(list[1])
	same = 0
	diff = 0
	sim = -100
	if len(word1) == 0 or len(word2) == 0:
		same = 0
		diff = 0
		sim = -100
	else:
		for tmpword1 in word1:
			for tmpword2 in word2:
				if tmpword1.pos()==tmpword2.pos():
					same += 1
					try:
						sim = max(tmpword1.res_similarity(tmpword2,brown_ic),sim)
					except Exception as e:
						continue
					finally:
						pass
				else:
					diff += 1
	# print(list[0],list[1],same,diff,sim)
	outFile.write(list[0]+","+list[1]+","+str(same)+","+str(diff)+","+str(sim)+"\n")
	X.append([modelHuang[list[0]][0],modelHuang[list[1]][0],same,diff])
	# X.append([list[0],list[1],same,diff])
	y.append(sim)
	line = inFile.readline()
print(X[0])
clf = svm.SVR()
clf.fit(X,y)
set2File = codecs.open("C:\\Users\\Aaron_Huang\\Desktop\\outSVM1.csv", 'r',"utf-8")
set2outFile = open("C:\\Users\\Aaron_Huang\\Desktop\\set1Predict.csv","w")
set2line = set2File.readline()
newList = []
while set2line:
	set2line = set2line.strip()
	listset2 = set2line.split(',')
	newList.append([modelHuang[listset2[0]][0],modelHuang[listset2[1]][0],listset2[2],listset2[3]])
	set2line = set2File.readline()
predict = clf.predict(newList)
print(predict)
print(predict[0])
for i in range(len(predict)):
	set2outFile.write(str(predict[i])+"\n")
print("finished!")
