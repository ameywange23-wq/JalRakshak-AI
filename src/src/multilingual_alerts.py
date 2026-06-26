def generate_alert(risk):

    if risk == "High Risk":

        return {
            "English": "Water quality is unsafe.",
            "Hindi": "पानी की गुणवत्ता असुरक्षित है।",
            "Marathi": "पाण्याची गुणवत्ता असुरक्षित आहे."
        }

    elif risk == "Moderate Risk":

        return {
            "English": "Water quality needs monitoring.",
            "Hindi": "पानी की गुणवत्ता पर निगरानी रखें।",
            "Marathi": "पाण्याच्या गुणवत्तेवर लक्ष ठेवा."
        }

    return {
        "English": "Water quality is safe.",
        "Hindi": "पानी की गुणवत्ता सुरक्षित है।",
        "Marathi": "पाण्याची गुणवत्ता सुरक्षित आहे."
    }
