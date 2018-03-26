import os
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stop_words = stopwords.words('english')
stop_words += ['mr','would','say','lt', 'p', 'gt', 'amp', 'nbsp',
               'bill','speaker','us','going','act','gentleman',
              'gentlewoman','chairman','nay','yea','thank']
pathnames = ['./convote_v1.1/data_stage_one/'+wor+'/' for 
             wor in ['development_set','training_set']]
#pathnames = ['./data_stage_one/training_set/']
docs,docLen=[],0
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
            stemmed = [w for w in stemmed if not w
                      in stop_words]
        docLen+=len(stemmed)
        docs.append(stemmed)
        #docs.append(noStop)
l = len(docs)
print ("Total Number of documents = %d"%l)
print("Average words per document = %d"%(docLen/l))

#################################################################
from gensim import corpora, models, similarities
import tempfile
TMP = tempfile.gettempdir()
dcy = corpora.Dictionary(docs)
print("Total vocabulary size = %d"%len(dcy))
dcy.save(os.path.join(TMP,'cong.dict'))
corpus = [dcy.doc2bow(text) for text in docs]
corpora.MmCorpus.serialize(os.path.join
                           (TMP,'congCorp.mm'),corpus)
#for c in corpus[:10]:
#    print(c)
tfidf = models.TfidfModel(corpus, normalize=True)
tfidf_corpus = tfidf[corpus]
tfidf_corpus = corpus
lda = models.LdaModel(tfidf_corpus, id2word=dcy, 
                      num_topics=10)
lda.print_topics(3,10)

