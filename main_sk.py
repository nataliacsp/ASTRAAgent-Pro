from astra_agent import initialize_kernel

def main():
    kernel = initialize_kernel()

    user = "natalia"
    date = "April 29, 2025"
    content = (
        "Today I deployed ASA Pro with a fully functioning journal system. "
        "She can now summarize what I say, detect my mood, and log everything in a neat, organized way. "
        "This feels like a major breakthrough in my AI journey. I'm proud of what I built!"
    )

    result = kernel.skills["journal"].save_journal_entry(user, date, content)
    print(result)

if __name__ == "__main__":
    main()
