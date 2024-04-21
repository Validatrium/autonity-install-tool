import subprocess

# Update and upgrade packages
subprocess.run(['apt', 'update'])
subprocess.run(['apt', 'upgrade', '-y'])

# Install required packages
packages = [
    'curl', 'iptables', 'build-essential', 'git', 'wget', 'jq', 'make', 'gcc',
    'nano', 'tmux', 'htop', 'nvme-cli', 'pkg-config', 'libssl-dev', 'libleveldb-dev',
    'tar', 'clang', 'bsdmainutils', 'ncdu', 'unzip', 'chrony', 'libleveldb-dev', 'liblz4-tool'
]
subprocess.run(['apt', 'install'] + packages + ['-y'])

# Install Go
ver = "1.21.3"
subprocess.run(['wget', f"https://golang.org/dl/go{ver}.linux-amd64.tar.gz"])
subprocess.run(['sudo', 'rm', '-rf', '/usr/local/go'])
subprocess.run(['sudo', 'tar', '-C', '/usr/local', '-xzf', f"go{ver}.linux-amd64.tar.gz"])
subprocess.run(['rm', f"go{ver}.linux-amd64.tar.gz"])
subprocess.run(['echo', f"export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin >> $HOME/.bash_profile"])
subprocess.run(['source', '$HOME/.bash_profile'])
subprocess.run(['go', 'version'])

# Clone Autonity repository and build
subprocess.run(['git', 'clone', 'https://github.com/autonity/autonity.git', 'autonity1'])
subprocess.run(['cd', 'autonity1'])
subprocess.run(['make', 'all'])
subprocess.run(['mv', 'build/bin/ethkey', '/usr/local/bin'])

subprocess.run(['cd', '..'])
subprocess.run(['git', 'clone', 'https://github.com/autonity/autonity'])
subprocess.run(['cd', 'autonity'])
subprocess.run(['git', 'checkout', 'tags/v0.13.0', '-b', 'v0.13.0'])
subprocess.run(['make', 'autonity'])

# Configure systemd service
service_config = """
[Unit]
Description=autonity node
After=network.target

[Service]
User=$USER
Type=simple
ExecStart=$(which autonity) --datadir $HOME/autonity-chaindata --syncmode full --piccadilly --http --http.addr 0.0.0.0 --http.api aut,eth,net,txpool,web3,admin --http.vhosts *  --ws     --ws.addr 127.0.0.1 --ws.api aut,eth,net,txpool,web3,admin --autonitykeys $HOME/autonity-chaindata/autonity/nodekey --nat extip:$(curl 2ip.ru)
Restart=on-failure
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
"""

with open('/etc/systemd/system/autonity.service', 'w') as f:
    f.write(service_config)

# Reload and restart systemd
subprocess.run(['systemctl', 'daemon-reload'])
subprocess.run(['systemctl', 'enable', 'autonity'])
subprocess.run(['sudo', 'systemctl', 'restart', 'autonity'])

# View service logs
subprocess.run(['journalctl', '-u', 'autonity', '-f', '-o', 'cat'])
