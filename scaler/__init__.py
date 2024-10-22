# scaler/__init__.py

from .ec2_scaler import scale_down_ec2_instances, scale_up_ec2_instances
from .rds_scaler import scale_down_rds_instances, scale_up_rds_instances
from .eks_scaler import scale_down_eks_nodes, scale_up_eks_nodes

__all__ = [
    "scale_down_ec2_instances",
    "scale_up_ec2_instances",
    "scale_down_rds_instances",
    "scale_up_rds_instances",
    "scale_down_eks_nodes",
    "scale_up_eks_nodes"
]
