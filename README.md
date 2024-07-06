**Perform Reverse DNS Lookups Using Python**

**Prerequisites**
Python 3 installed on your computer.
An API key from ViewDNS. You can get it here. The free version is okay to follow along.

Installing Required Libraries
We will use the argparse, ipaddress, socket, and requests libraries. If you don't have the requests library installed, you can install it using pip:

$ pip install requests

The others are pre-installed with Python. The uses of the above packages (as related to this program) include:

argparse: For parsing command-line arguments.
ipaddress: For validating IP addresses.
socket: To perform the reverse IP lookup.
requests: For making HTTP requests.

Dmonstrate on the file

**Running our Program**
Please do not forget to include your API key before running the program. 

To run the program (with all functionalities):

$ python reverse_lookup.py [IP Address] --all

I hope they don't send The Undertaker after us!

**Conclusion**
  In this tutorial, you learned how to perform reverse DNS lookups and identify other websites hosted on the same server using Python. 
  By leveraging the ViewDNS API, you can gain insights into server relationships and potentially discover more about the infrastructure 
  behind the IP addresses you're investigating.

