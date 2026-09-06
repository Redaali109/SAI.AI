# ==========================================================
#                    SAI AI 🤖
#              مشروع الذكاء الاصطناعي الأول
# ==========================================================

import json
import os
import datetime


MEMORY_FILE = "memory.json"
CHAT_FILE = "chat_history.json"


# ==========================================================
# تحميل الذاكرة
# ==========================================================

def load_memory():

    if os.path.exists(MEMORY_FILE):

        try:

            with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

                if not isinstance(data, dict):
                    raise ValueError
                
                if "name" not in data:
                    data["name"] = "صفا"

                if "memories" not in data:
                    data["memories"] = []

                return data

        except (json.JSONDecodeError, OSError, ValueError):
            pass

    return {
        "name": "صفا",
        "memories": []
    }


# ==========================================================
# حفظ الذاكرة
# ==========================================================

def save_memory(memory):

    try:

        with open(MEMORY_FILE, "w", encoding="utf-8") as file:

            json.dump(
                memory,
                file,
                ensure_ascii=False,
                indent=4
            )

    except OSError:

        print("SAI: حدث خطأ أثناء حفظ الذاكرة.")


# ==========================================================
# تحميل سجل المحادثة
# ==========================================================

def load_chat():

    if os.path.exists(CHAT_FILE):

        try:

            with open(CHAT_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return data

        except (json.JSONDecodeError, OSError):
            pass

    return []


# ==========================================================
# حفظ سجل المحادثة
# ==========================================================

def save_chat(chat):

    try:

        with open(CHAT_FILE, "w", encoding="utf-8") as file:

            json.dump(
                chat,
                file,
                ensure_ascii=False,
                indent=4
            )

    except OSError:

        print("SAI: حدث خطأ أثناء حفظ سجل المحادثة.")


# ==========================================================
# تحميل البيانات
# ==========================================================

memory = load_memory()
chat = load_chat()


# ==========================================================
# حفظ الرسالة
# ==========================================================

def save_message(user_message, bot_message):

    chat.append({

        "time": datetime.datetime.now().isoformat(),

        "user": user_message,

        "sai": bot_message

    })

    save_chat(chat)


# ==========================================================
# SAI - اللغة العربية
# ==========================================================

def sai_response_arabic(message):

    text = message.lower().strip()

    name = memory.get("name", "صفا")


    # ------------------------------------------
    # التحية
    # ------------------------------------------

    if text in [
        "سلام",
        "السلام عليكم",
        "السلام عليكم ورحمة الله وبركاته"
    ]:

        return f"وعليكم السلام ورحمة الله وبركاته يا {name} 🤖🖤"


    if text in [
        "هلا",
        "مرحبا",
        "اهلا",
        "أهلا",
        "أهلًا"
    ]:

        return (
            f"أهلًا يا {name}! أنا SAI 🤖\n"
            "مساعدك الشخصي بالذكاء الاصطناعي."
        )


    # ------------------------------------------
    # سؤال عن اسم SAI
    # ------------------------------------------

    if "اسمك" in text or "ماهو اسمك" in text:

        return "اسمي SAI 🤖"


    # ------------------------------------------
    # سؤال عن اسم المستخدم
    # ------------------------------------------

    if "شنو اسمي" in text or "ما اسمي" in text or "ماهو اسمي" in text:

        if memory["name"]:

            return f"اسمك هو {memory['name']} ❤️"

        return "ما أعرف اسمك بعد. اكتب: /name اسمك"


    # ------------------------------------------
    # الوقت
    # ------------------------------------------

    if (
        "الوقت" in text
        or "الساعة" in text
        or "ماهو الوقت الان" in text
        or "كم الساعة" in text
    ):

        now = datetime.datetime.now()

        return f"الوقت الآن هو {now.strftime('%H:%M:%S')} ⏰"


    # ------------------------------------------
    # التاريخ
    # ------------------------------------------

    if (
        "التاريخ" in text
        or "اليوم" in text
        or "ماهو تاريخ اليوم" in text
    ):

        now = datetime.datetime.now()

        return f"تاريخ اليوم هو {now.strftime('%Y-%m-%d')} 📅"


    # ------------------------------------------
    # الذاكرة
    # ------------------------------------------

    if "شنو تتذكر" in text or "ماذا تتذكر" in text:

        if not memory["memories"]:

            return "ذاكرتي فارغة حاليًا 🧠"

        result = "هذه الأشياء التي أتذكرها 🧠:\n"

        for i, item in enumerate(memory["memories"], 1):

            result += f"{i}. {item}\n"

        return result


    # ------------------------------------------
    # كيف حالك
    # ------------------------------------------

    if "شلونك" in text or "كيف حالك" in text:

        return f"أنا بخير يا {name} وجاهز أساعدك 🤖🔥"


    # ------------------------------------------
    # شكراً
    # ------------------------------------------

    if "شكرا" in text or "شكرًا" in text:

        return f"العفو يا {name}! 🖤"


    # ------------------------------------------
    # وداع
    # ------------------------------------------

    if "باي" in text or "مع السلامة" in text:

        return f"مع السلامة يا {name} 👋🖤"


    # ------------------------------------------
    # سؤال غير معروف
    # ------------------------------------------

    return (
        "ما زلت أتعلم 🤖\n"
        "لم أفهم السؤال بالكامل.\n"
        "في النسخة القادمة يمكننا إضافة نموذج AI حقيقي."
    )


# ==========================================================
# SAI - اللغة الإنجليزية
# ==========================================================

def sai_response_english(message):

    text = message.lower().strip()

    name = memory.get("name", "Safa")


    # ------------------------------------------
    # Greetings
    # ------------------------------------------

    if text in [
        "hello",
        "hi",
        "hey"
    ]:

        return (
            f"Hello {name}! I am SAI 🤖\n"
            "Your personal AI assistant."
        )


    if text in [
        "good morning"
    ]:

        return f"Good morning, {name}! Have a great day 🤖☀️"


    if text in [
        "good evening"
    ]:

        return f"Good evening, {name}! How can I help you? 🤖"


    # ------------------------------------------
    # Ask about SAI's name
    # ------------------------------------------

    if "your name" in text:

        return "My name is SAI 🤖"


    # ------------------------------------------
    # Ask about user's name
    # ------------------------------------------

    if "my name" in text or "what is my name" in text:

        if memory["name"]:

            return f"Your name is {memory['name']} ❤️"

        return "I don't know your name yet. Type: /name YourName"


    # ------------------------------------------
    # Time
    # ------------------------------------------

    if "time" in text or "clock" in text:

        now = datetime.datetime.now()

        return f"The current time is {now.strftime('%H:%M:%S')} ⏰"


    # ------------------------------------------
    # Date
    # ------------------------------------------

    if "date" in text or "today" in text:

        now = datetime.datetime.now()

        return f"Today's date is {now.strftime('%Y-%m-%d')} 📅"


    # ------------------------------------------
    # Memory
    # ------------------------------------------

    if (
        "what do you remember" in text
        or "your memory" in text
    ):

        if not memory["memories"]:

            return "My memory is currently empty 🧠"

        result = "These are the things I remember:\n"

        for i, item in enumerate(memory["memories"], 1):

            result += f"{i}. {item}\n"

        return result


    # ------------------------------------------
    # How are you
    # ------------------------------------------

    if "how are you" in text:

        return f"I'm doing great, {name}, and I'm ready to help you 🤖🔥"


    # ------------------------------------------
    # Thank you
    # ------------------------------------------

    if "thank you" in text or "thanks" in text:

        return f"You're welcome, {name}! 🖤"


    # ------------------------------------------
    # Goodbye
    # ------------------------------------------

    if "bye" in text or "goodbye" in text:

        return f"Goodbye, {name}! See you later 👋🖤"


    # ------------------------------------------
    # Unknown question
    # ------------------------------------------

    return (
        "I'm still learning 🤖\n"
        "I didn't fully understand your question.\n"
        "In the next version, we can add a real AI model."
    )


# ==========================================================
# الواجهة العربية
# ==========================================================

def show_arabic_header():

    print()

    print("=" * 55)

    print("                 SAI AI 🤖")

    print("              مساعد صفا الشخصي")

    print("=" * 55)

    print()

    print(
        "رجاءً هذا البرنامج على قيد التطوير، "
        "أرجو المعذرة منكم 🌹"
    )

    print()

    print("المستخدم:", memory.get("name", "صفا"))

    print()

    print("الأوامر:")

    print("/name اسمك       → حفظ اسمك")

    print("/remember شيء    → حفظ معلومة")

    print("/memory          → عرض الذاكرة")

    print("/forget رقم      → حذف ذاكرة")

    print("/clear           → مسح الذاكرة")

    print("/history         → عرض المحادثات")

    print("/help            → المساعدة")

    print("/exit            → خروج")

    print()


# ==========================================================
# الواجهة الإنجليزية
# ==========================================================

def show_english_header():

    print()

    print("=" * 55)

    print("                 SAI AI 🤖")

    print("           Safa's Personal Assistant")

    print("=" * 55)

    print()

    print(
        "Please note that this program is currently "
        "under development. Thank you for your understanding."
    )

    print()

    print("User:", memory.get("name", "Safa"))

    print()

    print("Commands:")

    print("/name YourName       → Save your name")

    print("/remember Something  → Save a memory")

    print("/memory              → Show memory")

    print("/forget Number       → Delete memory")

    print("/clear               → Clear memory")

    print("/history             → Show chat history")

    print("/help                → Show help")

    print("/exit                → Exit")

    print()


# ==========================================================
# اختيار اللغة
# ==========================================================

def choose_language():

    print()

    print("=" * 55)

    print("                 SAI AI 🤖")

    print("=" * 55)

    print()

    print("اختر اللغة / Choose language:")

    print()

    print("1. عربي 🇮🇶")

    print("2. English 🇬🇧")

    print()

    while True:

        language = input(
            "اختيارك / Your choice: "
        ).strip().lower()


        # ------------------------------------------
        # اللغة العربية
        # ------------------------------------------

        if language in [
            "1",
            "عربي",
            "عربية",
            "عربيه",
            "العربية",
            "arabic"
        ]:

            return "arabic"


        # ------------------------------------------
        # اللغة الإنجليزية
        # ------------------------------------------

        elif language in [
            "2",
            "english",
            "انكليزي",
            "إنكليزي",
            "انجليزي",
            "إنجليزي"
        ]:

            return "english"


        else:

            print()

            print("SAI: اكتب عربي أو English")

            print()


# ==========================================================
# تشغيل البرنامج
# ==========================================================

language = choose_language()


# ==========================================================
# عرض الواجهة
# ==========================================================

if language == "arabic":

    show_arabic_header()

else:

    show_english_header()


# ==========================================================
# البرنامج الرئيسي
# ==========================================================

while True:

    # ------------------------------------------
    # إدخال المستخدم
    # ------------------------------------------

    if language == "arabic":

        user = input("أنت: ").strip()

    else:

        user = input("You: ").strip()


    # ------------------------------------------
    # تجاهل الإدخال الفارغ
    # ------------------------------------------

    if not user:

        continue


    # ======================================================
    # EXIT
    # ======================================================

    if user.lower() == "/exit":

        print()

        if language == "arabic":

            print(
                f"SAI: إلى اللقاء يا "
                f"{memory.get('name', 'صفا')} 👋"
            )

        else:

            print(
                f"SAI: Goodbye, "
                f"{memory.get('name', 'Safa')}! 👋"
            )

        break


    # ======================================================
    # HELP
    # ======================================================

    if user.lower() == "/help":

        if language == "arabic":

            show_arabic_header()

        else:

            show_english_header()

        continue


    # ======================================================
    # حفظ الاسم
    # ======================================================

    if user.lower().startswith("/name "):

        name = user[6:].strip()


        if name:

            memory["name"] = name

            save_memory(memory)


            if language == "arabic":

                print(
                    f"SAI: حفظت اسمك: {name} 🧠❤️"
                )

            else:

                print(
                    f"SAI: I saved your name: {name} 🧠❤️"
                )

        else:

            if language == "arabic":

                print(
                    "SAI: اكتب اسمك بعد الأمر."
                )

            else:

                print(
                    "SAI: Enter your name after the command."
                )


        continue


    # ======================================================
    # حفظ الذاكرة
    # ======================================================

    if user.lower().startswith("/remember "):

        information = user[10:].strip()


        if information:

            memory["memories"].append(information)

            save_memory(memory)


            if language == "arabic":

                print(
                    "SAI: تم حفظ المعلومة في ذاكرتي 🧠"
                )

            else:

                print(
                    "SAI: Memory saved successfully 🧠"
                )

        else:

            if language == "arabic":

                print(
                    "SAI: اكتب المعلومة بعد /remember"
                )

            else:

                print(
                    "SAI: Enter something after /remember"
                )


        continue


    # ======================================================
    # عرض الذاكرة
    # ======================================================

    if user.lower() == "/memory":

        if not memory["memories"]:

            if language == "arabic":

                print("SAI: الذاكرة فارغة.")

            else:

                print("SAI: Memory is empty.")


        else:

            if language == "arabic":

                print("\nSAI - الذاكرة 🧠:")

            else:

                print("\nSAI - Memory 🧠:")


            for i, item in enumerate(
                memory["memories"],
                1
            ):

                print(f"{i}. {item}")


        continue


    # ======================================================
    # حذف ذاكرة
    # ======================================================

    if user.lower().startswith("/forget "):

        number = user[8:].strip()


        if number.isdigit():

            index = int(number) - 1


            if 0 <= index < len(memory["memories"]):

                deleted = memory["memories"].pop(index)

                save_memory(memory)


                if language == "arabic":

                    print(
                        f"SAI: تم حذف الذاكرة: "
                        f"{deleted} 🗑️"
                    )

                else:

                    print(
                        f"SAI: Memory deleted: "
                        f"{deleted} 🗑️"
                    )


            else:

                if language == "arabic":

                    print(
                        "SAI: رقم الذاكرة غير صحيح."
                    )

                else:

                    print(
                        "SAI: Invalid memory number."
                    )


        else:

            if language == "arabic":

                print(
                    "SAI: اكتب رقم الذاكرة، "
                    "مثال: /forget 2"
                )

            else:

                print(
                    "SAI: Enter the memory number, "
                    "example: /forget 2"
                )


        continue


    # ======================================================
    # مسح الذاكرة
    # ======================================================

    if user.lower() == "/clear":

        memory["memories"] = []

        save_memory(memory)


        if language == "arabic":

            print(
                "SAI: تم مسح الذاكرة 🗑️"
            )

        else:

            print(
                "SAI: Memory has been cleared 🗑️"
            )


        continue


    # ======================================================
    # سجل المحادثة
    # ======================================================

    if user.lower() == "/history":

        if not chat:

            if language == "arabic":

                print(
                    "SAI: لا توجد محادثات محفوظة."
                )

            else:

                print(
                    "SAI: There are no saved conversations."
                )


        else:

            if language == "arabic":

                print(
                    "\n===== سجل المحادثة ====="
                )

            else:

                print(
                    "\n===== Chat History ====="
                )


            for item in chat[-10:]:

                print()

                if language == "arabic":

                    print(
                        "أنت:",
                        item.get("user", "")
                    )

                    print(
                        "SAI:",
                        item.get("sai", "")
                    )

                else:

                    print(
                        "You:",
                        item.get("user", "")
                    )

                    print(
                        "SAI:",
                        item.get("sai", "")
                    )


                print("-" * 30)


        continue


    # ======================================================
    # الذكاء البسيط
    # ======================================================

    if language == "arabic":

        answer = sai_response_arabic(user)

    else:

        answer = sai_response_english(user)


    # ======================================================
    # عرض الإجابة
    # ======================================================

    print()

    print("SAI:", answer)

    print()


    # ======================================================
    # حفظ المحادثة
    # ======================================================

    save_message(user, answer)
