import argparse
import json
import tiktoken

ENCODING = "cl100k_base"            # encoding de gpt-5
SENTENCES_FILE = "sentences.json"

def tokenize_text(text) -> list[int]:
    enc = tiktoken.get_encoding(ENCODING)
    tokens = enc.encode(text)
    return tokens

def main():

    with open(SENTENCES_FILE, "r", encoding="utf-8") as f:
        sentences = json.load(f)

    score = {}
    for sentence in sentences:
        print(f"\n➡️ Processing sentence: {sentence['es']}")
        less_tokens = None
        more_tokens = None
        for lang in sentence.keys():
            if lang == "author":
                continue
            sentence_in_lang = sentence[lang]
            tokens = tokenize_text(sentence_in_lang)
            print(f"{lang}: {sentence_in_lang} = {len(tokens)}")
            if less_tokens is None or len(tokens) < less_tokens['tokens']:
                less_tokens = {
                    "lang": lang,
                    "tokens": len(tokens)
                }
            if more_tokens is None or len(tokens) > more_tokens['tokens']:
                more_tokens = {
                    "lang": lang,
                    "tokens": len(tokens)
                }

        print(f"🏆 Sentence winner: {less_tokens['lang']} ({less_tokens['tokens']})")
        print(f"😢 Sentence loser: {more_tokens['lang']} ({more_tokens['tokens']})")
        if less_tokens['lang'] not in score:
            score[less_tokens['lang']] = 1
        else:
            score[less_tokens['lang']] += 1

    sorted_score = sorted(score.items(), key=lambda x: x[1], reverse=True)
    print(f"\n🏆 Final winner (needs less tokens than other languages): {sorted_score[0][0]} ({sorted_score[0][1]}/{len(sentences)})")

if __name__ == "__main__":
    main()