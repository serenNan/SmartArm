import numpy as np
from matplotlib import pyplot as plt
 
fig=plt.figure()
ax1=plt.axes(projection='3d')

model_points = np.array([
                            (0.0, 0.0, 0.0),             # Nose tip
                            (0.0, -330.0, -65.0),        # Chin
                            (-225.0, 170.0, -135.0),     # Left eye left corner
                            (225.0, 170.0, -135.0),      # Right eye right corne
                            (-150.0, -150.0, -125.0),    # Left Mouth corner
                            (150.0, -150.0, -125.0)      # Right mouth corner
                        ])

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.scatter(model_points[:,0], model_points[:,1], model_points[:,2], cmap='Blues')
#ax1.view_init(-20,0)
#ax1.plot3D(x,y,z,'gray')
plt.show()