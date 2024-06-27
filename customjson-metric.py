## convert code coverage json to prometheus metric

import json
import time
from prometheus_client import start_http_server, Gauge

# Load the code coverage data from the JSON variable
data = {
    "name": "value",
    "metric2": 4.2,
    "metric3": 6,
    "metric4": "value4"
}

# Define the gauge metrics for code coverage
coverage_gauge = Gauge('code_coverage', 'Code coverage percentage', unit='percent')
line_coverage_gauge = Gauge('line_coverage', 'Line coverage percentage', unit='percent')
branch_coverage_gauge = Gauge('branch_coverage', 'Branch coverage percentage', unit='percent')
method_coverage_gauge = Gauge('method_coverage', 'Method coverage percentage', unit='percent')

# Set the values of the gauge metrics
coverage_gauge.set(data['coverage'])
line_coverage_gauge.set((data['coveredlines'] / data['totallines']) * 100)
branch_coverage_gauge.set((data['coveredbranches'] / data['totalbranches']) * 100)
method_coverage_gauge.set((data['coveredmethods'] / data['totalmethods']) * 100)

# Start the Prometheus metrics server
start_http_server(8080)

print("Prometheus metrics server started on port 8080")
while True:
    time.sleep(10)
