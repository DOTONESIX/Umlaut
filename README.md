# uMLaut

The uMLaut library simplifies model deployment and querying. It provides a single
access point for all of your organizations models and an interface to interact with all of them in the same way. Umlaut `models` can be as extensive as deep learning models or as simple as a reusable code block.

- Simple model lifecycle management
- Easily maintain and access multiple versions of the same model
- Quickly share business logic in reusable modules
- User interface with `MLflow`
- Audit tracking history (roadmap)
- Auto-deployed models that can be queried through an API (roadmap)

____
## Umlaut Class
A Python class to assist with saving and querying business logic.

- `track_model`: Converts a block of business logic into an Umlaut compatible `model`
- `query_model`: Queries a previously trained `model` and saves audit metadata
- `track_dataset`: Saves reporting datasets along with the initial query and underlying data that built it (roadmap)
- `audit_model (roadmap)`: Retrieve the results of a model run for a historic date
- `audit_dataset (roadmap)`: Retrieve a dataset as it was on a historic date

### Developing models with Umlaut
Custom `models` can be saved from any repository. Ensure the code block is in a Python `Class` and follow the example below.

```
from umlaut.core import Umlaut

class ExampleModel():
    """Example business logic that can be wrapped into a model.
       The class _must_ contain a 'predict' method.
    """
    def business_logic(self, record: dict) -> bool:
        if record.get("sales") > 5:
            return True
        else:
            return False

    def predict(self, model_input: dict) -> bool:
        return self.business_logic()

if __name__ == "__main__":
    from umlaut.core import Umlaut

    model = Umlaut(model_name="example model")
    model.track_model(ExampleModel())
```

This will push the latest changes of `ExampleModel()` to MLflow as a new model version. Navigate to the MLflow Tracking Server to find the latest push and associate it to the MLflow model.
