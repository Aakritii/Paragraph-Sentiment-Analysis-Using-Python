import re
from textblob import TextBlob

class ParaClient(object):
    #Clean the unwanted words from the paragraph
    def clean_para(self, para):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", para).split())

    #This function is to get the polarity of the words
    def get_para_sentiment(self, para):
        analysis = TextBlob(self.clean_para(para))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity < 0:
            return 'negative'
        else:
            return 'neutral'
        
    #This function is to return the sentiments of each words
    def get_Sentiments(self, query):
        paragraph = []

        for p in query.split():
            parsed_para = {}
            parsed_para['text'] = p
            parsed_para['sentiment'] = self.get_para_sentiment(p)

            if len(p) > 0:
                if parsed_para not in paragraph:
                    paragraph.append(parsed_para)
            else:
                paragraph.append(parsed_para)
        return paragraph

def main():
    #Creating Object of ParaClient class
    api = ParaClient()
    
    #paragraph by User
    query = input()
    
    #Call the get_Sentiments
    try:
        paragraph = api.get_Sentiments(query)
        
        #insert all positive words in the pPara list
        pPara = [para for para in paragraph if para['sentiment'] == 'positive']
        
        print("Positive sentiments percentage for paragraph: {0:.2f}%".format(100*len(pPara)/len(paragraph)))
        
        #insert all negative words in the nPara list
        nPara = [para for para in paragraph if para['sentiment'] == 'negative']
        print("Negative sentiments percentage for paragraph: {0:.2f}%".format(100*len(nPara)/len(paragraph)))
        
        #insert all negative words in the nPara list
        zPara = [para for para in paragraph if para['sentiment'] == 'neutral']
        print("Negative sentiments percentage for paragraph: {0:.2f}%".format(100*len(zPara)/len(paragraph)))


        print("\n\nPositive Sentiments:")
        for para in pPara[:10]:
            print(para['text'])

        print("\n\nNegative Sentiments:")
        for para in nPara[:10]:
            print(para['text'])
            
        print("\n\nNeutral Sentiments:")
        for para in zPara[:10]:
            print(para['text'])
    except:
        print("Error : " + str("Exception Occured..\nEnter few more words in the paragraph..."))

if __name__ == "__main__":
    main()
