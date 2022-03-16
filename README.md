# A Quantitative Analysis of Songs on Spotify

## Research Question 1: Do the songs with the most popular artists share a similar audio profile in terms of individual audio features? Does one audio feature seem to remain the most constant among these songs?

We decided to create plots to represent our findings using a new library of plotly. To reproduce these results, it is strongly recommended that you open up Visual Studio Code, a Jupyter notebook or use Datalore.JetBrains.com to access plot displays and have an interactive environment to use plotly to its fullest potential. After choosing an environment to explore our visual analysis follow the steps below to install the correct and sufficient libraries to explore our data. 

To start, download this project or clone it using:

```git clone https://github.com/scast26/cse-163-final.git```

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


Every file with the code to plot these plots contain comments explaining each step of the process and purpose of each line of code for readers to clearly follow. The file corresponding to our first research question is titled ```question_1.py```that includes these imports necessary for running the file. 
For the plot file labeled ```question_1.py```the following imports are included:

```ruby
import plotly.express as px
import plotly.subplots as sp
import pandas as pd
import numpy as np
```
With these imports in place, the file is ready to run. When running the final, three plots (one box plot, and two unique scatter plots) will be generated and displayed in separate tabs. The box plot and scatter plot with subplots both are created with inclusion of all significant audio features in our dataset. The other scatter plot created references the columns of ```danceability```, ```popularity```, ```energy```, and ```speechiness``` to showcase a more narrow approach to our data analysis.

The title of each plot function corresponds to an image of that same name that contains solely a capture of what the correct plot will output. 


## Research Question 2: Will Spotify recommend a list of popular songs if we pass in audio feature parameters that are representative of already popular songs?
The ability to reproduce the results of this research question can be done by running `question_2.py`.
To run the second research question, you will need to import requests, base64, json, and numpy. Python comes with the base64 module, and the JSON interpreter, so there is no need to install them.

Numpy should already have been downloaded from the previous research question. To install requests, run the following line in your terminal:

`python -m pip install requests`

In addition to these, the filter_data and show_box_plots functions from "question_1.py" have also been imported. The filter_data function preps the data for the API calls, and show_box_plots renders the same plot as the first question because it is especially relevant in this question.

The imports in "question_2.py" should be:
```ruby
import requests
import base64
import json
import numpy as np
from question_1 import filter_data, show_box_plots
```

Once these imports are properly in place, you can run the file. When you run the file, there should be 8 new files that appear in the current directory. 4 of them will be .json files, and the other 4 will be .txt files. There is one .json and one .txt file for each audio feature that was examined. It is currently defaulted at instrumentalness, speechiness, danceability, and liveness, as these are the 4 audio features with the least amount of spread. The .json files contain 20 recommendations based on the audio feature provided in raw JSON. The .txt file parses the .json file, and provides you with a list of recommendations, as well as their popularity score. At the end of the file, the average popularity score is computed.

You will likely find that songs by popular artists have a surprisingly low popularity score. As noted in the report, this context of popularity is associated with the popularity of the actual song (number of streams).

## Research Question 3: Can we predict a song’s popularity score based on its song’s audio features?
To (approximately) reproduce our results, you will need to run `question_3.py`. 

To properly run this file, you will need to install SciKit-Learn, Tensorflow, Keras, and Pandas, though this should already be installed from `question_1.py`.

To install the necessary libraries, run the following lines in your terminal:

`pip install -U scikit-learn`

`pip install tensorflow`
(note, the newest version of Python that Tensorflow is compatible with is v3.7)

`pip install keras`

The imports for this file should look like this:
```ruby
from sklearn.neural_network import MLPClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
```
Once this imports are in place, you can run the file. It will train and fit all three models; then it will test them and print out the mean squared error for each of them. The results will be different every time as the training data is randomzied and models will consequeny act differently. It will print the name of the model and then the MSE. 

Please note that while we ran the keras model with 300 epochs you can run it with as many as you wish if 300 takes too long. This will be on line 56 with "model.fit(inputs_train, labels_train, epochs=300, batch_size=10)". You can change epochs=x.
