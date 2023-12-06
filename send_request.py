import requests

# List of server IP addresses
server_ips = ['172.21.27.60','172.21.27.61']
server_port = 5000  # Assuming the servers are running on the same port

# Data to send in the request
data_to_send = {'user_input': 'value'}  # Replace with the data you want to send

for server_ip in server_ips:
    url = f'http://{server_ip}:{server_port}/receive_data'

    try:
        response = requests.post(url, data=data_to_send)
        print(f"Request sent to {server_ip}. Response: {response.text}")
    except requests.RequestException as e:
        print(f"Error sending request to {server_ip}: {e}")
