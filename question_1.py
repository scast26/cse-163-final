# Plots to be refined

import plotly.express as px
import plotly.subplots as sp
import pandas as pd
import numpy as np


DATA = 'song_dataset.csv'


def filter_data(data):
    """
    This function takes a DataFrame containing songs and their audio
    features, and returns a DataFrame which filters the original
    DataFrame down into songs with a popularity column of 80 or higher.
    """
    data = pd.read_csv(data, encoding='unicode_escape', low_memory=False)
    data['popularity'] = pd.to_numeric(data.popularity, errors='coerce')
    df = data[data['popularity'] >= 80]
    df = df[['popularity', 'name', 'danceability', 'energy', 'key', 'loudness',
            'mode', 'speechiness', 'acousticness', 'instrumentalness',
             'liveness', 'valence', 'tempo']]
    return df


def facetting_scatter_plot(data, n_cols=3, y='Features'):
    numeric_cols = data.select_dtypes('number').columns
    # math.ceil in a fast way, without import
    n_rows = -(-len(numeric_cols) // n_cols)
    row_pos, col_pos = 1, 0
    fig = sp.make_subplots(rows=n_rows, cols=n_cols,
                           subplot_titles=numeric_cols)

    for col in numeric_cols:
        # trace extracted from the fig
        trace = px.scatter(
            data, x=col, y=data['popularity'], trendline='ols',
            trendline_color_override='#DC143C')["data"]
        # auto selecting a position of the grid
        if col_pos == n_cols:
            row_pos += 1
        col_pos = col_pos + 1 if (col_pos < n_cols) else 1
        # adding trace to the grid
        fig.add_trace(trace[0], row=row_pos, col=col_pos)
        fig.add_trace(trace[1], row=row_pos, col=col_pos)
    return fig


def show_box_plots(data):
    """
    This function takes a DataFrame containing songs and their audio
    features as a parameter. It returns a plot that shows the box and whisker
    plots of all of the features whose values range from zero to one.
    """
    df = data
    df = df.melt(id_vars=["popularity", "name"], var_name="feature")
    filtered = df[(df['feature'] != 'tempo') & (df['feature'] != 'key')
                  & (df['feature'] != 'loudness') & (df['feature'] != 'mode')]
    box_plot = px.box(filtered, x='feature', y='value', color='feature',
                      title='Examining the Spread of Each Audio Feature')
    return box_plot


def main():
    df = filter_data(DATA)

    fig = facetting_scatter_plot(df.select_dtypes(np.float64))
    fig.update_layout(width=1000, height=800,
                      title='Comparison of Song Features', title_x=0.5)
    fig.show()

    box_plot = show_box_plots(df)
    box_plot.show()


if __name__ == '__main__':
    main()
