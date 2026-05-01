"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from langchain_core.load import dumpd
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()

SOURCE_PROMPT = "leonanluppi/bug_to_user_story_v1"
OUTPUT_PATH = "prompts/bug_to_user_story_v1.yml"


def serialize_prompt(prompt) -> dict:
    """Converte um ChatPromptTemplate em dict serializável para YAML."""
    messages = []
    for msg in getattr(prompt, "messages", []):
        role = getattr(msg, "type", None) or msg.__class__.__name__.lower().replace("messageprompttemplate", "")
        if hasattr(msg, "prompt") and hasattr(msg.prompt, "template"):
            content = msg.prompt.template
        elif hasattr(msg, "content"):
            content = msg.content
        else:
            content = str(msg)
        messages.append({"role": role, "content": content})

    return {
        "source": SOURCE_PROMPT,
        "input_variables": list(getattr(prompt, "input_variables", [])),
        "messages": messages,
        "raw": dumpd(prompt),
    }


def pull_prompts_from_langsmith() -> bool:
    """Faz pull do prompt do LangSmith Hub e salva em YAML local."""
    print_section_header("PULL DE PROMPTS DO LANGSMITH HUB")
    print(f"Source: {SOURCE_PROMPT}")
    print(f"Destino: {OUTPUT_PATH}\n")

    try:
        prompt = hub.pull(SOURCE_PROMPT)
        print(f"   ✓ Prompt baixado do Hub")
    except Exception as e:
        print(f"❌ Erro ao baixar prompt: {e}")
        return False

    data = serialize_prompt(prompt)

    if not save_yaml(data, OUTPUT_PATH):
        print(f"❌ Erro ao salvar YAML em {OUTPUT_PATH}")
        return False

    print(f"   ✓ Prompt salvo em {OUTPUT_PATH}")
    return True


def main():
    """Função principal"""
    if not check_env_vars(["LANGSMITH_API_KEY"]):
        return 1

    success = pull_prompts_from_langsmith()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
