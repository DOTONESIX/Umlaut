if __name__ == "__main__":
    """Saves the model to MLflow in an experiment run"""
    import sys
    import os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from core import Umlaut

    umlaut = Umlaut()
    umlaut.query_model(
        model_name="Sales Target",
        run_name="Update",
        # code_path=
    )
