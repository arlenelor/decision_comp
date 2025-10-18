# Decisional conflict & memory project
## Summary
In everyday life, we are constantly faced with conflicting choices. Although some research has investigated how such decisions are made, it remains unknown how dynamic processes that arise during complex decisions shapes our memory for these choices later on. To address this, we tracked moment-by-moment decision-making procsses to predict subsequent memory performance. 

## Repository structure
*Data*    
+ /data/raw: Contains the raw mousetracking and memory accuracy data.    
+ /data/processed: Includes the cleaned and processed mousetracking and memory data. 

*Scripts*   
+ /notebooks/preprocessing: Contains scripts used to process mousetracking and memory test responses. Mousetracking trajectories were resampled to 20 ms intervals and interpolated to handle missing points when the mouse was stationary. Additionally, trajectoties were time normalized to allow for trial-by-trial comparison. Trials on the memory test were filtered to include correct decisions (in accordance with task instructions). 

+ /notebooks/analyses: Consists of scripts used to analyze data.

+ + /notebooks/analyses: Includes analysis visualizations.
