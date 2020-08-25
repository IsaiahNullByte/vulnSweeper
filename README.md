# vulnSweeper

Dependencies:
Python2.7
pip install python-nmap


Tool used to scan the Internet or LAN for host running a specific vulnerable service. Script prompts user for service port and identifying parameter (i.e. service version number) to match for in banner grab results.

To specify specific host(s) or subnet(s) edit 'arguments' in line 26. By default the script scans the internet and excludes LAN addresses. 

E.x. - python vulnSweeper.py
