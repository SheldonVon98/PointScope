from pointscope.core.client import PointScopeClient
import open3d as o3d
import numpy as np

torus = np.asarray(o3d.geometry.TriangleMesh.create_torus().vertices)
sphere = np.asarray(o3d.geometry.TriangleMesh.create_sphere().vertices)
                
PointScopeClient().add_pcd(torus).add_color(np.zeros_like(torus)).add_pcd(sphere).add_pcd(np.random.random((30000, 3))).show()