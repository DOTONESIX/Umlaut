# uMLaut

The uMLaut library simplifies model deployment and querying. It provides a single
access point for all of your organizations models and an interface to interact with them. Umlaut `models` can be as extensive as deep learning models or as simple as a reusable code block.

uMLaut offers...
- simple model lifecycle management
- easy model maintenance
- access to multiple versions of the same model
- business logic sharing
- a user interface with `MLflow`
- audit tracking history (roadmap)
- auto-deployed models that can be queried through an API (roadmap)

____
## Umlaut Class
A Python class to assist with saving and querying business logic.

- `track_model`: Converts a data science model or block of business logic into an uMLaut compatible `model`
- `query_model`: Queries a previously trained `model` and saves audit metadata
- `track_dataset (roadmap)`: Saves reporting datasets along with the initial query and underlying data that built it (roadmap)
- `audit_model (roadmap)`: Retrieve the results of a model run for a historic date
- `audit_dataset (roadmap)`: Retrieve a dataset as it was on a historic date

### Deploying models with Umlaut
Custom data science models or business logic can be deployed simply by running `umlaut.track_model()`. Ensure the model code block is in a Python `Class` and follow the example below.

```
class ExampleModel():
    """
    Example business logic that can be wrapped into a model.
    The class _must_ contain a 'predict' method.
    """
    def business_logic(self, revenue: int) -> bool:
        if revenue > 5:
            return True
        else:
            return False

    def predict(self, model_input: dict) -> bool:
        return self.business_logic(revenue=model_input.get("revenue"))


if __name__ == "__main__":
    """Saves the model to MLflow in an experiment run"""
    from core import Umlaut

    umlaut = Umlaut()
    umlaut.track_model(
        model=ExampleModel(),
        model_name="Quarterly Revenue",
        run_name="Update",
    )
```

This will push the latest changes of `ExampleModel()` to MLflow as a new model version. Navigate to the MLflow Tracking Server to find the latest push and associate it to the MLflow model.


### Querying models with Umlaut
Once a model is deployed in MLflow with `umlaut.track_model()`, it can be queried by calling `umlaut.query_model()`.

```
from core import Umlaut

umlaut = Umlaut()
result = umlaut.query_model(
    model_name="Quarterly Revenue",
    input_config={"revenue": 3},
    stage="Staging",
)
print(f"Revenue will{'' if result else ' not'} exceed target")
```

If we query the simple `Quarterly Revenue` example model with `revenue = 3`, the model will return `False` as the revenue does not exceed the target of 5.
