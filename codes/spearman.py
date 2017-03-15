import codecs
import string
import gensim
import time
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
semcor_ic = wordnet_ic.ic('ic-semcor.dat')
import scipy
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
def main():
	# result = open(rootPath+"combinedResult.csv","w")
	rootPath = 'E:\\Homework1\\afterCompute\\'
	# result = open(rootPath+"set2Result.csv","w")
	# result = open(rootPath+"set2Result.csv","w")
	trueData = fileRead(rootPath+'set2.csv')
	# simData = wordnetFileRead()
	# cosinData = fileRead(rootPath+"cosinSimilaritySet2.csv")
	googleData = fileRead("C:\\Users\\Aaron_Huang\\Desktop\\set2Predict.csv")
	print(scipy.stats.stats.spearmanr(trueData, googleData)[0])
	# result.write("consinSimilarity,"+str(scipy.stats.stats.spearmanr(trueData, cosinData)[0])+"\n")
	# result.write("googleSimilarity,"+str(scipy.stats.stats.spearmanr(trueData, googleData)[0])+"\n")import codecs

if __name__ == '__main__':
		main()