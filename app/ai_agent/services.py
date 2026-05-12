from openai import OpenAI
from django.conf import settings


class AIAgent:
    """Сервис для генерации ответов через DeepSeek API"""

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com/v1"
        )

    def generate_answer(
            self,
            question_text: str,
            subject_name: str = "") -> str:
        """Генерирует развёрнутый ответ (Mock или реальный)"""

        if not settings.DEEPSEEK_API_KEY or 'your-api-key' in settings.DEEPSEEK_API_KEY:
            return self._mock_answer(question_text, subject_name)

        try:
            system_prompt = (
                "Ты - эксперт, помогающий студенту подготовиться к экзамену. "
                "Отвечай подробно, понятно, с примерами если нужно. "
                "Используй русский язык."
            )

            user_prompt = (
                f"Предмет: {subject_name}\n"
                f"Вопрос: {question_text}\n\n"
                f"Дай развёрнутый ответ для подготовки к экзамену:"
            )

            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception:
            return self._mock_answer(question_text, subject_name)

    def _mock_answer(self, question_text: str, subject_name: str) -> str:
        """Генерирует тестовый ответ без API"""
        return (
            f"📚 Это демонстрационный ответ на вопрос по предмету «{subject_name}»:\n\n"
            f"Вопрос: {question_text}\n\n"
            f"Ответ: Данный функционал использует DeepSeek API для генерации "
            f"развёрнутых ответов. При подключении реального API-ключа "
            f"ответы будут генерироваться нейросетью.\n\n"
            f"Для подключения:\n"
            f"1. Зарегистрируйтесь на platform.deepseek.com\n"
            f"2. Пополните баланс\n"
            f"3. Добавьте ключ в файл .env"
        )
