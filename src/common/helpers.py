# Helper Functions
def save_model(model, algorithm: str, experiment: str) -> None:

    today = datetime.today().strftime("%Y-%m-%d")
    
    path = os.path.join(
        os.path.dirname(os.path.dirname(os.getcwd())),
        'models',
        'genre_classification',
        algorithm,
        f'{experiment}_{today}_{algorithm}.pkl')

    print("Saving Model:\t{path}")
    joblib.dump(model, path)