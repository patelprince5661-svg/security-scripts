#!/usr/bin/env python3
"""
Prints system information using the platform module.
"""

import platform


def print_system_info():
    print("=" * 40)
    print(" System Information")
    print("=" * 40)

    print(f"System / OS:        {platform.system()}")
    print(f"OS Release:         {platform.release()}")
    print(f"OS Version:         {platform.version()}")
    print(f"Machine Type:       {platform.machine()}")
    print(f"Processor:          {platform.processor()}")
    print(f"Architecture:       {platform.architecture()[0]}")
    print(f"Node Name (host):   {platform.node()}")
    print(f"Platform:           {platform.platform()}")

    print("-" * 40)
    print(" Python Information")
    print("-" * 40)

    print(f"Python Version:     {platform.python_version()}")
    print(f"Python Build:       {platform.python_build()}")
    print(f"Python Compiler:    {platform.python_compiler()}")
    print(f"Python Implementation: {platform.python_implementation()}")


if __name__ == "__main__":
    print_system_info()
