import re

class EmojiRemover:
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons 
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs 
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols 
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS) 
                               "]+", flags=re.VERBOSE)

    def removeEmoji(self, string):
        result = "null"
        # if type(string)==string:
        #     print("string is string")
        try:
            return self.emoji_pattern.sub(r'', string)
        except TypeError:
            print("type error")
            return ""

    def getEmojilessList(self, reviewList):
        emojilessList = []
        for num in range(0, len(reviewList)):
            emojilessList.append(self.removeEmoji(reviewList[num]))

        return emojilessList