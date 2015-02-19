import botocore.session
import boto3
import sys
import dateutil.parser
import os
import calendar
import json

BENCHMARK_NAMES = ['ContentAll','FrontsAll']
TABLE_NAME = 'perf'

def iso_timetsamp_to_unix(iso_timestamp):
	datetime = dateutil.parser.parse(iso_timestamp)
	return calendar.timegm(datetime.timetuple())

session = botocore.session.get_session()
session.profile = 'nextgen'
boto3.setup_default_session(botocore_session=session)
client = boto3.client('dynamodb')

iso_timestamp = sys.argv[1]
unix_timestamp = iso_timetsamp_to_unix(iso_timestamp)

for test_name in BENCHMARK_NAMES:
	results_filename = os.path.join('results', iso_timestamp, test_name, 'results.json')
	with open(results_filename, 'r') as f:
		benchmark_data = f.read()
		benchmark_json = json.loads(benchmark_data)
		item = {
			'timestamp': { 'N': str(unix_timestamp) },
			'benchmark_name': { 'S': benchmark_json['benchmark_name'] },
			'benchmark_data': { 'S': benchmark_data }
		}
		client.put_item(TableName=TABLE_NAME, Item=item)
