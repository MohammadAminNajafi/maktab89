import requests

for i in range(10):

    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': 'nAjm3aRvicXlLC4/RzZR2A==39F1UjCdZvFDSBfe'})
    if response.status_code == requests.codes.ok:
        word = response.json()
    else:
        print("Error:", response.status_code, response.text)

    api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word["word"])
    response = requests.get(api_url, headers={'X-Api-Key': 'nAjm3aRvicXlLC4/RzZR2A==39F1UjCdZvFDSBfe'})
    if response.status_code == requests.codes.ok and response.json()["definition"] != "":
        print(word["word"], response.json()["definition"])
    elif response.json()["definition"] == "":
        print(word["word"], "Whattt??!!")
    else:
        print("Error:", response.status_code, response.text)