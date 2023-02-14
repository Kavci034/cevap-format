import json

class formatter:
    conf = None

    def configure(self, def_filepath):
        f = open(def_filepath)
        txt = f.read()
        self.conf = json.loads(txt)
        f.close()
    
    def format(self, text):
        new_text = text
        new_text = new_text.replace(self.conf['separator'], self.conf['new-separator'])
        opt_sep = '\n' if self.conf['use-newlines'] else ' '
        for opt in self.conf['options']:
            new_text = new_text.replace(f'{opt} ', f'{opt}{opt_sep}')
        return new_text
