import g4f
import asyncio


"""
    g4f.Provider.Bing,
    g4f.Provider.FreeChatgpt,
    g4f.Provider.Liaobots,
    g4f.Provider.OpenaiChat,
    g4f.Provider.Raycast,
    g4f.Provider.Theb,
    g4f.Provider.GeekGpt,

    g4f.Provider.AItianhuSpace,	
    g4f.Provider.AiChatOnline,	
    g4f.Provider.Aura,
	g4f.Provider.ChatBase,	
    g4f.Provider.ChatForAi,	
    g4f.Provider.ChatgptAi,	
	g4f.Provider.ChatgptDemo,	
	g4f.Provider.ChatgptNext,	
    g4f.Provider.Chatxyz,	
	g4f.Provider.GPTalk,	
    g4f.Provider.GeminiProChat,	
	g4f.Provider.Gpt6,	
    g4f.Provider.GptChatly,	
	g4f.Provider.GptForLove,	
    g4f.Provider.GptGo,	
    g4f.Provider.GptTalkRu,	
    g4f.Provider.Koala,
    g4f.Provider.MyShell,
    g4f.Provider.OnlineGpt,	
    g4f.Provider.PerplexityAi,	
    g4f.Provider.Poe,	
    g4f.Provider.TalkAi,	
    g4f.Provider.You,	
	g4f.Provider.AItianhu,	
    g4f.Provider.AiAsk,	
    g4f.Provider.Bestim,	
    g4f.Provider.ChatAnywhere,	
    g4f.Provider.Chatgpt4Online, 
	g4f.Provider.ChatgptDemoAi, 
    g4f.Provider.ChatgptFree,	
    g4f.Provider.ChatgptLogin,	
    g4f.Provider.ChatgptX,	
 	g4f.Provider.FakeGpt,	
 	g4f.Provider.FreeGpt,	
    g4f.Provider.GptGod,	
    g4f.Provider.Hashnode,	
    g4f.Provider.Vercel,	
    g4f.Provider.Ylokh,
    
    g4f.Provider.Bard,    
    g4f.Provider.DeepInfra,
    g4f.Provider.Gemini,
    g4f.Provider.HuggingChat,
    g4f.Provider.Llama2,
    g4f.Provider.PerplexityLabs,
    g4f.Provider.Phind,
    g4f.Provider.Pi,
    g4f.Provider.ThebApi,
    g4f.Provider.OpenAssistant
]




"""



_providers = [
    g4f.Provider.Bing,
    g4f.Provider.FreeChatgpt,
    g4f.Provider.Liaobots,
    g4f.Provider.OpenaiChat,
    g4f.Provider.Raycast,
    g4f.Provider.Theb,
    g4f.Provider.GeekGpt,

    g4f.Provider.AItianhuSpace,	
    g4f.Provider.AiChatOnline,	
    g4f.Provider.Aura,
	g4f.Provider.ChatBase,	
    g4f.Provider.ChatForAi,	
    g4f.Provider.ChatgptAi,	
	g4f.Provider.ChatgptDemo,	
	g4f.Provider.ChatgptNext,	
    g4f.Provider.Chatxyz,	
	g4f.Provider.GPTalk,	
    g4f.Provider.GeminiProChat,	
	g4f.Provider.Gpt6,	
    g4f.Provider.GptChatly,	
	g4f.Provider.GptForLove,	
    g4f.Provider.GptGo,	
    g4f.Provider.GptTalkRu,	
    g4f.Provider.Koala,
    g4f.Provider.MyShell,
    g4f.Provider.OnlineGpt,	
    g4f.Provider.PerplexityAi,	
    g4f.Provider.Poe,	
    g4f.Provider.TalkAi,	
    g4f.Provider.You,	
	g4f.Provider.AItianhu,	
    g4f.Provider.AiAsk,	
    g4f.Provider.Bestim,	
    g4f.Provider.ChatAnywhere,	
    g4f.Provider.Chatgpt4Online, 
	g4f.Provider.ChatgptDemoAi, 
    g4f.Provider.ChatgptFree,	
    g4f.Provider.ChatgptLogin,	
    g4f.Provider.ChatgptX,	
 	g4f.Provider.FakeGpt,	
 	g4f.Provider.FreeGpt,	
    g4f.Provider.GptGod,	
    g4f.Provider.Hashnode,	
    g4f.Provider.Vercel,	
    g4f.Provider.Ylokh,
    
    g4f.Provider.Bard,    
    g4f.Provider.DeepInfra,
    g4f.Provider.Gemini,
    g4f.Provider.HuggingChat,
    g4f.Provider.Llama2,
    g4f.Provider.PerplexityLabs,
    g4f.Provider.Phind,
    g4f.Provider.Pi,
    g4f.Provider.ThebApi,
    g4f.Provider.OpenAssistant
]

neyro_models = """
gpt_35_turbo_16k_0613
gpt_35_turbo_0613
gpt_35_turbo_16k
gpt_4_turbo
gpt_35_long
gpt_4
gpt_4_32k_0613
gpt_4_0613
gpt_4_32k
llama2_7b
llama2_13b
llama2_70b
codellama_34b_instruct
codellama_70b_instruct        
mixtral_8x7b
mistral_7b
dolphin_mixtral_8x7b
lzlv_70b
airoboros_70b
airoboros_l2_70b
openchat_35
gemini
gemini_pro
claude_v2
pi
"""


"""
default
FreeChatgpt: Yes, 
Llama2: Hello!
Bing: Hello, 
Aura: Hello! 
"""

"""
gpt_35_turbo_16k_0613
GeminiProChat: Hello Test,
FreeChatgpt: Hello, 
Aura: Hello! How can I assist you today?
Bing: Hello, this is Copilot.
"""

"""
gpt_35_turbo_16k
Aura: Hello! I'm here to help you with any questions or assistance you may need. How can I assist you today?
GeminiProChat: Hello, I am here to help you with your test.
GPTalk: Hello! How can I assist you today?
Bing: Hello, this is Copilot. I am an AI companion that can help you with information, questions, and conversation. 😊
"""


"""
gpt_35_turbo
Bing: Hello, this is Copilot.
Aura: Hello! 
"""

"""
airoboros_70b
GeminiProChat: Hello, this is a test. I am an AI chatbot, or virtual assistant, and I am here to help you with your inquiries. I can provide information, answer questions, and engage in conversations. I am trained on a massive amount of text and code data, which allows me to understand and respond to your requests in a natural and informative way.
Aura: Hello! How can I assist you today?
"""



async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "Hello is a test"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)
        
async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)

asyncio.run(run_all())
input()

"""


```
import os

try:
    import gpt_code
except Exception as e:
    if "No module named 'gpt_code'" in str(e):
        print("Trying to install the required module")
        os.system('pip install --upgrade "gpt_code"')
        input(error)
```


```python
import os

try:
    import gpt_code
except Exception as e:
    error = e
    if "No module named 'gpt_code'" in str(error):
        print(error)
        import_error = str(error).split("'")[1]
        print("Попытка установить необходимый модуль")
        os.system(f'pip install --upgrade {import_error}')
```






"""   

