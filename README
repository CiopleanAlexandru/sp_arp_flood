## What this code does
This code generates a series of ARP requests and sends them to the broadcast address. The ARP requests contain a random source MAC address that starts with the vendor identifier "b8:e8:56:".

The purpose of the ARP requests is to confuse network devices and possibly disrupt network communication. When a device receives an ARP request, it will attempt to resolve the IP address associated with the MAC address in the request. If the device receives multiple ARP requests with different MAC addresses for the same IP address, it may become confused and unable to determine the correct MAC address for that IP address.

## How to run this code
```sudo -E python3 arp_flood.py```