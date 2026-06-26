import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_tds():

    days = [1, 2, 3, 4, 5]

    tds = [300, 320, 350, 370, 400]

    model = LinearRegression()

    X = pd.DataFrame(days)

    model.fit(X, tds)

    future_day = pd.DataFrame([6])

    prediction = model.predict(
        future_day
    )

    return round(
        prediction[0],
        2
    )
