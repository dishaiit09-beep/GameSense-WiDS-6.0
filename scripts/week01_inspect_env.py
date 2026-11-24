"""Inspect the Flappy Bird observation/action space (no learning yet)."""

def main():
    import gymnasium as gym
    import flappy_bird_gymnasium  # registers FlappyBird-v0

    env = gym.make("FlappyBird-v0", use_lidar=False)
    try:
        observation, info = env.reset(seed=42)
        print("Observation shape:", getattr(observation, "shape", None))
        print("Example observation:", observation)
        print("Observation space:", env.observation_space)
        print("Action space:", env.action_space)
        print("0 = no flap, 1 = flap")
        next_observation, reward, terminated, truncated, info = env.step(0)
        print("Next observation:", next_observation)
        print("Reward:", reward, "terminated:", terminated, "truncated:", truncated)
    finally:
        env.close()

if __name__ == "__main__":
    main()
