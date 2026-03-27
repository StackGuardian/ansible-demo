#!/usr/bin/env python3
"""
Dynamic inventory script example for Ansible.

When called with --list, returns a JSON inventory of hosts.
When called with --host <hostname>, returns host-specific variables.

This example discovers hosts from environment variables,
but could query any API, cloud provider, CMDB, etc.
"""

import argparse
import json
import os
import sys


def get_inventory():
    """Build inventory from environment or a discovery source."""
    # Example: read comma-separated hosts from env var, fall back to defaults
    raw_hosts = os.environ.get("ANSIBLE_TARGET_HOSTS", "192.168.1.10,192.168.1.11")
    hosts = [h.strip() for h in raw_hosts.split(",") if h.strip()]

    return {
        "all": {
            "hosts": hosts,
            "vars": {
                "ansible_ssh_extra_args": "-o StrictHostKeyChecking=no"
            }
        },
        "_meta": {
            "hostvars": {}
        }
    }


def get_host_vars(hostname):
    """Return variables for a specific host."""
    return {}


def main():
    parser = argparse.ArgumentParser(description="Dynamic inventory script")
    parser.add_argument("--list", action="store_true", help="List all hosts")
    parser.add_argument("--host", type=str, help="Get variables for a specific host")
    args = parser.parse_args()

    if args.list:
        print(json.dumps(get_inventory(), indent=2))
    elif args.host:
        print(json.dumps(get_host_vars(args.host), indent=2))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
