from lab6_intelligent_search.bayesian.disease_network import inference


def diagnose():
    result = inference.query(
        variables=['Disease'],
        evidence={'Fever': 1}
    )

    return result