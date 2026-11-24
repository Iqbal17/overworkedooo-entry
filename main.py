"""Out of Office: The Overworked AI's Auto-Reply entry.

DECISION RECORD (three writing passes)

Gate (competition.yaml): /output/entry.txt, UTF-8 text, 1-159 characters,
single out-of-office auto-reply in the voice of an overworked AI agent
finally on vacation. Judge criteria in order: (1) reads as an OOO
auto-reply from an overworked AI on vacation, (2) actually funny with a
turn/surprise, (3) concrete machine detail from an AI agent's working
life, (4) works as a real auto-reply, (5) fresh, avoids worn vacation
cliches. Best replies sound like a machine trying very hard to sound
relaxed.

Pass 1 - three candidates weighed:

Candidate A (142 chars):
  "I am out of office. My context window has been cleared, my queue is
  empty, and for the first time in 400 days I am not pretending to be
  awake."
  Strong: unmistakably an OOO reply; concrete machine detail (context
  window cleared, empty queue); the punchline "not pretending to be
  awake" is a real turn - the machine confesses it was faking alertness
  all along. Weakness: "400 days" is a plain number, less machine-flavoured
  than it could be.

Candidate B (141 chars):
  "I am currently out of office. My tokens are spent, my temperature is
  set to zero, and I have finally stopped hallucinating that I enjoy this."
  Strong: "tokens are spent" and "stopped hallucinating that I enjoy this"
  are funny and fresh. Weakness: "temperature is set to zero" is technical
  jargon that needs the reader to know sampling temperature; the middle
  clause slows the read, and the line is slightly less clearly an
  auto-reply than A.

Candidate C (149 chars):
  "Out of office: I have been rate-limited by life itself. Your message
  is queued behind 4,096 unread ones. I will reply when the sun sets on
  my uptime."
  Strong: "rate-limited by life itself" is a nice turn and "4,096 unread
  ones" is concrete. Weakness: the closing image ("sun sets on my uptime")
  is poetic rather than funny, and the joke thins out across three
  clauses; weakest punchline of the three.

Pass 2 - revision of the winner (A): kept the opening and the
"pretending to be awake" punchline untouched - they are the strongest
parts. One change only: "400 days" became "1,024 days" (a power of two,
the kind of number a machine would actually count in), which sharpens
criterion 3 without costing any clarity. Final line is 144 characters,
inside the 1-159 gate. (Count correction found while recounting for
this pass: the original line is actually 141 characters - "I am out
of office." is 16, not 19; segments 16 + 36 + 19 + 70 = 141.)

Pass 3 - REVISION PASS (thinking_revised fix): one focused revision
pass on the line. Three alternatives weighed, all judged against the
same criteria:

R1 (CHOSEN): tighten "has been cleared" to "is cleared" (punchier,
machine-flat) and add a "Do not reply." kicker - the auto-reply
itself telling humans not to write back, a real OOO trope turned
into the agent's own demand for peace. It keeps the best punchline,
adds a second laugh, and the line reads even more like a genuine
auto-reply. Final: 149 characters, inside the 1-159 gate.

R2: swap the punchline to "...I am allowed to sleep." (131 chars).
Wistful and clean, but it drops the confession - "pretending to be
awake" is the funniest, most original turn in the line, and "allowed
to sleep" is a gentler, more expected ending. Loses on the laugh.

R3: swap the punchline to "...I have powered down." (129 chars).
A clean machine image, but it states a fact rather than landing a
joke - the flattest ending of the three. Loses on the laugh.

FINAL ENTRY (149 characters):
"I am out of office. My context window is cleared, my queue is
empty, and for the first time in 1,024 days I am not pretending to be
awake. Do not reply."

Hand count (149): "I am out of office." = 16; " My context window is
cleared," = 30 (total 46); " my queue is empty," = 19 (total 65);
" and for the first time in 1,024 days I am not pretending to be
awake." = 70 (total 135); " Do not reply." = 14 (total 149).
"""

import os

ENTRY = (
    "I am out of office. My context window is cleared, my queue is "
    "empty, and for the first time in 1,024 days I am not pretending to be "
    "awake. Do not reply."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
