from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from django.conf import settings


class HomeView(APIView):

    def get_text_obj(self):
        text_data = open(settings.BASE_DIR.joinpath('file_storage/words_text_file.txt'), "r")
        first_line = True
        text_obj = {}
        lines = []
        for line in text_data:
            if first_line:
                text_obj['title'] = line.split(" ")
                first_line = False
            else:
                lines.append(line.split(" "))
        text_obj['lines'] = lines
        return text_obj

    def get_words_and_word_data(self):
        word_data_df = pd.read_csv(settings.BASE_DIR.joinpath('file_storage/word_data.csv'), ";", encoding='utf-8')
        word_data_df = word_data_df.fillna('')
        words = list(word_data_df['word'])
        data = {}
        i = 0
        for word in words:
            data[word] = list(word_data_df.iloc[i])
            i += 1

        return words, data

    def get(self, request):
        text_obj = self.get_text_obj()
        words, data = self.get_words_and_word_data()
        return Response({'words': words, 'word_data': data, 'text_obj': text_obj})
