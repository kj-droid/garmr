
# Garmr Lightweight Firewall

class GarmrFirewall:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)
        print(f"Rule added: {rule}")

    def list_rules(self):
        print("Active Rules:")
        for rule in self.rules:
            print(rule)

if __name__ == "__main__":
    firewall = GarmrFirewall()
    firewall.add_rule("Block all inbound traffic on port 22")
    firewall.list_rules()
