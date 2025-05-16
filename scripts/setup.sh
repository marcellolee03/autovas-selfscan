#!/bin/bash

apt install traceroute
apt install nmap

docker exec -i greenbone-community-edition-gvmd-1 bash -c "mkdir auto_vas"

docker cp scripts/CreateTarget/create-targets-from-host-list.gmp.py greenbone-community-edition-gvmd-1:/auto_vas/create-targets-from-host-list.gmp.py
docker cp scripts/CreateTask/create-tasks-from-csv.gmp.py greenbone-community-edition-gvmd-1:/auto_vas/create-tasks-from-csv.gmp.py
docker cp scripts/RunScan/start-scans-from-csv.py greenbone-community-edition-gvmd-1:/auto_vas/start-scans-from-csv.py
docker cp scripts/ListReports/list-reports.gmp.py greenbone-community-edition-gvmd-1:/auto_vas/list-reports.gmp.py
docker cp scripts/ListReports/export-csv-report.gmp.py greenbone-community-edition-gvmd-1:/auto_vas/export-csv-report.gmp.py
docker cp scripts/ListReports/export-xml-report.gmp.py greenbone-community-edition-gvmd-1:/auto_vas/export-xml-report.gmp.py
docker cp scripts/ListReports/list-reports.gmp.py greenbone-community-edition-gvmd-1:/auto_vas/list-reports.gmp.py


docker exec -i greenbone-community-edition-gvmd-1 bash -c "apt-get update && apt-get install -y python3-venv python3-pip"
docker exec -i greenbone-community-edition-gvmd-1 bash -c "python3 -m venv path/to/venv && \
    source /path/to/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install python-gvm gvm-tools && \
    pip install OpenVAS-Reporting && \
    pip install pyyaml && \
    pip install defusedxml"
docker exec -i greenbone-community-edition-gvmd-1 bash -c "useradd auto_vas -s /bin/bash"