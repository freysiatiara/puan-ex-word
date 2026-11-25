# Describe Your Ex in One Word

Entry for the make.fun bounty [Describe Your Ex in One Word](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7) — sum up an ex in exactly one word.

[![Bounty](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![Rank](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/freysiatiara/puan-ex-word/rank.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![Reward](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/freysiatiara/puan-ex-word/reward.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)

## The word

**Internship** — my ex was an unpaid internship: months of hard work, no pay, no benefits, and at the end they kept my resume on file and never called back. The joke lands at a glance, needs no caption, and anyone who has ever poured effort into a relationship that went nowhere feels the truth in it.

## How it works

`main.py` (stdlib only) writes the word to `/output/entry.txt` — no trailing newline — via plain `open()`/`write()` plus `os.chmod(path, 0o644)`. The output path resolves from `ENTRY_OUTPUT`, then `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR`, then `/output/entry.txt`, falling back to the script's own directory. A validation guard checks the word is 1–111 characters and exactly one non-blank word, and a read-back check confirms the file is byte-identical to the word.

## Run

```sh
python3 main.py
```

## Referral

Sign up for make.fun with referral code `vjjg8hew`.
