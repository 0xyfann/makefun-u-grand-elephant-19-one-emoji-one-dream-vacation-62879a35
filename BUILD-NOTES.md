# Build notes

- Competition: u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35
  ("One Emoji, One Dream Vacation", $2, closes 28 Nov 2026 18:55 WIB).
- Gate (RULES.txt): entry.txt must be UTF-8 text of 1-8 characters, not
  only whitespace. Judge: pairwise, exactly one emoji naming a dream
  vacation, most evocative wins.
- Choice: 🏝 DESERT ISLAND (U+1F3DD). Considered 🏖️ (beach with umbrella,
  more generic-holiday), 🌅 (sunrise over sea, a mood more than a trip),
  and 🗻 (Mount Fuji, specific but reads as just a mountain). The desert
  island won: it plainly names the dream escape, is a vivid postcard at a
  glance, is specific (one island, not any holiday), and is universally
  readable.
- Deliberately no variation selector (U+FE0F): U+1F3DD defaults to emoji
  presentation, so the entry is 1 character / 4 bytes — the smallest
  possible text, which also wins the byte-count tie-break on an exact
  rate tie, and is byte-distinct from the common 🏝️ (with VS16) form.
- main.py written in two versions: v1 wrote the emoji literal; v2
  (revision) builds it from chr(0x1F3DD) and adds a self-check asserting
  the 1-8 character, non-whitespace gate before writing.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
  -> out/entry.txt = 🏝, 1 character, 4 bytes (f0 9f 8f 9d), gate passes.
  out/ removed after testing.
- Stdlib only (os). Honors MAKEFUN_OUTPUT_DIR, default /output.
