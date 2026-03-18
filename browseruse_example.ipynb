# Browser Use: Automating Web Tasks with Python
# This notebook demonstrates how to use the browser-use library to automate web browsing tasks programmatically. With this library, you can create AI agents that interact with web interfaces just like humans do.

# Key features:

#Web Automation: Control browsers to navigate websites, fill forms, and extract data
#AI Integration: Combine LLM capabilities with browser control for intelligent web interactions
#Real-world Applications: Automate job applications, data collection, document creation, and more
#Custom Functions: Extend functionality with your own specialized web automation routines
# 1. INSTALL DEPENDENCIES
!pip install -qU browser-use langchain-google-genai playwright nest_asyncio
!playwright install chromium
!apt-get update
!apt-get install -y libnss3 libnspr4 libgbm1 libasound2

import os
import asyncio
import nest_asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
# Set your API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBD54zdx2Pvr7ZTSZXokgz2nkOY4acvoHc"
nest_asyncio.apply()
async def run_browser_test():
    # 3. CONFIGURE BROWSER (The "Headless" Magic)
    # Colab needs --no-sandbox to run Chromium correctly
    config = BrowserConfig(
        headless=True, 
        extra_chromium_args=['--no-sandbox', '--disable-setuid-sandbox']
    )
    browser = Browser(config=config)

    # 4. INITIALIZE LLM & AGENT
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    
    agent = Agent(
        task="Go to Wikipedia, find the 'Article of the day', and tell me its title.",
        llm=llm,
        browser=browser
    )

    # 5. EXECUTE
    print("🚀 Starting browser-use agent...")
    try:
        history = await agent.run()
        print("\n✅ Task Completed!")
        print(f"Final Result: {history.final_result()}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        await browser.close()

# 6. RUN THE ASYNC FUNCTION
await run_browser_test()
