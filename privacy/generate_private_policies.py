import re
import os

# choose from the already existing templates or create a new one
policy_templates = {'voodoo': 'templates/policy_voodoo.mustache',
                    'other': 'templates/policy_other.mustache',
                    'wow': 'templates/policy_wow.mustache',
                    '4wheelers': 'templates/policy_4wheelers.mustache',
                    'aurora': 'templates/policy_aurora.mustache',
                    'lion': 'templates/policy_lion.mustache'}

# add the new game at the end of this list
GAMES = [
    ("Blocks Master 3D",'voodoo'),
    ("Swing Runner",'voodoo'),
    ("Beauty Salon 3D",'voodoo'),
    ("Drag Master",'other'),
    ("Morning Routine 3D",'other'),
    ("Emoji Master",'other'),
    ("Doctor Care",'other'),
    ("Differences 3D",'other'),
    ("Kelimekolik",'other'),
    ("Willy Wild",'other'),
    ("Magnet Master",'other'),
    ("Stack Dust 3D",'other'),
    ("Bump Rider",'other'),
    ("Billy Balance: Sniper",'other'),
    ("Dr. Florist",'other'),
    ("Captain Starla",'other'),
    ("Dr. Salon",'other'),
    ("Dance Masters",'other'),
    ("Aurora: Let Them Dye",'aurora'),
    ("4Wheelers",'4wheelers'),
    ("Slidroad",'other'),
    ("World of Words",'wow'),
    ("MalekAlKalamat",'wow'),
    ("Doctor Chem: Laboratory",'voodoo'),
    ("Ice Sling",'voodoo'),
    ("Quench Quest: Firefighter",'voodoo'),
    ("Moving Crew", 'voodoo'),
    ("Farming Fantasy", 'voodoo'),
    ("Hurry Party", 'lion'),
    ("Moving Inc", 'lion'),
    ("Hospitaller: Cure the Patients", 'voodoo'),
    ("Bakery Chef 3D", 'voodoo'),
    ("Bakery Inc", 'voodoo'),
]

HOME_URL = "https://joyixir.com"
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

with open('templates/template_for_python_script.html','r') as f:
    contents = f.readlines()
html_template_content = f"".join(contents)

overwrite_warning_count = 0
# if the filename of a policy already exists it does not update it, remove the
# existing filename in order for script to write the new one.
for game, policy in GAMES:
    filename = ''.join(g.lower() for g in game if not g.isspace() and g not in punc) + '.html'
    str_replaced = re.sub('\[NAME[0-9]+\]', f"'{game}'", html_template_content)
    str_replaced = re.sub('\[HOME\_URL[0-9]+\]', f"'{HOME_URL}'", str_replaced)
    str_replaced = re.sub('\[POLICY\_TEMPLATE\_NAME[0-9]+\]', f"'{policy_templates[policy]}'", str_replaced)
    # print(str_replaced) # for debugging
    if not os.path.exists(filename):
        with open(f'{filename}','w') as f:
            contents = f.write(str_replaced)
        print(f"{filename:27} --> created!")
    else:
        overwrite_warning_count += 1
        print(f"{filename:27} --> already exists, did not overwrite!")

if overwrite_warning_count > 0:
    print(f"\n {overwrite_warning_count} files were not updated because already exist. If you intend to update them, remove the previous file(s)!")
    print(f"\n contact or questions: novin@joyixir.com\n")
