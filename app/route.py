from flask import render_template

def hello_world():
    return "BDSE26 第五組!"

def index():
    title = "便捷台北 轉運動能"
    
    return render_template('index.html', title=title) 

def analysis():
    title = "便捷台北 轉運動能"
    return render_template('analysis.html', title=title) 

def model():
    title = "便捷台北 轉運動能"
    return render_template('model.html', title=title) 


def about():
    title = "便捷台北 轉運動能"
    return render_template('about.html', title=title)
