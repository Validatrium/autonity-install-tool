import subprocess

# Clone autonity-oracle repository and change directory
subprocess.run(['git', 'clone', 'https://github.com/autonity/autonity-oracle'])
subprocess.run(['cd', 'autonity-oracle'])

# Fetch latest changes and checkout version v0.1.6
subprocess.run(['git', 'fetch', '--all'])
subprocess.run(['git', 'checkout', 'v0.1.6'])

# Build autoracle
subprocess.run(['make', 'autoracle'])

# Move autoracle binary to /usr/local/bin
subprocess.run(['mv', 'build/bin/autoracle', '/usr/local/bin'])

# Configure systemd service
service_config = """
[Unit]
Description=Autonity Oracle Server
After=syslog.target network.target

[Service]
Type=simple
ExecStart=$(which autoracle) -key.file="/root/.autonity/keystore/oracle.key" -plugin.dir="/root/autonity-oracle/build/bin/plugins/" -plugin.conf="/root/autonity-oracle/build/bin/plugins-conf.yml" -key.password="" -ws="ws://127.0.0.1:8546"
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
"""

with open('/etc/systemd/system/antoracle.service', 'w') as f:
    f.write(service_config)

# Reload and restart systemd
subprocess.run(['systemctl', 'daemon-reload'])
subprocess.run(['systemctl', 'enable', 'antoracle'])
subprocess.run(['systemctl', 'restart', 'antoracle'])

# View service logs
subprocess.run(['journalctl', '-u', 'antoracle', '-f', '-o', 'cat'])
