from echo.config import load_config

class Agent:
    def __init__(self, name: str):
        self.name = name
        self.memory = []
        self.config = load_config()

    def perceive(self, input_data: str):
        self.memory.append(input_data)
        return f"Received: {input_data}"

                                                    def run(self):
                                                            print(f"Agent {self.name} core is running...")
                                                                    print(f"Model: {self.config.model_name}")
                                                                            print(f"Max steps: {self.config.max_steps}")


                                                                            if __name__ == "__main__":
                                                                                echo = Agent("echo")
                                                                                    echo.run()