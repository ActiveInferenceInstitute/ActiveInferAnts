import socket
import requests
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import netifaces
import usb.core
import usb.util

class NetworkUtils:
    """
    A collection of modern networking methods, including LAN, Ethernet, USB, Mesh Net, and website interactions.
    """

    @staticmethod
    def get_local_ip():
        """
        Retrieves the local IP address of the machine.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    @staticmethod
    def get_public_ip():
        """
        Retrieves the public IP address of the machine using an external service.
        """
        response = requests.get('https://api.ipify.org')
        return response.text

    @staticmethod
    def list_network_interfaces():
        """
        Lists all network interfaces and their details.
        """
        interfaces = netifaces.interfaces()
        return {interface: netifaces.ifaddresses(interface) for interface in interfaces}

    @staticmethod
    def start_simple_http_server(port=8000):
        """
        Starts a simple HTTP server on the specified port.
        """
        class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Hello, world!')

        httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
        httpd.serve_forever()

    @staticmethod
    def list_usb_devices():
        """
        Lists all connected USB devices.
        """
        devices = usb.core.find(find_all=True)
        return [usb.util.get_string(device, device.iProduct) for device in devices if device.iProduct]

    @staticmethod
    def fetch_website_content(url):
        """
        Fetches and returns the content of a website.
        """
        response = requests.get(url)
        return response.text

    @staticmethod
    def encode_url_parameters(params):
        """
        Encodes URL parameters.
        """
        return urllib.parse.urlencode(params)
