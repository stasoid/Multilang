from __future__ import print_function
import befunge_exec as bf, brainfuck as b, replacefuck as rf, eitherfuck as ef, rand as r, os
print("""
+-----------------------------------+
|     Multilang esoteric shell      |
|            by TieSoul             |
|  Replacefuck (rf), Befunge (bf),  |
|  Brainfuck (b), Eitherfuck (ef),  |
|             Random (r)            |
|           are supported.          |
+-----------------------------------+"""
)
dir = os.getcwd()
while True:
    try:
        c = input(dir + '>> ')
        a = c.split()
        langs = ['ef', 'bf', 'b', 'rf', 'r']
        for i in langs:
            exec("%scode = ''" % i)
        if c.lower() in langs:
            while True:
                try:
                    exec("%scode = %scode + input('%s> ') + '\\n'" % (c.lower(), c.lower(), c.lower()))
                except KeyboardInterrupt:
                    break
                except:
                    try:
                        print()
                    except KeyboardInterrupt:
                        break
                    except:
                        print("An error occurred.")
        elif a[0].lower() in langs:
            exec("%scode = c[len(a[0])+1:]" % a[0].lower())
        elif a[0].lower() == 'exit':
            break
        elif a[0].lower() == 'help':
            print("""List of commands:
<programming language> <code>: execute code in programming language
<programming language>: enter code environment for programming language
cd: go to directory
dir: list files
f <programming language> <file>: execute file in programming language
ctrl+C: exit an environment and execute code
exit: exit the shell

List of languages:
bf - befunge
b  - brainfuck
rf - replacefuck
ef - eitherfuck
r  - random""")
        elif a[0].lower() == 'cd':
            try:
                os.chdir(c[3:])
            except:
                pass
            dir = os.getcwd()
        elif c.lower() == 'dir':
            os.system('dir')
        elif a[0].lower() == 'f':
            if a[1].lower() in langs:
                if os.path.exists(a[2]):
                    exec("%s.execute(open(a[2]).read())" % a[1].lower())
                    print()
        for i in langs:
            exec("if %scode != '': %s.execute(%scode); print()" % (i, i, i))
    except KeyboardInterrupt:
        pass
    except:
        try:
            input()
        except KeyboardInterrupt:
            pass
        except:
            print("An error has occurred.")