# -*- coding: utf-8 -*-
"""
@File  : run.py
@Author: SangYu
@Date  : 2019/4/9 12:12
@Desc  : 
"""
from flask import Flask, render_template, request
import random
from fastTextClassifier import sentence_input

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/input", methods=["GET", "POST"])
def input():
    if request.method == "POST":
        input_text = request.form["input_text"]
        result = sentence_input(input_text)
        return render_template("input.html", input_text=input_text, result=result)
    return render_template("input.html", input_text="", result="")


def compute_emotion(input_text):
    emotion_list = ["正向", "中立", "负向"]
    return emotion_list[random.randrange(0, len(emotion_list))]


if __name__ == '__main__':
    app.run(debug=True)
