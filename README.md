# Legion

An app for voting on behalf of Sesi Technologies supporters who have opted in for their emails to be used for voting.

## Development

##### Prerequisites

The setups steps expect following tools installed on the system.

- Git
- Pipenv

##### 1. Check out the repository

```bash
git clone git@github.com:peter-ohara/legion.git
```

##### 2. Install dependencies

Run the following command to create python virtual environmant and install dependencies and install the project's
dependencies

```bash
cd legion
pipenv install --dev
```

##### 3. Activate the project's virtual environment

```bash
pipenv shell
```

##### 4. Run the program 

```bash
python main.py <api_key_from_anticaptcha_service>
```

If the API key is omitted, it will display the captcha in your default image viewer and ask you to enter the 
captcha text in the terminal.