import os
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stop_words = stopwords.words('english')
pathnames = ['./data_stage_one/'+wor+'/' for wor in
            ['development_set','training_set','test_set']]
docs=[]
for path in pathnames:
    for filename in os.listdir(path):
        with open(path+filename,'r') as inp:
            f=inp.read()
            words=word_tokenize(f)
            words = [w.lower() for w in words]
            noPunc = [w.translate(None,string.punctuation)
                      for w in words]
            noEmp = [w for w in noPunc if w.isalpha()]
            noStop = [w for w in noEmp if not w
                      in stop_words]
            stemmed = [porter.stem(w) for w in noStop]
        docs.append(stemmed)
print len(docs)

################### LDA using Gensim #######################
#from collections import defaultdict
from gensim import corpora, models, similarities
import tempfile
TMP = tempfile.gettempdir()
# frequency = defaultdict(int)
# for line in docs:
#     for token in line:
#         frequency[token] += 1
dcy = corpora.Dictionary(docs)
dcy.save(os.path.join(TMP,'cong.dict'))
corpus = [dcy.doc2bow(text) for text in docs]
corpora.MmCorpus.serialize(os.path.join
                           (TMP,'congCorp.mm'),corpus)
lda = models.LdaModel(corpus, id2word=dcy,num_topics=10)
lda.print_topics(10)


       
            
            
