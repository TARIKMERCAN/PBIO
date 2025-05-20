from Bio import Entrez,SeqIO
import pandas as pd,matplotlib.pyplot as plt
class R:
 def __init__(s,e,k):Entrez.email=e;Entrez.api_key=k;Entrez.tool='T'
 def s(s,t,m=None,x=None):
  try:
   o=Entrez.read(Entrez.efetch(db='taxonomy',id=t,retmode='xml'))[0]['ScientificName'];print(f'Organism: {o} (TaxID: {t})')
   q=f'txid{t}[Organism]'
   if m:q+=f' AND {m}:{x if x else 999999}[Sequence Length]'
   r=Entrez.read(Entrez.esearch(db='nucleotide',term=q,usehistory='y'))
   n=int(r['Count'])
   if not n:return print(f'No records found for {o}')
   print(f'Found {n} records')
   s.w,s.q,s.c=r['WebEnv'],r['QueryKey'],n
   return n
  except Exception as e:print(f'Error: {e}')
 def f(s,a=0,n=10):
  if not hasattr(s,'w')or not hasattr(s,'q'):return print('No search results.');[]
  try:
   h=Entrez.efetch(db='nucleotide',rettype='gb',retmode='text',retstart=a,retmax=min(n,500),webenv=s.w,query_key=s.q)
   return list(SeqIO.parse(h,'genbank'))
  except Exception as e:print(f'Error: {e}');return[]
 def csv(s,l,o):d=[{'A':r.id,'L':len(r.seq),'D':r.description}for r in l];df=pd.DataFrame(d);df.to_csv(o,index=0);print(f'CSV: {o}');return df
 def v(s,df,o):plt.figure(figsize=(12,6));plt.plot(range(len(df)),df.L,marker='o');plt.title('Lengths');plt.xlabel('Accession');plt.ylabel('Len');plt.grid(1);plt.xticks(range(len(df)),df.A,rotation=45,ha='right');plt.tight_layout();plt.savefig(o);print(f'Chart: {o}')
def main():
 e=input('Email for NCBI: ')
 k=input('NCBI API key: ')
 r=R(e,k)
 t=input('Taxid: ')
 m=input('Min len(enter for no min): ')
 x=input('Max len(enter for no max): ')
 m=int(m)if m else None
 x=int(x)if x else None
 n=r.s(t,m,x)
 if not n:return
 print('Fetching...')
 l=r.f(0,min(n,100))
 if not l:return
 df=r.csv(l,f'taxid_{t}_report.csv')
 r.v(df,f'taxid_{t}_chart.png')
if __name__=='__main__':main() 