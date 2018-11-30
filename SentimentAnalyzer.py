import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EmotionOptions, SentimentOptions

class SentimentAnalyzer():

    def  __init__(self):
        self.naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
        version='2018-09-21',
        iam_apikey='z22B_pFOjawl36w4CwyWGRs55jVnXE4y464VlyY7o-67',
        url='https://gateway-syd.watsonplatform.net/natural-language-understanding/api')
        self.def_features = Features(
            sentiment = SentimentOptions(
                document=True),
            emotion = EmotionOptions(
                document=True))
    def sentiment_score (self, lyrics : str):
        """Take lyrics text file in entry andgive a dict of sentiment/emotion analysis score"""

        response = self.naturalLanguageUnderstanding.analyze(
            text=lyrics,
            features=self.def_features).get_result()
        emotion = response.copy()
        sentiment = response.copy()
        emotion = emotion["emotion"]["document"]["emotion"]
        sentiment = sentiment["sentiment"]["document"]
        del sentiment["label"]
        sentiment["sentiment"] = sentiment.pop("score")
        emotion.update(sentiment)

        return emotion
    def sentiment_score_raw (self, lyrics : str):
        """Take lyrics text file in entry andgive a dict of sentiment/emotion analysis score"""

        response = self.naturalLanguageUnderstanding.analyze(
            text=lyrics,
            features=self.def_features).get_result()
        
        return response
