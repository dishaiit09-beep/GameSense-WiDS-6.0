"""Track results for reproducible RL experiments."""
from dataclasses import dataclass, asdict
from statistics import mean

@dataclass
class EpisodeResult:
    episode: int
    seed: int
    total_reward: float
    steps: int
    terminated: bool
    truncated: bool

    def as_row(self):
        return asdict(self)

def summary(results):
    if not results:
        raise ValueError("No results")
    return {"episodes":len(results),"mean_return":mean(r.total_reward for r in results),"mean_steps":mean(r.steps for r in results)}
