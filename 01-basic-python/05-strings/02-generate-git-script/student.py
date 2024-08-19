# Write your code here
from textwrap import dedent

def generate_git_script(id):
  string = '''
  if [ ! -d {} ]; then
      git clone https://github.com/{}/project {}
  else
      (cd {}; git pull)
  fi
  '''.format(id,id,id,id)
  return dedent(string).strip()
