"""
Hello AI Agent
Agentic AI Bootcamp Assignment
"""

class AIAgent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello! I am {self.name}, your AI Agent 🤖"

def main():
    agent = AIAgent("AgenticAI")
    print(agent.greet())

if __name__ == "__main__":
    main()
