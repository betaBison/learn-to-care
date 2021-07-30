# learn-to-care

Example code to begin diving into how you might create an algorithm that
"learns" the best personalized healthcare for patients.

## Installation

1. Clone this repository:  
   ``` git clone git@github.com:betaBison/learn-to-care.git```
2. Install dependencies:  
   ``` pip install -r requirements.txt```


## Examples
1. COVID-19 Reported Patient Impact and Hospital Capacity by State Timeseries.
Can download [here](https://dev.socrata.com/foundry/healthdata.gov/g62h-syeh).
See [HealthData.gov](HealthData.gov) for more datasets.

   Run instructions: ```python covid.py```

   ![covid deaths](https://github.com/betaBison/learn-to-care/blob/main/docs/img/deaths.png?raw=true)

2. Heart failure prediction. Can download
[here](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data).
See [Kaggle.com](https://www.kaggle.com/search?q=healthcare+tag%3A%22healthcare%22)
for more datasets.

   Run instructions: ```python heart.py```

   ![heart disease](https://github.com/betaBison/learn-to-care/blob/main/docs/img/heart.png?raw=true)

3. Managing Ehlers Danlos syndrone pain through therapy. Can download
[here](https://digitalcollections.cuanschutz.edu/work/ns/05cea025-a2f4-4f29-9db5-8e84089d1d59).

   Run instructions: ```python eds.py```

   ![EDS therapy use](https://github.com/betaBison/learn-to-care/blob/main/docs/img/therapy.png?raw=true)
