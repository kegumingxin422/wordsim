import codecs
import string
import cosinsimilarity
import gensim
import time
import wordnetFunction
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
semcor_ic = wordnet_ic.ic('ic-semcor.dat')
import scipy

rootPath = 'E:\\Homework1\\afterCompute\\'
wnPath = ['pathSimilarity','WPSimilarity','LCSimilarity','JCSimilarity','ResinkSimilarity','LinSimilarity']
wnWritePath = ['wordnet_Path_Similarity.csv','wordnet_WP_Similarity.csv','wordnet_LC_Similarity.csv','wordnet_JC_Similarity.csv','wordnet_Resink_Similarity.csv','wordnet_Lin_Similarity.csv']
wnPathSet1 = ['pathSimilaritySet1','WPSimilaritySet1','LCSimilaritySet1','JCSimilaritySet1','ResinkSimilaritySet1','LinSimilaritySet1']
wnWritePathSet1 =  ['Set1_Path_Similarity.csv','Set1_WP_Similarity.csv','Set1_LC_Similarity.csv','Set1_JC_Similarity.csv','Set1_Resink_Similarity.csv','Set1_Lin_Similarity.csv']
wnPathSet2 = ['pathSimilaritySet2','WPSimilaritySet2','LCSimilaritySet2','JCSimilaritySet2','ResinkSimilaritySet2','LinSimilaritySet2']
wnWritePathSet2 =  ['Set2_Path_Similarity.csv','Set2_WP_Similarity.csv','Set2_LC_Similarity.csv','Set2_JC_Similarity.csv','Set2_Resink_Similarity.csv','Set2_Lin_Similarity.csv']

	###第一种相似度计算方法，直接调用训练好的word2vec相似度
def word2vec_Similarity(modelHuang,str1,str2,i,outFile):
	if i==1:
		print("word2vec_Similarity")
	writeStr = str1+","+str2+","+str(modelHuang.similarity(str1,str2))+"\n"
	outFile.write(writeStr)


	###第二种相似度计算方法，调用自己写的cosin相似度计算
def cosinSimilarity(modelHuang,str1,str2,outFile,i):
	if i==1:
		print("cosinSimilarity")
	writeStr = str1+","+str2+","+str(cosinsimilarity.cosine_similarity(modelHuang[str1],modelHuang[str2]))+"\n"
	outFile.write(writeStr)

	###第三种相似度计算方法，调用Wordnet中自带的6中课堂所讲的相似度计算方法
def wordnetSimilarity(str1,str2,i,outFile):
	if i==1:
		print("wordnetSimilarity")
	word1 = wn.synsets(str1)
	word2 = wn.synsets(str2)
	pathscore = -100
	Resnikscore = -100
	Linscore = -100
	JCscore = -100
	WPscore = -100
	LCscore = -100
	if len(word1) == 0 or len(word2) == 0:
		writeerrorStr = str1+","+str2+","+"-100"+"\n"
		for j in range(6):
			outFile[j].write(writeerrorStr)
	else:
		score = 0
		i = 0
		for tmpword1 in word1:
			for tmpword2 in word2:
				if tmpword1.pos() == tmpword2.pos() :
					#用path_base计算相似度
					try:
						pathscore = max(tmpword1.path_similarity(tmpword2),pathscore)
						WPscore = max(tmpword1.wup_similarity(tmpword2),Resnikscore)
						LCscore = max(tmpword1.lch_similarity(tmpword2),LCscore)
						JCscore = max(tmpword1.jcn_similarity(tmpword2,brown_ic),JCscore)
						Resnikscore = max(tmpword1.res_similarity(tmpword2,brown_ic),Resnikscore)
						Linscore = max(tmpword1.lin_similarity(tmpword2,brown_ic),Linscore)
					except Exception as e:
						continue
					finally:
						pass
		writeStr = []
		writeStr.append(str1+","+str2+","+str(pathscore)+"\n")
		writeStr.append(str1+","+str2+","+str(WPscore)+"\n")
		writeStr.append(str1+","+str2+","+str(LCscore)+"\n")
		writeStr.append(str1+","+str2+","+str(JCscore)+"\n")
		writeStr.append(str1+","+str2+","+str(Resnikscore)+"\n")
		writeStr.append(str1+","+str2+","+str(Linscore)+"\n")
		for j in range(6):
			outFile[j].write(writeStr[j])

def fileRead(fileName):
	inFile = codecs.open(fileName,'r','utf-8')
	line = inFile.readline()
	newList = []
	while line:
		line = line.strip()
		list = line.split(',')
		newList.append(list[2])
		line = inFile.readline()
	return newList

def wordnetFileRead():
	simData = []
	for i in range(6):
		simData.append(fileRead(rootPath+wnWritePathSet2[i]))
	return simData

def wordnetFileOpen():
	outwordnetSimilarity = []
	for i in range(6):
		outwordnetSimilarity.append(open(rootPath+wnWritePathSet2[i],"w"))
	return outwordnetSimilarity


def SpearmanRank():
	# result = open(rootPath+"combinedResult.csv","w")
	result = open(rootPath+"set2Result.csv","w")
	# result = open(rootPath+"set2Result.csv","w")
	trueData = fileRead(rootPath+'set2.csv')
	simData = wordnetFileRead()
	cosinData = fileRead(rootPath+"cosinSimilaritySet2.csv")
	googleData = fileRead(rootPath+"googleSimilaritySet2.csv")
	i=0
	print("cosin:")
	print(scipy.stats.stats.spearmanr(trueData, cosinData)[0])
	result.write("consinSimilarity,"+str(scipy.stats.stats.spearmanr(trueData, cosinData)[0])+"\n")
	result.write("googleSimilarity,"+str(scipy.stats.stats.spearmanr(trueData, googleData)[0])+"\n")
	while i<6:
		print(wnPath[i]+":")
		print(scipy.stats.stats.spearmanr(trueData, simData[i])[0])
		print("\n")
		result.write(wnPath[i]+","+str(scipy.stats.stats.spearmanr(trueData, simData[i])[0])+"\n")
		i += 1


def main():
	# # modelHuang = gensim.models.Word2Vec.load('E:\\HuangModel')
	# # outword2vec_Similarity = open("E:\\Homework1\\afterCompute\\word2vec_Similarity.csv","w")
	# # outcosinSimilarity = open(rootPath+"cosinSimilarity.csv","w")
	# # outcosinSimilarity = open(rootPath+"cosinSimilaritySet2.csv","w")
	# inFile = codecs.open("E:\\Homework1\\afterCompute\\set2.csv", 'r',"utf-8")
	# outwordnetSimilarity = wordnetFileOpen()
	# line = inFile.readline()
	# i = 0
	# while line:
	# 	i += 1
	# 	line = line.strip()
	# 	list = line.split(',')
	# 	# word2vec_Similarity(modelHuang,list[0],list[1],i,outcosinSimilarity)
	# 	# cosinSimilarity(modelHuang,list[0],list[1],outcosinSimilarity,i)
	# 	wordnetSimilarity(list[0],list[1],i,outwordnetSimilarity)
	# 	line = inFile.readline()
	# print("count",i)
	SpearmanRank()

if __name__ == '__main__':
		start = time.clock()
		main()
		end = time.clock()
		print ("process: %f s" % (end - start))
