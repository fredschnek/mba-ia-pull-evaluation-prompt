"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()

V2_PROMPT_PATH = "prompts/bug_to_user_story_v2.yml"
PROMPT_BASENAME = "bug_to_user_story_v2"


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []

    if not prompt_data:
        return (False, ["YAML vazio ou inválido"])

    if "messages" not in prompt_data:
        errors.append("Campo 'messages' ausente")
    elif not isinstance(prompt_data["messages"], list) or not prompt_data["messages"]:
        errors.append("'messages' deve ser uma lista não-vazia")
    else:
        valid_roles = {"system", "user", "assistant", "human", "ai"}
        for i, msg in enumerate(prompt_data["messages"]):
            if not isinstance(msg, dict):
                errors.append(f"messages[{i}] deve ser um dict")
                continue
            if "role" not in msg or "content" not in msg:
                errors.append(f"messages[{i}] precisa de 'role' e 'content'")
                continue
            if msg["role"] not in valid_roles:
                errors.append(f"messages[{i}].role inválido: {msg['role']}")
            if not isinstance(msg["content"], str) or not msg["content"].strip():
                errors.append(f"messages[{i}].content vazio")

    system_prompt = prompt_data.get("system_prompt", "")
    if not isinstance(system_prompt, str) or not system_prompt.strip():
        errors.append("'system_prompt' ausente ou vazio")
    elif "[TODO]" in system_prompt:
        errors.append("'system_prompt' ainda contém marcadores [TODO]")

    techniques = prompt_data.get("metadata", {}).get("techniques", [])
    if not isinstance(techniques, list) or len(techniques) < 2:
        errors.append(f"metadata.techniques precisa de ≥ 2 técnicas (encontradas: {len(techniques) if isinstance(techniques, list) else 0})")

    return (len(errors) == 0, errors)


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt (formato: "{username}/{basename}")
        prompt_data: Dados do prompt carregados do YAML

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        messages = [(m["role"], m["content"]) for m in prompt_data["messages"]]
        prompt_template = ChatPromptTemplate.from_messages(messages)

        hub.push(
            prompt_name,
            prompt_template,
            new_repo_is_public=True,
            new_repo_description=prompt_data.get("description", ""),
            tags=prompt_data.get("tags", []),
        )
        print(f"   ✓ Push concluído: {prompt_name}")
        print(f"   ✓ URL: https://smith.langchain.com/hub/{prompt_name}")
        return True

    except Exception as e:
        print(f"   ❌ Erro no push: {e}")
        return False


def main():
    """Função principal"""
    print_section_header("PUSH DE PROMPTS PARA O LANGSMITH HUB")

    if not check_env_vars(["LANGSMITH_API_KEY", "USERNAME_LANGSMITH_HUB"]):
        return 1

    username = os.getenv("USERNAME_LANGSMITH_HUB")
    prompt_name = f"{username}/{PROMPT_BASENAME}"

    print(f"Arquivo: {V2_PROMPT_PATH}")
    print(f"Destino: {prompt_name}\n")

    data = load_yaml(V2_PROMPT_PATH)
    if data is None:
        print(f"❌ Não foi possível carregar {V2_PROMPT_PATH}")
        return 1

    is_valid, errors = validate_prompt(data)
    if not is_valid:
        print("❌ Prompt inválido:")
        for err in errors:
            print(f"   - {err}")
        return 1

    print("   ✓ Validação OK")

    if push_prompt_to_langsmith(prompt_name, data):
        print("\n✅ Prompt publicado com sucesso!")
        print("\nPróximos passos:")
        print("   1. Confira em https://smith.langchain.com/hub")
        print("   2. Rode a avaliação: python src/evaluate.py")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
