LogiSync is the simplest possible ML model deployment product

Small data departments are the market. They may have models they want to use/share
but don't know how to deploy. Simplify it by making any model into an endpoint. The
user installs the library which is FOSS. 

Important:
- Transformation tracking
- Include dataset tracking
- Associate dataset to model

Deploy:
The user installs the library which is a wrapper around MLflow. 

How do you simplify the MLflow deployment, or offer managed service?
Do things that don't scale.


# Analytics Layer

The Analytics Layer stores static business logic and provides an interface with MLflow for creating and using models. 

The layer introduces the concept of `models` which can be any reusable block of code that a team would like to make accessible to a broader audience.

- Easily maintain and access multiple versions of the same model
- Built in model lifecycle management
- Built in audit tracking and retrieval
- Built in UI using `MLflow`
- Auto-deployed logic that can be queried in an API (roadmap)

____
## Analytics Layer Class
A Python class to assist with saving and querying business logic.

- `update_model`: Converts a block of business logic into an Analytics Layer compatible `model`
- `query_model`: Queries a previously trained `model` and saves audit metadata
- `track_dataset`: Saves reporting datasets along with the initial query and underlying data that built it (roadmap)
- `audit_model`: Retrieve the results of a model run for a historic date
- `audit_dataset`: Retrieve a dataset as it was on a historic date

### Developing models with Analytics Layer
Custom `models` can be saved from any repository. To begin, install the private `analytics-layer` library by following this [development doc](https://docs.google.com/document/d/16blA2XrRTAMS-KORyJ2GkLLQUe2zJVBsMK02rcCMIEY/edit#heading=h.fixmy7m9p106). Ensure the code block is in a Python `Class` and follow the example below.

```
from analytics_layer.core import AnalyticsLayer

class CompanyFuzzyMatching():
    ...

def update_company_fuzzy_matching_model():
    company_fuzzy_matching = AnalyticsLayer(
        model=CompanyFuzzyMatching,
        model_name="Company Fuzzy Matching",
        s3_folder="company_fuzzy_matching",
    )
    company_fuzzy_matching.update_model()

if __name__ == "__main__":
    update_company_fuzzy_matching_model()
```

This will push the latest changes of `CompanyFuzzyMatching()` to MLflow as a new model version. Navigate to the [MLflow UI](http://mlflow-tracking.default.svc.cluster.local:5000/#/) to find the latest push and associate it to the MLflow model.
