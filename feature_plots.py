# Plots to be refined

import plotly.express as px
import plotly.subplots as sp
import pandas as pd
import numpy as np
data = pd.read_csv('https://raw.githubusercontent.com/scast26/cse-163-final/main/19332_Spotify_Songs.csv', encoding='unicode_escape', low_memory=False)
data['popularity'] = pd.to_numeric(data.popularity, errors='coerce')
data = data[data['popularity'] >= 80].sort_values('popularity')


def facetting_scatter_plot(data, n_cols=3, y='Features'):
    numeric_cols = data.select_dtypes('number').columns
    n_rows = -(-len(numeric_cols) // n_cols)  # math.ceil in a fast way, without import
    row_pos, col_pos = 1, 0
    fig = sp.make_subplots(rows=n_rows, cols=n_cols, subplot_titles=numeric_cols)

    for col in numeric_cols:
        # trace extracted from the fig
        trace = px.scatter(data, x=col, y=data['popularity'], trendline='ols', trendline_color_override='#DC143C')["data"]
        # auto selecting a position of the grid
        if col_pos == n_cols: row_pos += 1
        col_pos = col_pos + 1 if (col_pos < n_cols) else 1
        # adding trace to the grid
        fig.add_trace(trace[0], row=row_pos, col=col_pos)
        fig.add_trace(trace[1], row=row_pos, col=col_pos)
    return fig

fig = facetting_scatter_plot(data.select_dtypes(np.float64))

fig.update_layout(width=1000, height=800, title='Comparison of Song Features', title_x=0.5)
fig.show()
