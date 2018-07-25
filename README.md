# 

The extracted segments consists of pupil dilation values whenever there was a task. User take variable number of timesteps for different tasks so it consists of variable number of timesteps.

However, to make the number of timesteps same for all the samples, we have padded individual samples with zero to make the length equal to the maximum timestep taken by any user for any task.

Dataset Dimension = (1855,1092,1)

Number of timesteps = 1092

The difference between each of the timestep is 16ms

Number of samples = 1855

Number of features = 1

Removing Noise :
When the eye was not detected by the eye-tracker, the pupil size was shown as -1 which is an invalid value. Such values have been replaced by the average of the five most recent pupil size values.
