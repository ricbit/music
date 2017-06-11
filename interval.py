# Print all chromatic intervals
# Ricardo Bittencourt 2017

import itertools

notes = "C.D.EF.G.A.B"
names = "CDEFGAB"
perfects = [1, 0, 0, 1, 1, 0, 0]
tones = [0, 2, 4, 5, 7, 9, 11]

def notename(name, accent):
    if accent == 0:
        return name
    elif accent > 0:
        return name + "b" * accent
    else:
        return name + "#" * (-accent)

def spiral():
    yield 0
    for x in itertools.count(1):
        yield -x
        yield x

def findnote(note, name):
    for s in spiral():
        pos = (note + s + 12) % 12
        if notes[pos] == name:
            return notename(name, s)

def tonote(note_str):
    note = notes.index(note_str[0])
    if len(note_str) == 1:
        return (note, note_str, note_str)
    if note_str[1] == "#":
        note += 1
    else:
        note += 11
    return (note % 12, note_str[0], note_str)

def allnotes():
    for note in "CDEFGAB":
        yield tonote(note)
        yield tonote(note+"#")
        yield tonote(note+"b")

def allintervals():
    for interval, perfect in enumerate(perfects):
        if perfect:
            for semitone, name in zip([-1,0,1], "dPA"):
                yield (interval, semitone, name + str(1 + interval))
        else:
            for semitone, name in zip([-2,-1,0,1], "dmMA"):
                yield (interval, semitone, name + str(1 + interval))

print """
    <html><head><style>
    table {
        border-collapse: collapse;
        border: 1px solid gray;
    }
    th {
        background-color: #4CAF50;
        color: white;
    }
    td:first-child {
        background-color: #4CAF50;
        color: #f0f080;
        font-weight: bold;
    }
    tr:nth-child(odd) {background-color: #e2e2e2;}
    tr:nth-child(odd) > td:first-child {background-color: #3c9f40;}
    th,td {
        border-left: 1px solid black;
        padding: 5px;
    }
    .major {
        color: red;
    }
    </style></head><body><table><tr><th></th>
"""
for interval, semitone, iname in allintervals():
    print "<th>%s</th>" % iname
print "</tr>"
for tone, note, name in allnotes():
    print "<tr><td>%s</td>" % name
    for interval, semitone, iname in allintervals():
        newname = names[(names.index(note) + interval) % 7]
        print "<td %s>%s</td>" % (
            'class="major"' if semitone == 0 else '',
            findnote(tone + tones[interval] + semitone, newname))
    print "</tr>"
print "</body></html>"



