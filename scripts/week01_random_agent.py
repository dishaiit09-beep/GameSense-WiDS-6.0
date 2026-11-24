"""Run a random baseline for 20 Flappy Bird episodes and write a CSV.

This policy deliberately does NOT learn. Episode reward is NOT pipes passed.
"""
import argparse
import csv
from pathlib import Path
from gamesense.policies import RandomPolicy
from gamesense.metrics import EpisodeResult, summary

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-steps", type=int, default=20000)
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--out", type=Path, default=Path("results/week01/random_baseline.csv"))
    args = parser.parse_args()
    if args.episodes <= 0 or args.max_steps <= 0:
        parser.error("Episodes and max steps must be positive")

    import gymnasium as gym
    import flappy_bird_gymnasium  # registers FlappyBird-v0
    env = gym.make("FlappyBird-v0", use_lidar=False, render_mode="human" if args.render else None)
    policy = RandomPolicy(args.seed)
    results = []
    try:
        for episode in range(args.episodes):
            seed = args.seed + episode
            observation, info = env.reset(seed=seed)
            episode_return = 0.0
            terminated = truncated = False
            steps = 0
            for steps in range(1, args.max_steps + 1):
                action = policy.act(observation)
                observation, reward, terminated, truncated, info = env.step(action)
                episode_return += float(reward)
                if terminated or truncated:
                    break
            if not (terminated or truncated):
                truncated = True
            results.append(EpisodeResult(episode + 1, seed, round(episode_return, 6),
                                         steps, bool(terminated), bool(truncated)))
            print(f"Episode {episode + 1:02}: return={episode_return:.2f} steps={steps}")
    finally:
        env.close()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(results[0].as_row()))
        writer.writeheader()
        writer.writerows(result.as_row() for result in results)
    print("Summary:", summary(results))
    print("CSV:", args.out)
    print("A random baseline is NOT a trained AI. Return is not equal to pipe count.")

if __name__ == "__main__":
    main()
