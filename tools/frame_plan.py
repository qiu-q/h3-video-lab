"""Dry-run H3 duration planner; never submits generation jobs."""
import argparse, math, json
p=argparse.ArgumentParser();p.add_argument('seconds',type=float);a=p.parse_args()
if not math.isfinite(a.seconds) or a.seconds<=0:p.error('seconds must be finite and positive')
requested=math.ceil(a.seconds*24)
frames=5+17*math.ceil((max(5,requested)-5)/17)
print(json.dumps(dict(fps=24,target_seconds=a.seconds,requested_frames=requested,generated_frames=frames,last_frame_index=frames-1,generated_seconds=frames/24,trim_to_frames=requested,trimmed_seconds=requested/24,within_node_limit=frames<=3600,within_noted_training_range=124<=frames<=362),indent=2))
