# -*- coding: utf-8 -*-
"""
@File  : fastTextClassifier.py
@Author: SangYu
@Date  : 2019/4/11 11:38
@Desc  : fastText分类器
"""
import os
os.system("pip install fasttext-0.8.22-cp36-cp36m-win_amd64.whl")
import jieba
import fTModel.FastText as ff


def load_stop_words():
    """
    加载停用词典
    :return: 停用词表
    """
    stop_words_path = "Data/sentiment-dict/stopwords.dic"
    return set([line.strip() for line in open(stop_words_path, "r", encoding="utf-8").readlines()])


def load_punctuation_words():
    """
    加载标点符号词典
    :return: 标点符号词表
    """
    punctuation_words_path = "Data/sentiment-dict/punctuations.dic"
    return set([line.strip() for line in open(punctuation_words_path, "r", encoding="utf-8").readlines()])


def load_negative_words():
    """
    加载消极词典
    :return: 消极词表
    """
    negative_words_path = "Data/sentiment-dict/sentiment-words/negative_word.txt"
    return set([line.strip() for line in open(negative_words_path, "r", encoding="utf-8").readlines()])


def load_negative_emoticons():
    """
    加载消极表情符
    :return: 消极表情符
    """
    negative_emoticons_path = "Data/sentiment-dict/sentiment-words/negative_emoticon.txt"
    return set([line.strip() for line in open(negative_emoticons_path, "r", encoding="utf-8").readlines()])


def load_positive_words():
    """
    加载积极词典
    :return: 积极词表
    """
    positive_words_path = "Data/sentiment-dict/sentiment-words/positive_word.txt"
    return set([line.strip() for line in open(positive_words_path, "r", encoding="utf-8").readlines()])


def load_positive_emoticons():
    """
    加载积极表情符
    :return: 积极表情符
    """
    positive_emoticons_path = "Data/sentiment-dict/sentiment-words/positive_emoticon.txt"
    return set([line.strip() for line in open(positive_emoticons_path, "r", encoding="utf-8").readlines()])

def sentence_input(sentence):
    classifier = ff.load_model("fTModel/model/train")
    positive_emoticons = load_positive_emoticons()
    negative_emoticons = load_negative_emoticons()
    punctuation_words = load_punctuation_words()
    stop_words = load_stop_words()
    positive_words = load_positive_words()
    negative_words = load_negative_words()
    print(sentence)
    # 识别其中的表情符，并替换成相应的字符
    for p_word in positive_emoticons:
        if p_word in sentence:
            sentence = sentence.replace(p_word, " 积极 ")
    for p_word in negative_emoticons:
        if p_word in sentence:
            sentence = sentence.replace(p_word, " 消极 ")
    print(sentence)
    # 识别其中的标点符号，替换成空格
    for p_word in punctuation_words:
        if p_word in sentence:
            sentence = sentence.replace(p_word, " ")
    print(sentence)
    # 对句子进行分词,去除停用词，识别情感词，并为情感词打上特殊标记
    line = sentence.replace("蒙牛", "")
    seg_line = [seg for seg in jieba.cut(line)]
    print(seg_line)
    add_str = ""
    for word in seg_line:
        if word not in stop_words and word != "" and " " not in word:
            if word in positive_words:
                add_str += "# " + word + " # "
            elif word in negative_words:
                add_str += "* " + word + " * "
            else:
                add_str += word + " "
    print(add_str.strip())
    label = classifier.predict(add_str.strip())
    print(label)
    return label

if __name__ == '__main__':
    sentence_input("真是个良心企业")