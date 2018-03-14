
from django.views.generic import TemplateView
import plotly.offline as py
import plotly.graph_objs as go
import random
import numpy as np
import pandas as pd


class Graph2(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Graph2, self).get_context_data(**kwargs)



        l = []
        y = []
        data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
        # Setting colors for plot.
        N = 53
        c = ['hsl(' + str(h) + ',50%' + ',50%)' for h in np.linspace(0, 360, N)]

        for i in range(int(N)):
            y.append((2000 + i))
            trace0 = go.Scatter(
                x=data['rank'],
                y=data['pop'] + (i * 1000000),
                mode='markers',
                marker=dict(size=14,
                            line=dict(width=1),
                            color=c[i],
                            opacity=0.3
                            ), name=y[i],
                text=data['state'])  # The hover text goes here...
            l.append(trace0);

        layout = go.Layout(
            title='Stats of USA States',
            hovermode='closest',
            xaxis=dict(
                title='Pop',
                ticklen=5,
                zeroline=False,
                gridwidth=2,
            ),
            yaxis=dict(
                title='Rank',
                ticklen=5,
                gridwidth=2,
            ),
            showlegend=False
        )
        fig = go.Figure(data=l, layout=layout)
        div=py.plot(fig, auto_open=False, output_type='div')


        context['graph2'] = div

        return context