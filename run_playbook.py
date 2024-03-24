import ansible_runner

playbook_path = "hello.yml"
command = f"ansible-playbook {playbook_path}"
results = ansible_runner.interface.run_command(executable_cmd=command)
response, _, _ = results
print(f"Response: {response}")