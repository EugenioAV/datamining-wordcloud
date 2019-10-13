import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def read_data(file_path='input/text.txt'):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    return text


def draw_word_cloud(text):
    stopwords = set(STOPWORDS)

    word_cloud = WordCloud(max_font_size=70, background_color="white", max_words=50, stopwords=stopwords)
    word_cloud.generate(text)

    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    word_cloud.to_file(os.path.join(d, "output/word_cloud.png"))

    plt.figure()
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    data = read_data()
    draw_word_cloud(data)
