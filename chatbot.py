def chatbot():
    print("=" * 50)
    print("AI CAREER GUIDANCE CHATBOT")
    print("=" * 50)
    print("Type 'exit' to quit")

    while True:
        user = input("\nYou: ").lower()

        if user == "exit":
            print("Bot: Thank you! Good luck with your career.")
            break

        elif user == "career":
            print("\nBot: Career Options for CSE Students")
            print("1. AI Engineer")
            print("2. Data Scientist")
            print("3. Web Developer")
            print("4. Cybersecurity Analyst")
            print("5. Cloud Engineer")

        elif user == "ai":
            print("\nBot: AI Engineer")
            print("Skills Required:")
            print("- Python")
            print("- Machine Learning")
            print("- Deep Learning")

        elif user == "data science":
            print("\nBot: Data Scientist")
            print("Skills Required:")
            print("- Python")
            print("- SQL")
            print("- Statistics")

        elif user == "web":
            print("\nBot: Web Developer")
            print("Skills Required:")
            print("- HTML")
            print("- CSS")
            print("- JavaScript")

        elif user == "cybersecurity":
            print("\nBot: Cybersecurity Analyst")
            print("Skills Required:")
            print("- Networking")
            print("- Linux")
            print("- Ethical Hacking")

        elif user == "cloud":
            print("\nBot: Cloud Engineer")
            print("Skills Required:")
            print("- AWS")
            print("- Azure")
            print("- Docker")

        else:
            print("\nBot: Please type one of these:")
            print("career")
            print("ai")
            print("data science")
            print("web")
            print("cybersecurity")
            print("cloud")

chatbot()