import pandas as pd
import plotly.graph_objects as go
from flask import Flask, render_template
from plotly.offline import plot

import config

app = Flask(__name__)

# data = pd.read_excel("data.xlsx")
data = pd.read_csv("data.csv")


@app.route('/')
def index():
    course = data['Course'][0]
    average = data['Average'][0]

    return render_template('gauge.html',
                           selected_average=average,
                           selected_course=course,
                           average_dict=data.to_dict(),
                           fig_div=get_div(average, course))


@app.route('/index_update/<course>')
def index_update(course):
    average = data[data["Course"] == course]["Average"]
    return render_template('gauge.html',
                           selected_average=average,
                           selected_course=course,
                           average_dict=data.to_dict(),
                           fig_div=get_div(average, course))


def get_div(average, course):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=float(average),
        number={'suffix': "%"},
        domain={'x': [0, 1], 'y': [0, 1]},

        title={'text': "Course : {}".format(course.title()), 'font': {'size': 24}},
        #     delta = {'reference': 400, 'increasing': {'color': "RebeccaPurple"}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
        }))

    # fig.show()
    return plot(fig, output_type='div')


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=True)
