from whispers.cli import parse_args
from whispers.core import run

src = "tests/fixtures"
configfile = "../whis.yml"
args = parse_args(["-c", configfile, src])
for secret in run(args):
  print(secret)