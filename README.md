# personal-data
A tool for retrieving data about yourself from various sources and putting it into a MySQL database.

This tool is freely available under the MIT licence (see LICENCE) unless otherwise noted.

## Downloading and Setting up
1. Make sure that Java and Python 3 are installed
2. Install the Python Google API Client with
```pip3 install --upgrade google-api-python-client```
3. Create a wrapper directory (```mkdir personal-data```) and enter it (```cd personal-data```)
4. Clone this Github repository with 
```git clone https://github.com/medude/personal-data.git``` or download and extract the zip file into the wrapper directory
5. Go to [this Google website](https://console.developers.google.com/flows/enableapi?apiid=fitness)
6. Create a project and select continue
7. Click the button to go to the credentials page
8. Leave the first drop down menu at the default and select "Other UI" for the other one, also checking the "User data" radio button before clicking the button at the bottom.
9. Choose a name. It doesn't matter very much.
10. Choose your email and type a name in the product name box. It doesn't matter either.
11. Choose download and put the resulting file in the wrapper directory that the project went into.
12. Rename the file that you just downloaded to ```client_secrets.json```.

## Usage
**If you skipped the previous section, make sure to at least follow step 2 and steps 5 through 12, or else it will not work!**

In ```src```, run ```python3 fit_data.py``` to download your step counts from Google Fit. You can modify ```request.json``` in ```src``` to change the time period.