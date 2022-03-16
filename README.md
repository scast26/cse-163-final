# A Quantitative Analysis of Songs on Spotify

## Research Question 1: Do the songs with the most popular artists share a similar audio profile in terms of individual audio features? Does one audio feature seem to remain the most constant among these songs?

We decided to create plots to represent our findings using a new library of plotly. To reproduce these results, it is strongly recommended that you open up Visual Studio Code, a Jupyter notebook or use Datalore.JetBrains.com to access plot displays and have an interactive environment to use plotly to its fullest potential. After choosing an environment to explore our visual analysis follow the steps below to install the correct and sufficient libraries to explore our data. 

To start, download this project or clone it using:

```git clone ```

If using Visual Studio Code: Then open Git or GitBash (depending on your operating system) to install the necessary libraries:
Make sure to type these commands in separate lines.

```pip install plotly```

To check if plotly was installed correctly:

```pip list | grep plotly```

```pip show plotly```

Install the rest:

```pip install --upgrade --no-deps statsmodels```

```pip install scipy```

```pip install patsy```


Every file with the code to plot these plots contain comments explaining each step of the process and purpose of each line of code for readers to clearly follow. The file corresponding to our first research question is titled “question_1.py” that includes these imports necessary for running the file. 
For the plot file labeled "question_1.py" the following imports are included:

```ruby
import plotly.express as px
import plotly.subplots as sp
import pandas as pd
import numpy as np
```

The title of each plot function corresponds to an image of that same name that contains solely a capture of what the correct plot will output. 


## Research Question 2: Will Spotify recommend a list of popular songs if we pass in audio feature parameters that are representative of already popular songs?


## Research Question 3: Can we predict a song’s popularity score based on its song’s audio features?
