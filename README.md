# 

The extracted segments consists of pupil dilation values whenever there was a task. User take variable number of timesteps for different tasks so it consists of variable number of timesteps.

However, to make the number of timesteps same for all the samples, we have padded individual samples with zero to make the length equal to the maximum timestep taken by any user for any task.

Dataset Dimension = (1855,1092,1)

Number of timesteps = 1092

Number of samples = 1855

Number of features = 1

