class ExampleModel():
    """Example business logic that can be wrapped into a model.
       The class _must_ contain a 'predict' method."""
    def business_logic(self, record: dict) -> bool:
        if record.get("revenue") > 5:
            return True
        else:
            return False

    def predict(self, model_input: dict) -> bool:
        return self.business_logic(model_input)


if __name__ == "__main__":
    """Saves the model to MLflow in an experiment run"""
    import sys
    import os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from core import Umlaut

    umlaut = Umlaut()
    umlaut.track_model(
        model=ExampleModel,
        model_name="Quarterly Revenue",
        run_name="Update",
        # code_path=
    )
