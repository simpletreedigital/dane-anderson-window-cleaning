import re, glob

def fix(html):
    count = [0]
    def repl(m):
        count[0] += 1
        if count[0] == 1:
            return m.group(0)
        opentag = re.sub(r'^<h2', '<h3', m.group(0))
        opentag = re.sub(r'</h2>$', '</h3>', opentag)
        return opentag
    new_html = re.sub(r'<h2(?:\s[^>]*)?>.*?</h2>', repl, html, flags=re.S)
    return new_html

for f in glob.glob('/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/**/index.html', recursive=True):
    html = open(f).read()
    new_html = fix(html)
    if new_html != html:
        open(f, 'w').write(new_html)
        print('fixed', f)
