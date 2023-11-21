import boto3

iam = boto3.client("iam")

role_name = "MyNewEC2Role"

policy_name = "MyNewECPolicy"

iam.attach_role_policy(
    RoleName = role_name,
    PolicyArn = "arn:aws:iam::416815474093:policy/MyNewECPolicy"
)

print(f"Policy {policy_name} attached to IAM Role {role_name}")

