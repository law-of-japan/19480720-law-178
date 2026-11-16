"""Re-run structural checks and trial invariants from any working directory."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

repo = Path(__file__).resolve().parents[1]
root = repo.parent
snapshot = json.loads((repo/'docs/trial-snapshot.json').read_text(encoding='utf-8'))
exe = root/'loj-validator/target/release/loj-validator.exe'
out = repo/'docs/validation'
out.mkdir(exist_ok=True)
first = repo/'versions'/snapshot['revisions']['enactment']
second = repo/'versions'/snapshot['revisions']['firstAmendment']
jobs = [(f'{name}-{level}', [str(path),'--level',level]) for name,path in [('enactment',first),('amendment',second)] for level in ['L0','L1']]
jobs += [('history-L3',[str(repo),'--level','L3']),('rebuild',[str(repo),'--check','rebuild']),('registry',[str(root/'loj-registry'),'--check','registry','--registration-space','law-of-japan']),('relations-L4',['--registry',str(root/'loj-registry'),'--repository',str(repo),'--level','L4','--registration-space','law-of-japan'])]
summary = []
for name,args in jobs:
    args = [str(Path(a).relative_to(root)).replace('\\','/') if a.startswith(str(root)) else a for a in args]
    cmd = [str(exe),'check']+args+['--format','json']
    result = subprocess.run(cmd,capture_output=True,cwd=root)
    (out/(name+'.json')).write_bytes(result.stdout)
    report = json.loads(result.stdout)
    summary.append({'name':name,'command':['loj-validator/target/release/loj-validator.exe']+cmd[1:],'exitCode':result.returncode,'results':report.get('results',[]),'stderr':result.stderr.decode('utf-8',errors='replace')})
    print(name, result.returncode)

before = (first/'main.md').read_bytes()
after = (second/'main.md').read_bytes()
pattern = rb'<!-- loj:row key=([a-z0-9]{4}) -->\n(.*?)<!-- loj:end-row -->\n'
base_rows = {k:v for k,v in re.findall(pattern,before,re.S)}
next_rows = {k:v for k,v in re.findall(pattern,after,re.S)}
added = set(next_rows)-set(base_rows)
assert len(base_rows)==9 and len(next_rows)==12 and len(added)==3
assert all(next_rows[k]==v for k,v in base_rows.items())
expected = {
    '建国記念の日': ('成人の日',['建国記念の日','政令で定める日','建国をしのび、国を愛する心を養う。']),
    '敬老の日': ('こどもの日',['敬老の日','九月十五日','多年にわたり社会につくしてきた老人を敬愛し、長寿を祝う。']),
    '体育の日': ('秋分の日',['体育の日','十月十日','スポーツにしたしみ、健康な心身をつちかう。']),
}
ordered = []
for key,value in re.findall(pattern,after,re.S):
    cells = [x.decode('utf-8') for x in re.findall(rb'<!-- loj:cell -->\n(.*?)\n<!-- loj:end-cell -->',value,re.S)]
    if key in added:
        preceding, wanted = expected[cells[0]]
        assert cells==wanted and ordered[-1]==preceding
    ordered.append(cells[0])
without_added = re.sub(pattern,lambda m:b'' if m[1] in added else m[0],after,flags=re.S)
assert without_added==before, 'Unexpected change outside inserted rows'
assert (first/'supplement.md').read_bytes()==(second/'supplement.md').read_bytes()
for entry in json.loads((repo/'docs/sources/downloads.json').read_text(encoding='utf-8')):
    assert hashlib.sha256((repo/'docs/sources'/entry['file']).read_bytes()).hexdigest()==entry['sha256']
for line in snapshot['legacyRefs']:
    sha,ref = line.split(' ',1)
    if ref.startswith('refs/heads/trial/'):
        continue
    assert subprocess.check_output(['git','-C',str(repo),'rev-parse',ref],text=True).strip()==sha, ref
for p in list((repo/'versions').glob('*/*'))+[repo/'history.yaml',repo/'rebuild.yaml']:
    assert p.read_bytes().endswith(b'\n'), str(p)
invariants = {'originalRows':9,'amendedRows':12,'insertedRows':3,'unchangedOriginalRows':True,'unchangedOtherMainText':True,'unchangedSupplement':True,'sourceHashesMatch':True,'legacyRefsUnchanged':True,'addedRows':expected}
(out/'invariants.json').write_text(json.dumps(invariants,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'commands.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
provenance = {'binarySha256':hashlib.sha256(exe.read_bytes()).hexdigest(),'validatorCheckout':snapshot['loj-validator'],'specCommit':snapshot['loj-spec'],'note':'Directory checks, not canonical-commit certification. Binary hash identifies the executable; checkout HEAD is not a build attestation.'}
(out/'provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert all(x['exitCode']==0 for x in summary), 'See validation reports'
print('All checks and trial invariants passed.')
