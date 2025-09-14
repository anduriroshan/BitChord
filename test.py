import asyncio
from bitchord.core.context import Context
from bitchord.core.nodes import PromptNode, AnswerNode
from bitchord.executors.chain_executors import ChainExecutor
from bitchord.core.llm import GroqLLM

async def main():
    # setup llm + context
    llm = GroqLLM(model="llama3-8b-8192")  # example model
    ctx = Context()
    ctx.add_to_history(role="user", content="Hello! Can you tell me a fun fact about space?")

    # define nodes
    nodes = [
        PromptNode(name="prompt_node", llm=llm),
        AnswerNode(name="answer_node")
    ]

    # run executor
    executor = ChainExecutor(nodes)
    final_ctx = await executor.run(ctx, initial_input="You are a helpful assistant. Answer the user.")

    print("\nFinal Output:")
    print(final_ctx.history[-1])

if __name__ == "__main__":
    asyncio.run(main())