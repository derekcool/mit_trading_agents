from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from dotenv import load_dotenv

load_dotenv()

# Create a custom config
config = DEFAULT_CONFIG.copy()
# config["llm_provider"] = "openai"  # Use a different model
# config["deep_think_llm"] = "gpt-5"  # Use a different model
# config["quick_think_llm"] = "gpt-5"  # Use a different model
config["llm_provider"] = "google"  # Use a different model
config["backend_url"] = "https://generativelanguage.googleapis.com/v1"  # Use a different backend
config["deep_think_llm"] = "gemini-2.0-flash"  # Use a different model
config["quick_think_llm"] = "gemini-2.0-flash"  # Use a different model
config["max_debate_rounds"] = 1  # Increase debate rounds
config["online_tools"] = True  # Increase debate rounds

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns

# import matplotlib.pyplot as plt
# from PIL import Image
# from io import BytesIO
# import numpy as np


# def show_mermaid(png_bytes, figsize=(6, 6)):
#     pil_img = Image.open(BytesIO(png_bytes))
#     img_array = np.array(pil_img)
#     plt.figure(figsize=figsize)
#     plt.imshow(img_array)
#     plt.axis("off")
#     plt.show()
#
# show_mermaid(ta.graph.get_graph().draw_mermaid_png(), figsize=(20, 18))