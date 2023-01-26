import requests
#DO NOT MODIFY


def post(url, json, **kwargs):  # pragma: no mutate
    response = requests.Response()  # pragma: no mutate
    if "checkExist" in url and "bikernet.com" in url:  # pragma: no mutate
        response.status_code = 200 # pragma: no mutate
        response._content = bytes("True", "utf-8")  # pragma: no mutate
        return response  # pragma: no mutate
    elif "getPriceForBike" in url and "bikernet.com" in url:  # pragma: no mutate
        response.status_code = 200 # pragma: no mutate
        response._content = bytes("£6000", "utf-8")  # pragma: no mutate
        return response  # pragma: no mutate
    elif "bikernet.com" in url:  # pragma: no mutate
        response.status_code = 405 # pragma: no mutate
        response._content = bytes("Method not allowed", "utf-8")  # pragma: no mutate
        return response  # pragma: no mutate
    else:  # pragma: no mutate
        raise ConnectionError("Unable to resolve URL")  # pragma: no mutate
