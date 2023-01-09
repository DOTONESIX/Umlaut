class ExampleModel():
    """Example business logic"""
    def business_logic(self, revenue: int) -> bool:
        if revenue > 100000:
            return True
        else:
            return False

    def predict(self, model_input: dict) -> bool:
        return self.business_logic(revenue=model_input.get("revenue"))


if __name__ == "__main__":
    from umlaut.core import Umlaut

    umlaut = Umlaut()
    umlaut.track_model(
        model=ExampleModel(),
        model_name="Revenue Forecast",
        run_name="Update"
    )
