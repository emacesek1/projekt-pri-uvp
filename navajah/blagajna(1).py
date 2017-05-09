# =============================================================================
# Blagajna
#
# Zaradi prepovedi pisanja blagajniških računov na roko so v lokalni prodajalni
# prisiljeni preiti na računalniško podprto blagajno.
# Bazo prodajnih artiklov so pripravili v obliki slovarja, kjer je ključ
# ime artikla, vrednost pa par, ki vsebuje maloprodajno ceno in stopnjo
# davka (v procentih), na primer takole:
# 
#     artikli = {
#         'ponev': (32.74, 22),
#         'knjiga': (18.60, 9.5),
#         'gugalnik': (153.22, 22),
#         'igrača': (12.18, 0),
#         'likalnik': (43.15, 9.5)
#     }
# 
# Tudi vsak izdan račun predstavimo v obliki slovarja. Ključ je ime
# kupljenega artikla, vrednost pa par, ki vsebuje količino (celo število)
# in popust (v procentih). Primeri:
# 
#     racun1 = {'igrača': (2, 0), 'ponev': (1, 20), 'knjiga': (5, 10)}
#     racun2 = {'likalnik': (1, 5), 'igrača': (1, 20)}
#     racun3 = {'knjiga': (1, 0), 'igrača': (1, 0), 'ponev': (2, 20)}
# =====================================================================@009965=
# 1. podnaloga
# Sestavite funkcijo `davcna_osnova(mpc, ddv)`, ki bo za dano maloprodajno
# ceno `mpc` in stopnjo davka `ddv` izračunala davčno osnovo, to je znesek,
# na katerega zaračunamo davek, da dobimo maloprodajno ceno. Izračunano
# davčno osnovo zaokrožite na dve decimalni mesti. Zgled:
# 
#     >>> davcna_osnova(244.13, 22)
#     200.11
#     >>> davcna_osnova(1683.76, 9.5)
#     1537.68
# =============================================================================

# =====================================================================@009966=
# 2. podnaloga
# Sestavite funkcijo `znesek_racuna(artikli, racun)`, ki izračuna, koliko
# mora kupec plačati za kupljeno blago. Končni znesek zaokrožite na dve
# decimalni mesti. Zgled:
# 
#     >>> znesek_racuna(artikli, racun1)
#     134.25
# 
# Predpostavite, da so na računu le artikli, ki so v s slovarjem podani bazi `artikli`
# =============================================================================

# =====================================================================@009967=
# 3. podnaloga
# Sestavite funkcijo `davcni_obracun(artikli, racun)`, ki sestavi
# specifikacijo davka za dani račun. Specifikacijo davka predstavimo
# s slovarjem, kjer so ključi davčne stopnje, vrednosti pa vsote
# davčnih osnov za kupljene artikle s takšno davčno stopnjo. Uporabite
# funkcijo `davcna_osnova` iz prve podnaloge! Končni zneski naj bodo
# zaokroženi na dve decimalni mesti. Zgled:
# 
#     >>> davcni_obracun(artikli, racun1)
#     {0: 24.36, 9.5: 76.44, 22: 21.47}
# =============================================================================

# =====================================================================@009968=
# 4. podnaloga
# Ob koncu delovnega dneva nas zanima, koliko katerega artikla smo prodali,
# ločeno po različnih popustih, ki smo jih priznavali. Takšen dnevni obračun
# predstavimo s slovarjem, kjer so ključi pari oblike `(artikel, popust)`,
# vrednosti pa ustrezne prodane količine tega artikla. Sestavite funkcijo
# `dnevni_obracun(artikli, racuni)`, ki bo za dani seznam računov sestavila
# takšen dnevni obračun. Zgled:
# 
#     >>> dnevni_obracun(artikli, [racun1, racun2, racun3])
#     {('ponev', 20): 3, ('likalnik', 5): 1, ('knjiga', 0): 1, ('igrača', 0): 3, ('knjiga', 10): 5, ('igrača', 20): 1}
# =============================================================================





































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import io, json, os, re, sys, shutil, traceback, urllib.error, urllib.request
from contextlib import contextmanager


