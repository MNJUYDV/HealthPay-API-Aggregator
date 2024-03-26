**HealthPay API Aggregator**

The HealthPay API Aggregator is a service that fetches healthcare information for a member from multiple APIs, aggregates the data, and provides the "true" out-of-pocket maximum (oop_max), remaining out-of-pocket maximum (remaining_oop_max), and copay information to the user.

**Features**

**API Aggregation**: Fetches data from multiple APIs to provide comprehensive healthcare information.

**Data Coalescing**: Aggregates data from different APIs to provide accurate information to the user.

**Error Handling**: Handles common error cases, such as API failures or downtime, gracefully.

**Flexibility**: Easily extendable to add additional APIs or modify existing ones.

**Installation**
Clone the repository:

```
git clone https://github.com/your-username/HealthPay-API-Aggregator.git
```


```
cd HealthPay-API-Aggregator
```

Create and activate a virtual environment (recommended):

```
python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate.bat     # For Windows
```

**Install the dependencies**:
```
pip install -r requirements.txt
```

**Usage**
Run the FastAPI server:

```
uvicorn app.main:app --reload
```

Use the /healthcare/{member_id} endpoint to fetch healthcare information for a specific member by providing the member ID as a parameter.

**Testing**
To run the tests, execute the following command:

```
python manage.py

or 

run individual test file
```

