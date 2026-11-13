import sys
from pathlib import Path

# 支持直接运行: python customer/utils/llm_client.py
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from customer.config.config import settings


llm: BaseChatModel = init_chat_model(
    model=settings.llm_model,
    model_provider="openai",
    api_key=settings.llm_api_key,
    base_url=settings.llm_base_url,
    temperature=0,
)

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(llm.invoke("hello").content)
