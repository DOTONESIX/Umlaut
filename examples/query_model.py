if __name__ == "__main__":
    from umlaut.core import Umlaut

    umlaut = Umlaut()
    result = umlaut.query_model(
        model_name="Revenue Forecast",
        input_config={"revenue": 50000},
        stage="Staging"
    )
    print(result)
