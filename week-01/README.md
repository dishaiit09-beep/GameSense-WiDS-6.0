# Week 1 — Meet Reinforcement Learning 🐣

**Level:** Beginner · **Time:** ~8 hours including meetings and shared coding · **GPU:** Not required.

## 👉 Your primary learning resource

### **[Open the Week 1 Google Doc — full step-by-step guide](https://docs.google.com/document/d/1ooopqDUiiGSvQ9Zh6pKobe8IPoPcbLI4XPvaCYBKjCQ/edit?usp=drivesdk)**

**Follow that Google Doc from top to bottom.** It includes plain-language explanations, links to recommended courses, Flappy Bird examples, setup instructions and the mini check-in.

## What happens this week?

| Order | Approx. time | Task | Link |
| --- | ---: | --- | --- |
| 1 | 45 min | Python and NumPy refresher (optional) | [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) |
| 2 | 75 min | Learn agent, state, action, reward, policy, episode | [Hugging Face RL Unit 1](https://huggingface.co/learn/deep-rl-course/en/unit1/introduction) |
| 3 | 60 min | Learn reset(), step(), observations and actions | [Gymnasium Basic Usage](https://gymnasium.farama.org/main/introduction/basic_usage/) |
| 4 | 2 hr | Install + run our Flappy Bird random agent | [Setup guide](SETUP.md) |
| 5 | 90 min | Collect 20 episodes and inspect the CSV/plot | [Week 1 scripts](../scripts/) |
| 6 | 1.5–2 hr | Mentor discussion, debugging and code review | Team meeting / GitHub Issues |
| 7 | 10–15 min | **Only individual weekly assignment** | [Check-in](CHECKIN.md) |

## Team project milestone (not extra homework)

Together, we will produce:
1. A running Flappy Bird Gymnasium environment.
2. A random-policy **20-episode** CSV in `results/week01/`.
3. A graph of returns and survival steps from **real** recorded data.
4. A short discussion about why random play is not learning.

This random-policy code is the first baseline we will later compare with trained DQN. **No neural networks this week.**

## How to know you're finished

- [ ] I can explain agent → action → environment → observation + reward → agent.
- [ ] I understand what a random policy does.
- [ ] Our shared baseline runs, produces 20 CSV rows and a plot.
- [ ] I submitted the [10–15 minute check-in](CHECKIN.md).

If you get stuck on the game, use [SETUP.md](SETUP.md) and open a GitHub Issue with the error text.
