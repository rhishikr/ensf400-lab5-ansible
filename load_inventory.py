import ansible_runner
import json

# Load inventory
inventory_data = json.loads(ansible_runner.interface.get_inventory(action="list", inventories=["./hosts.yml"])[0])

# Display host info
print("Hosts and their corresponding IP addresses:")
for host_name, attributes in inventory_data.get("_meta", {}).get("hostvars", {}).items():
    ip_address = attributes.get("ansible_host", "Unknown")
    print(f"{host_name} - IP address: {ip_address}")

# Display group info
print("\nHosts by group:")
for group_name, group_info in inventory_data.items():
    if group_name != "_meta":
        print(f"Hosts that are part of {group_name}:")
        for host in group_info.get("hosts", []):
            print(f"\t{host}")

# Ping all hosts
command_to_run = "ansible all:localhost -m ping"
result = ansible_runner.interface.run_command(executable_cmd=command_to_run)
response, _, _ = result
print(f"\nPing response: \n{response}")
