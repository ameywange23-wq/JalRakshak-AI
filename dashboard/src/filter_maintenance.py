def recommend_maintenance(tds, turbidity):

    recommendations = []

    if tds > 600:
        recommendations.append(
            "Replace activated carbon filter"
        )

    if turbidity > 5:
        recommendations.append(
            "Clean sand filter"
        )

    if len(recommendations) == 0:
        recommendations.append(
            "System operating normally"
        )

    return recommendations
