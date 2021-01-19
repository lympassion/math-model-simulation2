from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS


def get_data(list):
    simple_data = []
    for single in list:
        product_name = single[6]
        star = single[8]
        review = str(single[13])
        date = datetime.strptime(single[15], '%m/%d/%Y')
        detail = {'name': product_name, 'star': star, 'date': date, 'review': review}
        if (single[12] == 'Y'):  # 过滤未交易的订单
            simple_data.append(detail)
    return simple_data


hairdryer_data = get_data(pd.read_excel("../dataset/hairdryer_clean.xlsx", sheet_name="Sheet1").values)
pacifier_data = get_data(pd.read_excel("../dataset/pacifier_clean.xlsx", sheet_name="Sheet1").values)
microwave_data = get_data(pd.read_excel("../dataset/microwave_clean.xlsx", sheet_name="Sheet1").values)


# 词云
def ciyun(data, path, name):
    stopwords = set(STOPWORDS)
    useless_words = ['hair', 'dryer']
    for i in useless_words:
        stopwords.add(i)
    string = ''
    for i in data:
        string += i['review'] + ' '
    wordcloud = WordCloud(background_color="white", stopwords=stopwords, width=1000, height=860, margin=2).generate(string)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(path + name)
    plt.show()


# 生成对应的词云
path = '../images/'
ciyun(hairdryer_data, path, 'hairdryer_data')
ciyun(pacifier_data, path, 'pacifier_data')
ciyun(microwave_data, path, 'microwave_data')


def calc_star(data, path, name):
    labels = ['Five star', 'Four star', 'Three star', 'Two star', 'One star']
    res = [0, 0, 0, 0, 0]
    for i in data:
        star = i['star']
        if (star == 5):
            res[0] += 1
        elif (star == 4):
            res[1] += 1
        elif (star == 3):
            res[2] += 1
        elif (star == 2):
            res[3] += 1
        else:
            res[4] += 1
    fig = plt.figure()
    plt.pie(res, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
    plt.title("Pie-figure")
    plt.savefig(path + name + '_pie')
    plt.show()


calc_star(hairdryer_data, path, 'hairdryer_data')
calc_star(pacifier_data, path, 'pacifier_data')
calc_star(microwave_data, path, 'microwave_data')
