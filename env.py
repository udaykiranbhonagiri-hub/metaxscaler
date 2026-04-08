import random

class DeliveryEnv:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.reset()

    def reset(self):
        if self.difficulty == "easy":
            self.packages = 1
            self.time = 10
        elif self.difficulty == "medium":
            self.packages = 3
            self.time = 15
        else:
            self.packages = 5
            self.time = 20

        self.delivered = 0
        self.state = {
            "packages_left": self.packages,
            "time_left": self.time
        }
        return self.state

    def step(self, action):
        reward = 0

        if action == "DELIVER" and self.packages > 0:
            self.packages -= 1
            self.delivered += 1
            reward += 10
        else:
            reward -= 1

        self.time -= 1

        done = self.packages == 0 or self.time <= 0

        self.state = {
            "packages_left": self.packages,
            "time_left": self.time
        }

        return self.state, reward, done

    def get_score(self):
        return self.delivered / (self.delivered + self.packages + 1e-5)