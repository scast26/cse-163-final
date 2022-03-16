

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


def scatter_plot(data, num_cols=3):
    """
    This function takes a DataFrame containing songs and their audio
    features as a parameter as well as a number to determine how many
    plots will be plotting in a single row. This returns many scatterplot
    subplots that compare the presence and value of audio featues in
    songs with a popularity score of 80 or above.
    """
    numeric_columns = data.select_dtypes('number').columns
    # Calculate grid for plots
    num_rows = -(-len(numeric_columns) // num_cols)
    row_position, col_position = 1, 0
    fig = sp.make_subplots(rows=num_rows, cols=num_cols,
                           subplot_titles=numeric_columns)

    for column in numeric_columns:
        # Extracting trace from previously defined fig
        trace = px.scatter(
            data, x=column, y=data['popularity'], trendline='ols')["data"]
        # Selecting a position of the grid
        if col_position == num_cols:
            row_position += 1
        col_position = col_position + 1 if (col_position < num_cols) else 1
        # Adding each trace to fig
        fig.add_trace(trace[0], row=row_position, col=col_position)
        fig.add_trace(trace[1], row=row_position, col=col_position)
    return fig


def size_scatter(data):
    """
    This function takes a DataFrame containing songs and their audio
    features as a parameter. This returns a colorful and size
    senstiive scatterplot that compares the ratio of the values of
    danceability to the values of energy with the size of each point
    measuring the value of speechiness of a particular song with a
    popularity score of 80 or above.
    """
    fig = px.scatter(data, x='danceability', y='energy', size='speechiness',
                     color='popularity', log_x=True, size_max=60)
    fig.show()


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

    fig = scatter_plot(df.select_dtypes(np.float64))
    fig.update_layout(width=1000, height=800,
                      title='Comparison of Song Features', title_x=0.5)
    fig.show()

    size_scatter(df)

    box_plot = show_box_plots(df)
    box_plot.show()


if __name__ == '__main__':
    main()
