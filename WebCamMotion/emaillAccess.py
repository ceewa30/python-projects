from configparser import ConfigParser

def _get_email_key():
    """Fetch the API key from your configuration file.

    Expects a configuration file named "secrets.ini" with structure:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["email_access"]["SENDER"] , config["email_access"]["PASSWORD"] , config["email_access"]["RECEIVER"]

if __name__ == "__main__":
    print(_get_email_key())