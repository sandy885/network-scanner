import tkinter as tk
from tkinter import messagebox
from scapy.all import ARP, Ether, srp
import ipaddress

def scan_network(network):
    # Create an ARP request packet
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send the packet and receive the response
    result = srp(packet, timeout=2, verbose=False)[0]

    # Parse the response
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def scan_button_clicked():
    network = entry.get()

    # Validate the network input
    try:
        ipaddress.ip_network(network)
    except ValueError:
        messagebox.showerror("Error", "Invalid network format. Please use CIDR notation (e.g., 192.168.1.0/24).")
        return

    print(f"Scanning network: {network}...")
    devices = scan_network(network)

    # Display the results in the text widget
    text.delete(1.0, tk.END)
    text.insert(tk.END, "Available devices:\n")
    text.insert(tk.END, "IP Address\t\tMAC Address\n")
    text.insert(tk.END, "-----------------------------------------\n")
    for device in devices:
        text.insert(tk.END, f"{device['ip']}\t{device['mac']}\n")

# Create the main window
root = tk.Tk()
root.title("Network Scanner")

# Set the background color to black
root.configure(bg='black')

# Create and place the widgets
label = tk.Label(root, text="Enter the network to scan (e.g., 192.168.1.0/24):", bg='black', fg='red')
label.pack()

entry = tk.Entry(root)
entry.pack()

scan_button = tk.Button(root, text="Scan", command=scan_button_clicked, bg='black', fg='red')
scan_button.pack()

text = tk.Text(root, height=30, width=80, bg='black', fg='red')
text.pack()

# Run the main loop
root.mainloop()
