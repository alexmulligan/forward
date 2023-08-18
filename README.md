# foward

forward is a program to listen for Windows notifications and forward them to the selected outputs (Telegram messages, email).  It offers the options to only handle notifications from specific programs and to choose multiple outputs to send to.


## Requirements

- Python 3.8 or 3.9, winrt only supports up to 3.9 (Tested with 3.8.10) - see [this link](https://www.python.org/downloads/windows/) for installing Python
- Poetry (Tested with 1.4.2, but may work with older versions) - see [this link](https://python-poetry.org/docs/) for installing Poetry
- All dependency requirements managed by poetry


## Setting up the program

1. Run `poetry install` inside the project folder to automatically install the dependencies for this program
2. Fill in the `config_example.py` as needed and rename it to `config.py`

### Configuring for sending Telegram messages

TODO: This section to be written.


### Configuring for sending emails

Under the email section in the config file, there are fields for Email and Password.  
These are the credentials for the account used to send emails.  

Some email providers (like Gmail) don't support email & password log in from Third Party Apps anymore.  The way I solved this with Gmail is to [create an app password](https://urldefense.com/v3/__https://support.google.com/mail/answer/185833?hl=en__;!!MiXNeB2G!JfyhheHvhysiGUW_JXZMoCstAzP3-L8fg2e6aieke2V9YJqBbGrmqvTy6x5Y660kj8y3QxPkpObtq-NDxSkKcw$) and put that in the Password field.  
Using an app password like this requires no change in implementation, so it works as is. Other solutions may require different implementations and are not supported at this time.

Note: Only Gmail is supported at this time.

## Running the program

In the project folder, run `poetry run python forward` to run the program manually.
