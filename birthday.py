import click


@click.command()
@click.argument('name')
@click.argument('number')
# Function To send the Wihes to the person who information is obtained from input on the command line.
def sendwishes(name, number):

    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = f"sender_id=FSTSMS&message=Happy birthday {name} !! Wish you a great journey.Regards:Poobalan &language=english&route=p&numbers={number}"
    headers = {
        'authorization': "KpiPTf215ZCqYAjeNm0cFRdhkGxyowLJ4UX63lb8WDEu9HBSVOn4PGsK0rWV7A1oDiemxhYL5aX8gqbt",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


if __name__ == '__main__':
    sendwishes()
