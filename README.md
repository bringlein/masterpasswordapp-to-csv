Masterpasswordapp/"Password: Spectre" to CSV
==============================
Simple python script to convert a JSON export from ["Masterpasswordapp"/"Password Spectre"](https://spectre.app) to a CSV file for importing in other password managers. 

As basis, export the configuration *with passwords* as JSON (works only on the iOS app, sadly). Afterwards, create a CSV file with:
```commandline
python3.8 mpw-to-csv.py path/to/mpwsites-export.json path/to/new.csv
```

As usual, some python packages are required: 

```commandline
virtualenv venv -p /usr/bin/python3.8
source venv/bin/activate
pip3 install -r requirements.txt
```


