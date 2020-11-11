import re
import operator
class FrequencyCounter:
    frequencyVectors = {}
    finalKeywords = set({})
# )
    def countNSetFrequency(self,id,string,keywordSet):
        frequency = {}
        str_list = string.split()
        for word in keywordSet:
            frequency[word] = str_list.count(word)
            if frequency[word]>4:
                self.finalKeywords.add(word)

        self.frequencyVectors[str(id)] = dict(sorted(frequency.items(),key=operator.itemgetter(1),reverse=True))
        print("id",id, self.frequencyVectors[str(id)])

    def getFrequencyVector(self, id):
        return self.frequencyVectors[id]



