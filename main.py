import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS


def read_data(file_path='input/text.txt'):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    return text


def get_mask(d, file_path='input/cloud_mask.png'):
    return np.array(Image.open(os.path.join(d, file_path)))


def draw_word_cloud(text):
    stopwords = set(STOPWORDS)
    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    cloud_mask = get_mask(d)

    word_cloud = WordCloud(background_color="white", max_font_size=500, max_words=100,
                           mask=cloud_mask, stopwords=stopwords)
    word_cloud.generate(text)
    word_cloud.to_file(os.path.join(d, "output/word_cloud.png"))

    plt.figure()
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    data = read_data()
    draw_word_cloud(data)
