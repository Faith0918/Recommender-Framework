from rake_nltk import Rake


class RakeKeywordManager:
    r = Rake()

    keyVectorSet = set()


    def getKeywords(self, string):
        self.r.extract_keywords_from_text(string)
        return self.r.get_ranked_phrases()

    def selectKeywords(selfself, keywordsList):
        selectedKeywordsList = []
        for keyword in keywordsList:
            words = keyword.split()
            if len(words)==1 and len(keyword)>3:
                selectedKeywordsList.append(keyword)
                # if len(words) == 1:
                #     selectedKeywordsList.append(keyword)
                # if len(words) == 2 and len(words[0])>3 and len(words[1])>3:
                #     selectedKeywordsList.append(words[0])
                #     selectedKeywordsList.append(words[1])
                # if len(words) == 3 and len(words[0])>2 and len(words[1])>2 and len(words[2])>2:
                #     selectedKeywordsList.append(words[0])
                #     selectedKeywordsList.append(words[1])
                #     selectedKeywordsList.append(words[2])
        return selectedKeywordsList

