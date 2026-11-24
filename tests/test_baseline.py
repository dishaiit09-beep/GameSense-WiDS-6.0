"""Checks that beginner baseline pieces work without the game dependency."""
from gamesense.metrics import EpisodeResult, summary
from gamesense.policies import RandomPolicy

def test_random_policy_actions():
    p = RandomPolicy(42)
    actions = [p.act([1, 2, 3]) for _ in range(100)]
    assert set(actions) == {0, 1}

def test_random_policy_reproducible():
    p1, p2 = RandomPolicy(42), RandomPolicy(42)
    assert [p1.act(None) for _ in range(20)] == [p2.act(None) for _ in range(20)]

def test_episode_metrics():
    data = [EpisodeResult(1, 42, 2.0, 10, True, False),
            EpisodeResult(2, 43, 4.0, 20, True, False)]
    assert summary(data)["mean_return"] == 3
    assert summary(data)["mean_steps"] == 15
