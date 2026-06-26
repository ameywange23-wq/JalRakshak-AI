def predict_risk(ph, tds, turbidity, do):

    if (
        tds > 700 or
        turbidity > 8 or
        ph < 6 or
        ph > 8.5
    ):
        return "High Risk"

    elif (
        tds > 400 or
        turbidity > 4
    ):
        return "Moderate Risk"

    else:
        return "Safe"
