# Flask RESTPlus monkeypatches

Fix a few issues with [Flask-RESTPlus](https://github.com/noirbizarre/flask-restplus).

The reasons why this package exists are to be found here: <https://github.com/noirbizarre/flask-restplus/issues/517>

## How to contribute

Fork the repository, then get hacking:

```sh
git clone git@github.com:you/flask_restplus_monkeypatch
cd flask_restplus_monkeypatch
```

Create a new branch off the `dev` branch for your contribution. Prefix with `feature-` or `bugfix-` as appropriate.

```sh
git checkout -b feature-my-jazzy-contribution dev
```

Install the dependencies:

```sh
virtualenv --python=python3 ./venv
source venv/bin/activate
pip install -r requirements.txt
```

All fixes are implemented with a simple plugin architecture. All your code should live in `flask_restplus_monkeypatch/plugins/my_jazzy_contribution/__init__.py`. It must contain the function `init(app,**kwars)` which takes the app as the first, obligatory argument, and returns the app, as well as anything else you need to return. See the `example` plugin as a template.

Add your plugin:

```sh
mkdir flask_restplus_monkeypatch/plugins/my_jazzy_contribution
touch flask_restplus_monkeypatch/plugins/my_jazzy_contribution/__init__.py
```

Edit the new `__init__.py` and save. Any arguments that need to be passed to your plugin must be added to `kwargs` 

Add your contribution to the tests. Edit `tests/test_all.py`. Note that the function names contain numbers so they are executed in order. Add your test at the end, or wherever is appropriate. Two other things to be aware of:

1. The func name must begin with `test_` so it is automatically picked up for testing.
2. Any arguments you need to pass to your plugin must be done so as a `dict` with the same name as your plugin.

Here's an example:

```python

import flask_restplus_monkeypatch as frm
# Other imports here.
# An app and a logger are also defined.

class MyTestCase(unittest.TestCase):

    # Other code trimmed for brevity
    
    def test_00700_my_jazzy_contribution(self):
        """
        Put some explanatory docs here if you're conscientious!
        """
        global app, base_url, logger, name
        app = frm.apply(app,
                  my_jazzy_contribution = {
                      "Any other arguments": "required by your plugin",
                      "can go in here": "They will appear in kwargs",
                  }
        )

        response = app.test_client().get(base_url + "/a-route-you-added-perhaps")
        assert response.status_code == 200,
            "Error message here will be displayed if the test fails."

```

Run the tests:

```sh
python -m unittest discover -v -s ./tests/
```

If everything is okay, commit the changes to your feature branch and [issue a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) asking to merge the changes into the `dev` branch:

```sh
git add .
git commit -m 'Informative message here please!'
# Push the branch back to your repository:
git push --set-upstream origin feature-my-jazzy-contribution
```
