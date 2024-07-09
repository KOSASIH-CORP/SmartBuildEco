def get_api_data(url):
    # Make API request
    response = requests.get(url)

    return response.json()
