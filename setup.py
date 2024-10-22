from flask import Flask, jsonify
from scaler.ec2_scaler import scale_down_ec2_instances, scale_up_ec2_instances
from scaler.rds_scaler import scale_down_rds_instances, scale_up_rds_instances
from scaler.eks_scaler import scale_down_eks_nodes, scale_up_eks_nodes

app = Flask(__name__)

@app.route('/scale-down/ec2/<tag>', methods=['POST'])
def scale_down_ec2(tag):
    scale_down_ec2_instances(tag)
    return jsonify({"message": f"Scaled down EC2 instances with tag {tag}"}), 200

@app.route('/scale-up/ec2/<tag>', methods=['POST'])
def scale_up_ec2(tag):
    scale_up_ec2_instances(tag)
    return jsonify({"message": f"Scaled up EC2 instances with tag {tag}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
