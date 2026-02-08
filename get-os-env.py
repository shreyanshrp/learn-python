#Used export AWS_REGION="us-east-1" to inject env variable into OS, the following program will ectract env from there to get region

import os
region = os.getenv("AWS_REGION")

print(f"The region is {region}")