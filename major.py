# Print all major scales
# Ricardo Bittencourt 2017

notes = "C.D.EF.G.A.B"
names = "CDEFGAB"
steps = [0,2,2,1,2,2,2]

def notename(name, accent):
    if accent == 0:
        return name
    elif accent > 0:
        return name + "b" * accent
    else:
        return name + "#" * (-accent)

def findnote(note, name):
    search = [0,-1,1,-2,2,-3,3]
    for s in search:
        pos = (note + s + 12) % 12
        if notes[pos] == name:
            return notename(name, s)

def scale(note, name):
    ans = []    
    for step, name in zip(steps, (names + names)[names.index(name):]):
        note = (note + step) % 12
        ans.append(findnote(note, name))
    return "".join(ans)


def tonote(note_str):
    note = notes.index(note_str[0])
    if len(note_str) == 1:
        return (note, note_str)
    if note_str[1] == "#":
        note += 1
    else:
        note += 11
    return (note % 12, note_str[0])


for note in "CDEFGAB":
  print scale(*tonote(note))
  print scale(*tonote(note+"#"))
  print scale(*tonote(note+"b"))
