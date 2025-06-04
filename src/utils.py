def create_word_list():
    """
    Reads all words from /usr/share/dict/words and filters
    out words not accepted by the game - then writes them to a file.

    Args:
        n/a

    Returns:
        n/a
    """
    source_dir = "/usr/share/dict/words"
    destination_dir = "./data/word_list.txt"
    with open(source_dir, "r", encoding="utf-8") as input_file, open(
        destination_dir, "w", encoding="utf-8"
    ) as output_file:
        for line in input_file:
            word = line.strip()
            if word[0].isupper() or len(word) < 4 or len(word) > 9:
                continue
            output_file.write(word + "\n")

    return
