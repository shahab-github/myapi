import boto3

def scale_down_eks_nodes(asg_name, min_size=0, desired_size=0):
    asg = boto3.client('autoscaling')
    asg.update_auto_scaling_group(AutoScalingGroupName=asg_name, MinSize=min_size, DesiredCapacity=desired_size)
    print(f"Scaled down EKS nodes in ASG: {asg_name}")

def scale_up_eks_nodes(asg_name, min_size=2, desired_size=2):
    asg = boto3.client('autoscaling')
    asg.update_auto_scaling_group(AutoScalingGroupName=asg_name, MinSize=min_size, DesiredCapacity=desired_size)
    print(f"Scaled up EKS nodes in ASG: {asg_name}")