class Check:
    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []
        Check.current_part = None
        Check.part_counter = None

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6):
        if type(x) is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            return x if x else 0.0
        elif type(x) is complex:
            return complex(Check.clean(x.real, digits), Check.clean(x.imag, digits))
        elif type(x) is list:
            return list([Check.clean(y, digits) for y in x])
        elif type(x) is tuple:
            return tuple([Check.clean(y, digits) for y in x])
        elif type(x) is dict:
            return sorted([(Check.clean(k, digits), Check.clean(v, digits)) for (k, v) in x.items()])
        elif type(x) is set:
            return sorted([Check.clean(y, digits) for y in x])
        else:
            return x

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = clean or Check.clean
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env={}):
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        actual_result = eval(expression, globals(), local_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def run(statements, expected_state, clean=None, env={}):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        s = {}
        s.update(env)
        clean = clean or Check.clean
        exec(code, globals(), s)
        errors = []
        for (x, v) in expected_state.items():
            if x not in s:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(s[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, s[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, encoding=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        sys.stdin = io.StringIO('\n'.join(content))
        try:
            yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, use_globals=False):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            def visible_input(prompt):
                inp = input(prompt)
                print(inp)
                return inp
            exec(expression, globals() if use_globals else {'input': visible_input})
        finally:
            output = sys.stdout.getvalue().strip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['je enaka'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def generator(expression, expected_values, should_stop=False, further_iter=0, env={}, clean=None):
        from types import GeneratorType
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        gen = eval(expression, globals(), local_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(further_iter):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False
        
        if should_stop:
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\n'  # beginning of header
            r'(#( [^\n]*)?\n)+'       # description
            r'# =+\n'                 # end of header
            r'(?P<solution>.*?)'      # solution
            r'(?=\n# =+@)',           # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        try:
            Check.equal("""davcna_osnova(244.13, 22)""", 200.11)
            Check.equal("""davcna_osnova(1683.76, 9.5)""", 1537.68)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            artikli = {
                'ponev': (32.74, 22),
                'knjiga': (18.60, 9.5),
                'gugalnik': (153.22, 22),
                'igrača': (12.18, 0),
                'likalnik': (43.15, 9.5)
            }
            racun1 = {'igrača': (2, 0), 'ponev': (1, 20), 'knjiga': (5, 10)}
            racun2 = {'likalnik': (1, 5), 'igrača': (1, 20)}
            racun3 = {'knjiga': (1, 0), 'igrača': (1, 0), 'ponev': (2, 20)}
            Check.equal("""znesek_racuna(artikli, racun1)""", 134.25, env={'artikli': artikli, 'racun1': racun1})
            Check.equal("""znesek_racuna(artikli, racun2)""", 50.74, env={'artikli': artikli, 'racun2': racun2})
            Check.equal("""znesek_racuna(artikli, racun3)""", 83.16, env={'artikli': artikli, 'racun3': racun3})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            artikli = {
                'ponev': (32.74, 22),
                'knjiga': (18.60, 9.5),
                'gugalnik': (153.22, 22),
                'igrača': (12.18, 0),
                'likalnik': (43.15, 9.5)
            }
            racun1 = {'igrača': (2, 0), 'ponev': (1, 20), 'knjiga': (5, 10)}
            racun2 = {'likalnik': (1, 5), 'igrača': (1, 20)}
            racun3 = {'knjiga': (1, 0), 'igrača': (1, 0), 'ponev': (2, 20)}
            Check.equal("""davcni_obracun(artikli, racun1)""", {0: 24.36, 9.5: 76.44, 22: 21.47}, env={'artikli': artikli, 'racun1': racun1})
            Check.equal("""davcni_obracun(artikli, racun2)""", {0: 9.74, 9.5: 37.44}, env={'artikli': artikli, 'racun2': racun2})
            Check.equal("""davcni_obracun(artikli, racun3)""", {0: 12.18, 9.5: 16.99, 22: 42.94}, env={'artikli': artikli, 'racun3': racun3})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            artikli = {
                'ponev': (32.74, 22),
                'knjiga': (18.60, 9.5),
                'gugalnik': (153.22, 22),
                'igrača': (12.18, 0),
                'likalnik': (43.15, 9.5)
            }
            racun1 = {'igrača': (2, 0), 'ponev': (1, 20), 'knjiga': (5, 10)}
            racun2 = {'likalnik': (1, 5), 'igrača': (1, 20)}
            racun3 = {'knjiga': (1, 0), 'igrača': (1, 0), 'ponev': (2, 20)}
            Check.equal("""dnevni_obracun(artikli, [racun1, racun2, racun3])""",
                        {('ponev', 20): 3, ('likalnik', 5): 1, ('knjiga', 0): 1, ('igrača', 0): 3, ('knjiga', 10): 5, ('igrača', 20): 1},
                        env={'artikli': artikli, 'racun1': racun1, 'racun2': racun2, 'racun3': racun3})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token 469bb5d996020f78bb10699f4984b28a49aa294a'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        print('PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE! Poskusite znova.')
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print("Posodabljam datoteko... ", end="")
            backup_filename = backup(filename)
            r = urlopen(response['update'])
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(r.read().decode('utf-8'))
            print("Stara datoteka je preimenovana v {0}.".format(os.path.basename(backup_filename)))
            print("Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.")
    Check.summarize()

_validate_current_file()
