#!/usr/bin/env python3
"""Compile the JVM crypto helper, then run the journal's complete browser suite."""
from pathlib import Path
import os,shutil,subprocess
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'qa/crypto-classes';OUT.mkdir(parents=True,exist_ok=True)
sources=[ROOT/'tests/CryptoCli.java',ROOT/'app/src/main/java/hu/emlekor/naplo/CryptoBox.java']
if os.environ.get('ECJ_JAR'):
    java=Path(shutil.which('java')).resolve().parent.parent
    boot=java/'jmods/java.base.jmod'
    if not boot.is_file():boot=java/'lib/jrt-fs.jar'
    compiler=['java','-jar',os.environ['ECJ_JAR'],'-bootclasspath',str(boot),'-source','8','-target','8']
else:compiler=['javac','-source','8','-target','8']
subprocess.run([*compiler,'-encoding','UTF-8','-d',str(OUT),*map(str,sources)],cwd=ROOT,check=True)
for test in ['tests/test-app.cjs','tests/test-offline.cjs','tests/test-growth.cjs']:
    print('Running',test,flush=True)
    subprocess.run(['node',test],cwd=ROOT,check=True)
