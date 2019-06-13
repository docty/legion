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

Run the following command to install the dependencies with Pipenv

```bash
pipenv install --dev
```

##### 4. Run the code

Run main.py to vote 

```ruby
python main.py
```

By default it will display the captcha in your default image viewer and ask you to enter the captcha text in the 
terminal. You can modify the code and the Anticaptcha service, https://anti-captcha.com/, to solve the captchas instead.