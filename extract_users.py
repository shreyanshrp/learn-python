import sys

aws_arns = [ "arn:aws:iam::123456789012:user/shreyansh",
    "arn:aws:iam::123456789012:user/dev-ops-admin",
    "arn:aws:iam::987654321098:user/deploy-bot" ]

def get_username(arn):
	return arn.split("/")[-1]

print("--Extracted Users--")
for arn in aws_arns:
	user = get_username(arn)
	print(user)

