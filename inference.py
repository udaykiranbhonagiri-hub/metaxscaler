from env import DeliveryEnv

def run_env(difficulty):
    env = DeliveryEnv(difficulty)
    state = env.reset()

    print("[START]")
    done = False

    while not done:
        action = "DELIVER"  # simple baseline agent
        state, reward, done = env.step(action)
        print(f"[STEP] state={state}, reward={reward}")

    score = env.get_score()
    print(f"[END] score={score}")

if __name__ == "__main__":
    for level in ["easy", "medium", "hard"]:
        run_env(level)