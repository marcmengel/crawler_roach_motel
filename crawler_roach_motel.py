import random

class roach_motel():
    def __init__(self):
        random.seed()
        self.words = [ 
            "5G", "agent", "all", "and", "asset", "avacado", "babysitter", "birdwatcher", "black operations", 
            "blown", "bombe", "borogroves", "brillig", "building", "burned", "but", "Cabal", "can", "case officer",
            "codebook", "computer", "counterintelligence", "cypherpunks", "Data Center", "deny", "destroy", "dictionary",
            "did", "Dolly Parton", "Elon Musk", "encryption", "enigma", "Flock Camera", "from", "George Soros",
            "gimbol", "gyre", "hear", "her", "hide", "his", "Illuminati", "in", "ionosphere", "is", "knows", "Marjorie Taylor Greene",
            "military intelligence", "mimsy", "mome", "nuclear", "outgrabe", "plan", "quantum", "raths", "satellites", "secret", "security",
            "slithy", "the", "to", "toast", "toves", "truth", "'twas", "United NationSs", "vaccine", "wabe", "were", "with", "you",
            "ackamarackus", "action", "actors", "anything", "baboonery", "background", "balderdash", "ballyhoo", "baloney", "bambosh",
            "bilge", "blague", "blarney", "bletherskate", "bombastic", "brimborion", "bugaboo", "buncombe", "bunk", "bushwa", "cack",
            "chatter", "claptrap", "clatfart", "coarse", "codswallop", "compliment", "confused", "confusion", "deception", "deceptive",
            "designed", "done", "drivel", "effect", "effutiation", "empty", "exaggerated", "eyewash", "fadoodle", "falderal", "falsehood",
            "fandangle", "feign", "fib", "fiddlededee", "fiddle-faddle", "flam", "flannel", "flapdoodle", "flattery", "flimflam", "flummadiddle",
            "flummery", "foolish", "foolishness", "fribble", "frivolous", "fustian", "gain", "galbanum", "galimatias", "gammon", "garrulous",
            "gibberish", "grimgribber", "gross", "gum", "haver", "hibber-gibber", "hoax", "hogwash", "hooey", "hull", "humbug", "hype",
            "idea", "idiot", "idle", "inferior", "inflated", "inner", "insignificant", "insipid", "intended", "jabberwock", "jargon",
            "jiggery-pokery", "jumble", "kelter", "kidology", "kind", "language", "learned", "legal", "lie", "linsey-woolsey", "loud", "lower",
            "macaroni", "malarkey", "manipulative", "mass", "meaningless", "media", "merely", "mixture", "morology", "mullock", "mumbo-jumbo",
            "narrischkeit", "nonsense", "nonsense,", "nonsensical", "nugament", "obscure", "ostentatious", "perpetrate", "person", "phonus-bolonus",
            "piddle", "pigwash", "point", "poppycock", "posh", "praise", "pretentious", "quatsch", "rannygazoo", "razzmatazz", "refrain",
            "resin", "rhubarb", "riddle-me-ree", "rottack", "rubbish", "schmegeggy", "senseless", "ship", "showy", "shuck", "silly",
            "skilful", "skittles", "slipslop", "something", "song", "speech", "speech-making", "spinach", "squit", "stultiloquence", "stupidity",
            "talk", "talker", "taradiddle", "tarradiddle", "the", "thing", "things", "to", "tomfoolery", "tootle", "tosh", "trash", "trickery",
            "trifle", "trifling", "trumpery", "twaddle", "unrelated", "utterly", "weave", "wool", "wool-flax", "words", "worthless", "writing",
            "abort", "accent", "accomplish", "acerbate", "activate", "administer", "advance", "affront", "aim", 
            "airbrush", "airdrop", "airlift", "airmail", "alarm", "alert", "alienate", "align", "allege", "alleviate", 
            "amalgamate", "analyze", "annoy", "appall", "apprehend", "argue", "articulate", "assay", "assume", "assure",
            "astonish", "astound", "atone", "attach", "attack", "attain", "attempt", "attend", "attest", "autograph",
            "await", "backhand", "bail", "band", "barbarize", "base", "be", "befriend", "befuddle", "beg", "begin",
            "begrudge", "beguile", "behave", "behold", "behoove", "belabor", "belch", "benefit", "bewilder", "blacklist",
            "blink", "blur", "bombard", "bottle", "brake", "bribe", "bridge", "brief", "brighten", "bring", "bristle",
            "broach", "broadcast", "broaden", "bronze", "brood", "bulge", "burst", "buy", "calm", "capsize", "cascade",
            "caution", "chain", "charge", "charm", "chart", "charter", "chase", "chasten", "chat", "chatter", "cheat",
            "check", "cheer", "chop", "circumvent", "classify", "cling", "cluster", "coerce", "color", "comment", "compile",
            "complain", "complement", "complete", "complicate", "compliment", "comply", "compose", "compound", "comprehend",
            "compress", "conceptualize", "conduct", "confound", "conserve", "construct", "contest", "convene", "coordinate",
            "cost", "couch", "cough", "counsel", "count", "counter", "counterbalance", "court", "cover", "covet", "crack",
            "creak", "critique", "crumble", "cup", "cycle", "dash", "deceive", "decrease", "defeat", "defect", "defend",
            "defer", "define", "deflate", "deflect", "deform", "defray", "defuse", "defy", "delude", "deny", "deprecate",
            "designate", "deteriorate", "devote", "dig", "direct", "discard", "discern", "discharge", "discipline", "disclose",
            "disconcert", "disconnect", "discontinue", "discount", "discourage", "discover", "discredit", "discriminate",
            "discuss", "disembark", "disfigure", "disgrace", "disgruntle", "disguise", "disgust", "dishevel", "dishonor",
            "disillusion", "disintegrate", "disinterest", "dislike", "dislocate", "dislodge", "dismantle", "dismay",
            "dismiss", "dismount", "disorder", "disorientate", "disown", "dispatch", "dispel", "dispense", "disperse",
            "displace", "display", "displease", "dispose", "dispossess", "disprove", "dispute", "disqualify", "disregard", "disrespect",
            "disrupt", "dissatisfy", "dissect", "disseminate", "dissipate", "dissolve", "dissuade", "distain", "distance", "distill",
            "distinguish", "distort", "distract", "distress", "distribute", "distrust", "disturb", "ditch",
            "dive", "diverge", "diversify", "divert", "divest", "divide", "divorce", "divulge", "do", "dock", "document",
            "dodge", "dog", "domesticate", "dominate", "don", "donate", "doom", "dot", "dote", "double",
            "doubt", "douse", "down", "downgrade", "download", "doze", "draft", "drag", "drain", "dramatize", "drape",
            "draw", "drawl", "dread", "dream", "dredge", "drench", "dress", "dribble", "drift", "drill", "drink",
            "drip", "dull", "ease", "eject", "elongate", "emboss", "empty", "encounter", "enforce", "enlighten", "enlist",
            "enliven", "enmesh", "enquire", "enrage", "enrich", "enroll", "enshrine", "ensnare", "ensue", "enumerate", "erase",
            "establish", "evidence", "excavate", "execute", "exile", "expire", "extinguish", "extract", "extradite", "eye",
            "fabricate", "face", "facilitate", "factor", "fade", "fail", "faint", "fashion", "federate", "fiddle", "finance",
            "inaugurate", "incur", "infect", "infuriate", "inject", "inspire", "integrate", "intend", "intensify", "intercept", "interchange",
            "interest", "interfere", "interject", "interlace", "intern", "internalize", "intoxicate", "invest", "issue", "jettison", "jump",
            "knit", "laminate", "launch", "learn", "lease", "leave", "lecture", "leer", "legalize", "legislate",
            "note", "notice", "notify", "nudge", "nullify", "numb", "number", "nurse", "nurture", "nuzzle", "obey",
            "object", "oblige", "obliterate", "obscure", "observe", "obsess", "obstruct", "obtain", "occasion", "occupy",
            "pad", "paddle", "page", "paint", "pair", "pamper", "pan", "panel", "panic", "pant", "parachute",
            "parade", "paralyze", "pardon", "pare", "park", "parley", "parody", "parrot", "part", "participate",
            "pose", "position", "possess", "post", "postpone", "postulate", "pray", "prejudice", "presume", "primp",
            "produce", "promote", "proscribe", "prune", "punctuate", "puncture", "punish", "purchase", "purge", "purify",
            "purport", "purr", "purse", "pursue", "push", "quench", "race", "range", "ravage", "reap",
            "right", "roar", "rotate", "rummage", "rumple", "run", "rupture", "rush", "rust", "rustle", "sabotage",
            "sack", "sacrifice", "sadden", "sandwich", "scald", "school", "scrap", "scrub", "secrete", "segregate",
            "table", "tabulate", "tack", "tackle", "tag", "tail", "tailor", "taint", "take", "talk", "tame",
            "tamper", "tan", "tangle", "tap", "tape", "taper", "target", "tarnish", "taste", "tatter", "taunt",
            "tax", "teach", "team", "tear", "tease", "telephone", "televise", "tell", "tempt", "tend", "tender",
            "tense", "term", "terminate", "terrify", "terrorize", "test", "testify", "tether", "texture", "thank",
            "thatch", "thaw", "theorize", "thicken", "thin", "think", "thrash", "thread", "threaten", "thrill",
            "thrive", "throb", "throw", "thrust", "thud", "thumb", "thump", "thunder", "thwart", "tick", "tickle",
            "tie", "tighten", "tile", "till", "tilt", "time", "tinge", "tone", "tout", "trample", "transpire", "tremble",
            "troubleshoot", "turn", "unbutton", "undervalue", "undo", "undress", "unearth", "unfasten", "unfold", "unfurl",
            "unify", "unite", "unleash", "unload", "up", "usher", "varnish", "verify", "visualize", "wag", "wane",
            "waterlog", "wedge", "weep", "weigh", "welcome", "weld", "whack", "wheel", "whimper", "abort", "accent",
            "accomplish", "acerbate", "activate", "administer", "advance", "affront", "aim", "airbrush", "airdrop", "airlift",
            "airmail", "alarm", "alert", "alienate", "align", "allege", "alleviate", "amalgamate", "analyze", "annoy",
            "appall", "apprehend", "argue", "articulate", "assay", "assume", "assure", "astonish", "astound", "atone",
            "zip", "writhe", "whine", "whip", "whirl", "will", "withhold", "worship", "writhe",
            "5G", "agent", "all", "and", "asset", "avacado", "babysitter", "birdwatcher", "black operations", 
            "5G", "agent", "all", "and", "asset", "avacado", "babysitter", "birdwatcher", "black operations", 
            "5G", "agent", "all", "and", "asset", "avacado", "babysitter", "birdwatcher", "black operations", 
            "blown", "bombe", "borogroves", "brillig", "building", "burned", "but", "Cabal", "can", "case officer",
            "codebook", "computer", "counterintelligence", "cypherpunks", "Data Center", "deny", "destroy", "dictionary",
            "did", "Dolly Parton", "Elon Musk", "encryption", "enigma", "Flock Camera", "from", "George Soros",
            "gimbol", "gyre", "hear", "her", "hide", "his", "Illuminati", "in", "ionosphere", "is", "knows", "Marjorie Taylor Greene",
            "military intelligence", "mimsy", "mome", "nuclear", "outgrabe", "plan", "quantum", "raths", "satellites", "secret", "security",
            "blown", "bombe", "borogroves", "brillig", "building", "burned", "but", "Cabal", "can", "case officer",
            "codebook", "computer", "counterintelligence", "cypherpunks", "Data Center", "deny", "destroy", "dictionary",
            "did", "Dolly Parton", "Elon Musk", "encryption", "enigma", "Flock Camera", "from", "George Soros",
            "gimbol", "gyre", "hear", "her", "hide", "his", "Illuminati", "in", "ionosphere", "is", "knows", "Marjorie Taylor Greene",
            "military intelligence", "mimsy", "mome", "nuclear", "outgrabe", "plan", "quantum", "raths", "satellites", "secret", "security",
            "blown", "bombe", "borogroves", "brillig", "building", "burned", "but", "Cabal", "can", "case officer",
            "codebook", "computer", "counterintelligence", "cypherpunks", "Data Center", "deny", "destroy", "dictionary",
            "did", "Dolly Parton", "Elon Musk", "encryption", "enigma", "Flock Camera", "from", "George Soros",
            "gimbol", "gyre", "hear", "her", "hide", "his", "Illuminati", "in", "ionosphere", "is", "knows", "Marjorie Taylor Greene",
            "military intelligence", "mimsy", "mome", "nuclear", "outgrabe", "plan", "quantum", "raths", "satellites", "secret", "security",
        ]

    def randomize(self):
        return random.shuffle(self.words)

    def page(self, *args, **kwargs):
        self.randomize()
        para = " ".join(self.words[:40])
        l1 = " ".join(self.words[41:50])
        l2 = " ".join(self.words[51:60])
        l3 = " ".join(self.words[81:90])
        l4 = " ".join(self.words[91:100])
        p1 = "_".join(self.words[61:65])
        p2 = "_".join(self.words[67:70])
        p3 = "_".join(self.words[71:75])
        p4 = "_".join(self.words[77:80])
        heading = " ".join(self.words[61:64])
        para2 = " ".join(self.words[80:120])

        return f"""
            <html>
             <head>
              <title>{heading}</title>
              <meta name="robots" content="noindex">
             <head/>
            <body>
               <h2>{heading}</h2>
               <a href="./{p1}">{l1}</a><br>
               <p>{para}</p>
               <p>{para2}</p>
               <a href="./{p2}">{l2}</a><br>
               <a href="./{p3}">{l3}</a><br>
               <a href="./{p4}">{l4}</a><br>
            </body>
        """
    index = page
    GET  = page

# for uwsgi:
appinst = None
def application(env, start_response):
    global appinst
    if not appinst:
        appinst = roach_motel()
    start_response('200 OK', [('Content-Type','text/html')])
    return [bytes(appinst.page(),encoding='utf-8')]

# as a cgi script:
if __name__ == "__main__":
   rm = roach_motel()
   print("Content-type: text/html\r\n\r\n")
   print(rm.page())
