import operator
class SimilarityCalculator:
    similarityVectors = {}
    similarItemsVectors={}
    def calculateSimilarity(self, tfVector1, tfVector2):
        sum1 = 0
        sum2 = 0
        for word in tfVector1.keys():
            sum1 += tfVector1[word]**2
        for word in tfVector2.keys():
            sum2 += tfVector2[word]**2
        if sum1 == 0 or sum2 == 0:
            return 0

        denominator = (sum1*sum2)**0.5

        nominator = 0
        for word in tfVector1.keys():
            if word in tfVector2.keys():
                nominator += tfVector1[word]*tfVector2[word]

        print(nominator/denominator)
        return nominator/denominator

    def setSimilarity(self, id, similarityVector):
        self.similarityVectors[id] = dict(sorted(similarityVector.items(), key=operator.itemgetter(1), reverse=True))
    def setSimilarItems(self, id):
        self.similarItemsVectors[id] = dict(sorted(self.similarityVectors[id].items(), key=operator.itemgetter(1), reverse=True)[:30])