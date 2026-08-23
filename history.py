from datetime import datetime
import re


def save_history(text):

    with open("history.txt", "a") as file:

        timestamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        file.write("=" * 50 + "\n")
        file.write("Date & Time: " + timestamp + "\n\n")
        file.write(text + "\n\n")


def clean_text(text):

    # Remove horizontal lines
    text = re.sub(r"^-{3,}$", "", text, flags=re.MULTILINE)

    # Remove Markdown headings
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)

    # Convert Markdown bullet points to normal bullets
    text = re.sub(r"^\s*\*\s+", "• ", text, flags=re.MULTILINE)

    # Remove Markdown bold symbols
    text = text.replace("**", "")

    # Remove unnecessary blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def get_history():

    try:

        with open("history.txt", "r") as file:
            data = file.read()

        if not data.strip():
            return []

        entries = data.split("=" * 50)

        history_list = []

        for entry in entries:

            entry = entry.strip()

            if not entry:
                continue

            lines = entry.split("\n")

            timestamp = ""

            if lines and lines[0].startswith("Date & Time:"):
                timestamp = lines[0].replace(
                    "Date & Time:", ""
                ).strip()

            content = "\n".join(lines[2:]).strip()

            title = "AI Activity"

            if "=== Summary ===" in content:

                title = "📝 Summary"

                content = content.replace(
                    "=== Summary ===", ""
                ).strip()

            elif "=== Quiz ===" in content:

                title = "🧠 Quiz"

                content = content.replace(
                    "=== Quiz ===", ""
                ).strip()

            elif "=== Explain Topic ===" in content:

                title = "💡 Explain Topic"

                content = content.replace(
                    "=== Explain Topic ===", ""
                ).strip()

            elif "=== HR Interview ===" in content:

                title = "🎤 HR Interview"

                content = content.replace(
                    "=== HR Interview ===", ""
                ).strip()

            elif "=== Technical Interview ===" in content:

                title = "💻 Technical Interview"

                content = content.replace(
                    "=== Technical Interview ===", ""
                ).strip()

            elif "=== Resume Review ===" in content:

                title = "📄 Resume Review"

                content = content.replace(
                    "=== Resume Review ===", ""
                ).strip()

            elif "=== Career Guidance ===" in content:

                title = "🎯 Career Guidance"

                content = content.replace(
                    "=== Career Guidance ===", ""
                ).strip()

            # Clean AI Markdown formatting
            content = clean_text(content)

            history_list.append({
                "title": title,
                "timestamp": timestamp,
                "content": content
            })

        history_list.reverse()
        
        return history_list

    except FileNotFoundError:

        return []


def clear_history():

    with open("history.txt", "w") as file:
        pass