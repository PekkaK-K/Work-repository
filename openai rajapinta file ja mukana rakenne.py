import openai
import os

def main():
    # Aseta API-avain ympäristömuuttujaan ennen ajoa:
    # Linux/macOS: export OPENAI_API_KEY="avaimesi"
    # Windows (PowerShell): $env:OPENAI_API_KEY="avaimesi"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    print("ChatGPT CLI – kirjoita kysymys (Ctrl+C lopettaa)")
    while True:
        try:
            user_input = input("\nSinä: ")
            if not user_input.strip():
                continue

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",   # tai "gpt-4" jos käytettävissä
                messages=[{"role": "user", "content": user_input}]
            )

            answer = response["choices"][0]["message"]["content"]
            print(f"\nChatGPT: {answer}")

        except KeyboardInterrupt:
            print("\nLopetetaan.")
            break
        except Exception as e:
            print(f"Virhe: {e}")

if __name__ == "__main__":
    main()